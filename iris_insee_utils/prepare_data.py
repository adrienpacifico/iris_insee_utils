import iris_insee_utils
import geopandas as gpd
from pathlib import Path

DATA_PATH = iris_insee_utils.__path__[0]+'/../data'

def prepare_data_():
    """
    Transform .SHP file to feather for faster data loading.
    """
    data_path = DATA_PATH
    import os
    df_map = gpd.read_file(data_path+"/raw/CONTOURS-IRIS_2-1__SHP__FRA_2018-01-01/CONTOURS-IRIS/1_DONNEES_LIVRAISON_2018-07-00057/CONTOURS-IRIS_2-1_SHP_LAMB93_FXX-2018")
    Path(DATA_PATH+"/transformed").mkdir(parents=True, exist_ok=True)
    df_map.to_feather(data_path+'/transformed/iris_2018.feather')

if __name__ == "__main__":
    prepare_data_()

