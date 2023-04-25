import iris_insee_utils
import geopandas as gpd

df_map = gpd.read_feather(iris_insee_utils.__path__[0]+'/../data/transformed/iris_2018.feather')
df_map = df_map.to_crs(epsg=4326)

def gps_to_iris(long, lat, iris_year=2018):
    """
    Get the longtitude and latitude of gps point(s), and returns the CODE IRIS 
    """
    


    gdf = gpd.GeoDataFrame(
        geometry=gpd.points_from_xy([long], [lat])
    )

    gdf.crs = "EPSG:4326"
    gdf = gdf.to_crs(epsg=4326)
    df = gpd.sjoin(gdf.head(1), df_map,predicate='within') 
    df
    return df
    