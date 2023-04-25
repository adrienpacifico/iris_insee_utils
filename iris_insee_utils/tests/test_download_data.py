import iris_insee_utils
from iris_insee_utils.download_data import download, unzip_downloaded_file, prepare_data_




url = "https://wxs.ign.fr/1yhlj2ehpqf3q6dt6a2y7b64/telechargement/inspire/CONTOURS-IRIS-2018-01-02$CONTOURS-IRIS_2-1__SHP__FRA_2018-01-01/file/CONTOURS-IRIS_2-1__SHP__FRA_2018-01-01.7z"

DATA_PATH = iris_insee_utils.__path__[0]+'/../data'
file_to_write_path = DATA_PATH+"/raw/iris_2018.7z"

def test_downlad():
    download(url, DATA_PATH+"/raw/iris_2018.7z")

def test_unzip_downloaded_file():
    unzip_downloaded_file(file_to_write_path, DATA_PATH+"/raw")

def test_prepare_data():
    prepare_data_(DATA_PATH)
