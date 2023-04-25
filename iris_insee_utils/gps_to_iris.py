"""This module test functions that are related to giving iris information from geographical data."""
import geopandas as gpd

import iris_insee_utils


def gps_to_iris(long, lat, iris_year=2018):
    """
    Get the longtitude and latitude of gps point(s), and returns the CODE IRIS
    """
    if iris_year == 2018:
        df_ign_map = gpd.read_feather(
            iris_insee_utils.__path__[0] + "/../data/transformed/iris_2018.feather"
        )
        df_ign_map = df_ign_map.to_crs(epsg=4326)
    else:
        raise NotImplementedError("Pour l'instant ne marche qu'avec les IRIS 2018")
    gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy([long], [lat]))

    gdf.crs = "EPSG:4326"
    gdf = gdf.to_crs(epsg=4326)
    result_df = gpd.sjoin(gdf.head(1), df_ign_map, predicate="within")
    return result_df
