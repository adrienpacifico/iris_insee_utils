import iris_insee_utils
import geopandas as gpd

def prepare_data_():
    raw_path = iris_insee_utils.__path__[0]+'/../dataf'#/data/raw'#/IRIS_GE.SHP'
    import os
    print(raw_path)
    print(os.path.isdir(raw_path))
    print(os.listdir(raw_path))
   # print(iris_insee_utils.__path__[0]+'/data/raw/IRIS_GE.SHP')
    #df_map = gpd.read_file(iris_insee_utils.__path__[0]+'/data/raw/IRIS_GE.SHP')
    #df_map.to_feather(iris_insee_utils.__path__[0]+'/data/iris_2018.feather')

if __name__ == "__main__":
    prepare_data_()

