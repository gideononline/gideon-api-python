from typing import Optional
import fiona
import geopandas
from geopandas.geodataframe import GeoDataFrame
from shapely.geometry import Point

_LAT = 'latitude'
_LON = 'longitude'
_CENTROID = 'centroid'


def _get_centroid(series, lat_col: str = _LAT, lon_col: str = _LON) -> Point:
    """Returns a point from the lat/lon columns"""
    return Point(float(series[lat_col]), float(series[lon_col]))


def to_geojson(df,
               filename: str,
               return_geodataframe: bool = True) -> Optional[GeoDataFrame]:
    """Exports a dataframe containing latitude and longitude data to a GeoJSON
        file to be used in other programs.
    
    Args:
        df (DataFrame): The dataframe with the columns "latitude" and "longitude"
        filename: the name of the GeoJSON file saved the computer. The save
            location is relative to the current working directory.
        return_geodataframe: Indicates if the underlying GeoDataFrame should
            be returned as a Python object, in addition to the expored GeoJSON
            file.
    
    Returns:
        Optionally returns the GeoDataFrame of the input dataframe.
    """
    # Check if the dataframe has lat/lon data
    if _LAT in df and _LON in df:
        df = df[df[_LAT].notna() & df[_LON].notna()].copy()
        # Temporary fix for latitude and longitude reversed
        df[_CENTROID] = df.apply(lambda x: _get_centroid(x, _LON, _LAT),
                                 'columns')
        gdf = geopandas.GeoDataFrame(df, geometry=_CENTROID)
        gdf.to_file(filename, 'GeoJSON')
        return gdf
    else:
        raise ValueError('Latitude/Longitude data not in dataframe')
