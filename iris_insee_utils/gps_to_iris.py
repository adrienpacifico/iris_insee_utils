import iris_insee_utils
import geopandas as gpd

df_map = gpd.read_file(iris_insee_utils.__path__[0]+'/../data/raw/IRIS_GE.SHP')
df_map.head()
df_mars = df_map[df_map.NOM_COM.str.contains("Marseille ",case=True)]






def gps_to_iris(long, lat, iris_year=2018):
    """
    Get the longtitude and latitude of gps point(s), and returns the CODE IRIS 
    """
    
    gdf = gpd.GeoDataFrame(
        geometry=gpd.points_from_xy([43.2387], [5.36413])
        )
    gdf.crs = "EPSG:4326"
    gdf = gdf.to_crs(epsg=4326)

    df = gpd.sjoin(gdf, df_mars,predicate='within') 
    return df.CODE_IRIS