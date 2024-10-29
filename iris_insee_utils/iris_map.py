"""This module is test that gps coordinates are linking to the correct IRIS."""

from iris_insee_utils.gps_to_iris import gps_to_iris
import pandas as pd
from loguru import logger
import geopandas as gpd
import folium
from tqdm import tqdm

def plot_folium_map(iris_year=None, commune_name="Marseille", df_oi: pd.DataFrame=None, df_enrich: pd.DataFrame=None,
                    df_enrich_iriscol_colname=None, df_enrich_select_cols=None, save_map=False):
    """
    Plot a folium map of iris, for a given commune, or departement number.
    """
    df_map = gpd.read_parquet(f"data/transformed/iris_{iris_year}.parquet").to_crs(epsg=4326) # TODO: add this to the cleaning function
    df_map["NOM_COM"]=df_map.NOM_COM.str.strip() # remove leading and trailing spaces, TODO: add this to the cleaning function
    df_map = df_map[df_map.NOM_COM.str.contains(commune_name,case=True)]#df_map = df_map.query("NOM_COM == @commune_name")
    print(df_map)
    map = folium.Map(location=[df_map.geometry.centroid.y.mean(), df_map.geometry.centroid.x.mean()], zoom_start=12)
    for _, r in df_map.iterrows():
        # Without simplifying the representation of each borough,
        # the map might not be displayed
        sim_geo = gpd.GeoSeries(r['geometry'])#.simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j,smooth_factor=.1,
                            style_function=lambda x: {'fillColor': 'lightblue'})
        folium.Popup("Code iris: "+r['CODE_IRIS']+"<br>"
                    +"nom iris: "+ r['NOM_IRIS'] + "<br>"
                    + "Commune: "+ r['NOM_COM'] + "<br>"
                
                    ).add_to(geo_j)
        geo_j.add_to(map)
    
    



    if df_enrich:
        raise NotImplementedError("This functionality has not been implemented yet.")
    if save_map:
        raise NotImplementedError("This functionality has not been implemented yet.")
        # 
        map.save("index.html")
    
    logger.warning("Test")
    return map





if __name__ == '__main__':
    plot_folium_map(iris_year=2018, commune_name="Nice")

    