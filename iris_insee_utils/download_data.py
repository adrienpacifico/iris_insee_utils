#TODO

#https://geoservices.ign.fr/contoursiris
import iris_insee_utils
import geopandas as gpd

DATA_PATH = iris_insee_utils.__path__[0]+'/../data'
data_path = iris_insee_utils.__path__[0]+'/../data'

from tqdm import tqdm
import requests

url = "https://wxs.ign.fr/1yhlj2ehpqf3q6dt6a2y7b64/telechargement/inspire/CONTOURS-IRIS-2018-01-02$CONTOURS-IRIS_2-1__SHP__FRA_2018-01-01/file/CONTOURS-IRIS_2-1__SHP__FRA_2018-01-01.7z"




def download(url, filename):
    import functools
    import pathlib
    import shutil
    import requests
    from tqdm.auto import tqdm
    
    r = requests.get(url, stream=True, allow_redirects=True)
    if r.status_code != 200:
        r.raise_for_status()  # Will only raise for 4xx codes, so...
        raise RuntimeError(f"Request to {url} returned status code {r.status_code}")
    file_size = int(r.headers.get('Content-Length', 0))

    path = pathlib.Path(filename).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

    desc = "(Unknown total file size)" if file_size == 0 else ""
    r.raw.read = functools.partial(r.raw.read, decode_content=True)  # Decompress if needed
    with tqdm.wrapattr(r.raw, "read", total=file_size, desc=desc) as r_raw:
        with path.open("wb") as f:
            shutil.copyfileobj(r_raw, f)

    return path

def unzip_downloaded_file(file_to_unzip=None,extract_path="/raw" ):
    import os 
    import py7zr
    print(extract_path)
    Path(extract_path).mkdir(parents=True, exist_ok=True)  ### TODO: Faire mieux pour utiliser l'absolute path (pour que ça marche peu importe d'ou on lance le script)
    with py7zr.SevenZipFile(file_to_unzip, mode='r') as z:
        z.extractall(path="./data/raw")

from pathlib import Path


def prepare_data_(data_path=None):
    """
    Transform .SHP file to feather for faster data loading.
    """
    import os
    df_map = gpd.read_file(data_path+"/raw/CONTOURS-IRIS_2-1__SHP__FRA_2018-01-01/CONTOURS-IRIS/1_DONNEES_LIVRAISON_2018-07-00057/CONTOURS-IRIS_2-1_SHP_LAMB93_FXX-2018")
    Path(DATA_PATH+"/transformed").mkdir(parents=True, exist_ok=True)
    df_map.to_feather(data_path+'/transformed/iris_2018.feather')

if __name__ == "__main__":
    file_to_write_path = DATA_PATH+"/raw/iris_2018.7z"
    download(url, file_to_write_path)
    unzip_downloaded_file(file_to_write_path, DATA_PATH+"/raw")
    prepare_data_(data_path=DATA_PATH)
