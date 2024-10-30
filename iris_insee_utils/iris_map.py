"""This module is test that gps coordinates are linking to the correct IRIS."""
import os

import iris_insee_utils
from iris_insee_utils.gps_to_iris import gps_to_iris
import pandas as pd
from loguru import logger
import geopandas as gpd
import folium
from tqdm import tqdm


from loguru import logger

def plot_folium_map(iris_year, commune_name="Marseille", df_oi: pd.DataFrame=None, df_enrich: pd.DataFrame=None,
                    df_enrich_iriscol_colname=None, df_enrich_select_cols=None, save_map=False):
    """
    Plot a folium map of iris, for a given commune, or departement number.
    """

    file_path = os.path.join(os.path.dirname(iris_insee_utils.__file__),
                                f"../data/transformed/iris_{iris_year}.parquet")
                                

    df_map = gpd.read_parquet(file_path).to_crs(epsg=4326) # TODO: add this to the cleaning function
    df_map["NOM_COM"]=df_map.NOM_COM.str.strip() # remove leading and trailing spaces, TODO: add this to the cleaning function
    df_map = df_map[df_map.NOM_COM.str.contains(commune_name,case=True)]#df_map = df_map.query("NOM_COM == @commune_name")
    m = folium.Map(location=[df_map.geometry.centroid.y.mean(), df_map.geometry.centroid.x.mean()], zoom_start=12)
    for _, row in df_map.iterrows():
        sim_geo = gpd.GeoSeries(row['geometry'])#.simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j,smooth_factor=.1,
                            style_function=lambda x: {'fillColor': 'lightblue'})
        folium.Popup("Code iris: "+row['CODE_IRIS']+"<br>"
                    +"nom iris: "+ row['NOM_IRIS'] + "<br>"
                    + "Commune: "+ row['NOM_COM'] + "<br>"
                
                    ).add_to(geo_j)
        geo_j.add_to(m)

    if df_oi is not None:

        for _, row in df_oi.iterrows():
            location = [row["lat"], row["lon"]]
            tooltip = ""
            for column_name, value in row.items():
                if column_name not in ["lat", "lon"]:
                    tooltip += f"{column_name}: {value}<br>"
            
            m.add_child(folium.Marker(location=[row["lat"], row["lon"]],#icon=icon, 
                                tooltip=  tooltip
                                )
                    )

    if df_enrich:
        raise NotImplementedError("This functionality has not been implemented yet.")
    if save_map:
        raise NotImplementedError("This functionality has not been implemented yet.")
        # 
        m.save("index.html")
    
    logger.warning("Test")
    return m





if __name__ == '__main__':
    plot_folium_map(iris_year=2018, commune_name="Nice")

    