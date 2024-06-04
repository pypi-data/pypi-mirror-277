import logging

import fiona
import pyproj
from fiona.transform import transform_geom
from rasterio.crs import CRS
from shapely.errors import TopologicalError
from shapely.geometry import (
    GeometryCollection,
    LinearRing,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Polygon,
    base,
    box,
    mapping,
    shape,
)
from shapely.validation import explain_validity

from mapchete.errors import GeometryTypeError, ReprojectionFailed
from mapchete.validate import validate_crs

logger = logging.getLogger(__name__)


CRS_BOUNDS = {
    # http://spatialreference.org/ref/epsg/wgs-84/
    "epsg:4326": (-180.0, -90.0, 180.0, 90.0),
    # unknown source
    "epsg:3857": (-180.0, -85.0511, 180.0, 85.0511),
    # http://spatialreference.org/ref/epsg/3035/
    "epsg:3035": (-10.6700, 34.5000, 31.5500, 71.0500),
}


def _reproject_geom(
    geometry, src_crs, dst_crs, validity_check, antimeridian_cutting, fiona_env
):
    if geometry.is_empty:
        return geometry
    else:
        with fiona.env.Env(**fiona_env):
            try:
                transformed = transform_geom(
                    src_crs.to_dict(),
                    dst_crs.to_dict(),
                    mapping(geometry),
                    antimeridian_cutting=antimeridian_cutting,
                )
            except Exception as exc:
                raise ReprojectionFailed(
                    f"fiona.transform.transform_geom could not transform geometry from {src_crs} to {dst_crs}"
                ) from exc
        # Fiona >1.9 returns None if transformation errored
        if transformed is None:  # pragma: no cover
            raise ReprojectionFailed(
                f"fiona.transform.transform_geom could not transform geometry from {src_crs} to {dst_crs}"
            )
        out_geom = to_shape(transformed)
        return _repair(out_geom) if validity_check else out_geom


def _segmentize_value(geometry, segmentize_fraction):
    height = geometry.bounds[3] - geometry.bounds[1]
    width = geometry.bounds[2] - geometry.bounds[0]
    return min([height, width]) / segmentize_fraction


def reproject_geometry(
    geometry,
    src_crs=None,
    dst_crs=None,
    clip_to_crs_bounds=True,
    error_on_clip=False,
    segmentize_on_clip=False,
    segmentize=False,
    segmentize_fraction=100,
    validity_check=True,
    antimeridian_cutting=False,
    retry_with_clip=True,
    fiona_env=None,
):
    """
    Reproject a geometry to target CRS.

    Also, clips geometry if it lies outside the destination CRS boundary.
    Supported destination CRSes for clipping: 4326 (WGS84), 3857 (Spherical
    Mercator) and 3035 (ETRS89 / ETRS-LAEA).

    Parameters
    ----------
    geometry : ``shapely.geometry``
    src_crs : ``rasterio.crs.CRS`` or EPSG code
        CRS of source data
    dst_crs : ``rasterio.crs.CRS`` or EPSG code
        target CRS
    error_on_clip : bool
        raises a ``RuntimeError`` if a geometry is outside of CRS bounds
        (default: False)
    validity_check : bool
        checks if reprojected geometry is valid and throws ``TopologicalError``
        if invalid (default: True)
    clip_to_crs_bounds : bool
        Always clip geometries to CRS bounds. (default: True)
    antimeridian_cutting : bool
        cut geometry at Antimeridian; can result in a multipart output geometry

    Returns
    -------
    geometry : ``shapely.geometry``
    """
    src_crs = validate_crs(src_crs)
    dst_crs = validate_crs(dst_crs)
    fiona_env = fiona_env or {}
    try:
        geometry = (
            geometry if isinstance(geometry, base.BaseGeometry) else shape(geometry)
        )
    except Exception:  # pragma: no cover
        raise TypeError(f"invalid geometry type: {type(geometry)}")

    # return repaired geometry if no reprojection needed
    if src_crs == dst_crs or geometry.is_empty:
        return _repair(geometry)
    # geometry needs to be clipped to its CRS bounds
    elif (
        clip_to_crs_bounds
        and dst_crs.is_epsg_code
        and dst_crs.get("init")
        != "epsg:4326"  # and is not WGS84 (does not need clipping)
        and (
            dst_crs.get("init") in CRS_BOUNDS
            or pyproj.CRS(dst_crs.to_epsg()).area_of_use.bounds
        )
    ):
        wgs84_crs = CRS().from_epsg(4326)
        # get dst_crs boundaries
        crs_bbox = box(
            *CRS_BOUNDS.get(
                dst_crs.get("init"), pyproj.CRS(dst_crs.to_epsg()).area_of_use.bounds
            )
        )
        # reproject geometry to WGS84
        geometry_4326 = _reproject_geom(
            geometry,
            src_crs,
            wgs84_crs,
            validity_check,
            antimeridian_cutting,
            fiona_env,
        )
        # raise error if geometry has to be clipped
        if error_on_clip and not geometry_4326.within(crs_bbox):
            raise RuntimeError("geometry outside target CRS bounds")

        clipped = crs_bbox.intersection(geometry_4326)

        # segmentize clipped geometry using one 100th of with or height depending on
        # which is shorter
        if segmentize_on_clip or segmentize:
            clipped = segmentize_geometry(
                clipped, _segmentize_value(clipped, segmentize_fraction)
            )

        # clip geometry dst_crs boundaries and return
        return _reproject_geom(
            clipped, wgs84_crs, dst_crs, validity_check, antimeridian_cutting, fiona_env
        )

    # return without clipping if destination CRS does not have defined bounds
    else:
        try:
            if segmentize:
                return _reproject_geom(
                    segmentize_geometry(
                        geometry, _segmentize_value(geometry, segmentize_fraction)
                    ),
                    src_crs,
                    dst_crs,
                    validity_check,
                    antimeridian_cutting,
                    fiona_env,
                )
            else:
                return _reproject_geom(
                    geometry,
                    src_crs,
                    dst_crs,
                    validity_check,
                    antimeridian_cutting,
                    fiona_env,
                )
        except TopologicalError:  # pragma: no cover
            raise
        except ValueError as exc:  # pragma: no cover
            if retry_with_clip:
                logger.error(
                    "error when transforming %s from %s to %s: %s, trying to use CRS bounds clip",
                    geometry,
                    src_crs,
                    dst_crs,
                    exc,
                )
                try:
                    return reproject_geometry(
                        geometry,
                        src_crs=src_crs,
                        dst_crs=dst_crs,
                        clip_to_crs_bounds=True,
                        error_on_clip=error_on_clip,
                        segmentize_on_clip=segmentize_on_clip,
                        segmentize=segmentize,
                        segmentize_fraction=segmentize_fraction,
                        validity_check=validity_check,
                        antimeridian_cutting=antimeridian_cutting,
                        retry_with_clip=False,
                    )
                except Exception as exc:
                    raise ReprojectionFailed(
                        f"geometry cannot be reprojected: {str(exc)}"
                    )
            else:
                raise


def _repair(geom):
    repaired = geom.buffer(0) if geom.geom_type in ["Polygon", "MultiPolygon"] else geom
    if repaired.is_valid:
        return repaired
    else:
        raise TopologicalError(
            "geometry is invalid (%s) and cannot be repaired"
            % explain_validity(repaired)
        )


def segmentize_geometry(geometry, segmentize_value):
    """
    Segmentize Polygon outer ring by segmentize value.

    Just Polygon geometry type supported.

    Parameters
    ----------
    geometry : ``shapely.geometry``
    segmentize_value: float

    Returns
    -------
    geometry : ``shapely.geometry``
    """
    if geometry.geom_type != "Polygon":
        raise TypeError("segmentize geometry type must be Polygon")

    return Polygon(
        LinearRing(
            [
                p
                # pick polygon linestrings
                for l in map(
                    lambda x: LineString([x[0], x[1]]),
                    zip(geometry.exterior.coords[:-1], geometry.exterior.coords[1:]),
                )
                # interpolate additional points in between and don't forget end point
                for p in [
                    l.interpolate(segmentize_value * i).coords[0]
                    for i in range(int(l.length / segmentize_value))
                ]
                + [l.coords[1]]
            ]
        )
    )


def to_shape(geom) -> base.BaseGeometry:
    """
    Convert geometry to shapely geometry if necessary.

    Parameters
    ----------
    geom : shapely geometry or GeoJSON mapping

    Returns
    -------
    shapely geometry
    """
    if isinstance(geom, base.BaseGeometry):
        return geom
    elif hasattr(geom, "__geo_interface__") and geom.__geo_interface__.get("geometry"):
        return shape(geom.__geo_interface__["geometry"])
    else:
        return shape(geom)


def multipart_to_singleparts(geom):
    """
    Yield single part geometries if geom is multipart, otherwise yield geom.

    Parameters
    ----------
    geom : shapely geometry

    Returns
    -------
    shapely single part geometries
    """
    if isinstance(geom, base.BaseGeometry):
        if hasattr(geom, "geoms"):
            for subgeom in geom.geoms:
                yield subgeom
        else:
            yield geom


def clean_geometry_type(
    geometry, target_type, allow_multipart=True, raise_exception=True
):
    """
    Return geometry of a specific type if possible.

    Filters and splits up GeometryCollection into target types. This is
    necessary when after clipping and/or reprojecting the geometry types from
    source geometries change (i.e. a Polygon becomes a LineString or a
    LineString becomes Point) in some edge cases.

    Parameters
    ----------
    geometry : ``shapely.geometry``
    target_type : string
        target geometry type
    allow_multipart : bool
        allow multipart geometries (default: True)

    Returns
    -------
    cleaned geometry : ``shapely.geometry``
        returns None if input geometry type differs from target type

    Raises
    ------
    GeometryTypeError : if geometry type does not match target_type
    """
    if target_type == "Unknown":  # pragma: no cover
        return geometry

    multipart_geoms = {
        "Point": MultiPoint,
        "LineString": MultiLineString,
        "Polygon": MultiPolygon,
        "MultiPoint": MultiPoint,
        "MultiLineString": MultiLineString,
        "MultiPolygon": MultiPolygon,
    }
    if target_type not in multipart_geoms.keys():
        raise TypeError("target type is not supported: %s" % target_type)

    if geometry.geom_type == target_type:
        return geometry

    elif allow_multipart:
        target_multipart_type = multipart_geoms[target_type]
        if geometry.geom_type == "GeometryCollection":
            return target_multipart_type(
                [
                    clean_geometry_type(
                        g, target_type, allow_multipart, raise_exception=raise_exception
                    )
                    for g in geometry.geoms
                ]
            )
        elif (
            isinstance(geometry, target_multipart_type)
            or multipart_geoms[geometry.geom_type] == target_multipart_type
        ):
            return geometry

    if raise_exception:
        raise GeometryTypeError(
            "geometry type does not match: %s, %s" % (geometry.geom_type, target_type)
        )

    else:
        return GeometryCollection()
