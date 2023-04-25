"""This module test functions associated with preparing the IGN geographical data."""
import iris_insee_utils
from iris_insee_utils.download_data import (
    download,
    prepare_data_,
    unzip_downloaded_file,
)

URL = "https://wxs.ign.fr/1yhlj2ehpqf3q6dt6a2y7b64/telechargement/inspire/CONTOURS-IRIS-2018-01-02$CONTOURS-IRIS_2-1__SHP__FRA_2018-01-01/file/CONTOURS-IRIS_2-1__SHP__FRA_2018-01-01.7z"

DATA_PATH = iris_insee_utils.__path__[0] + "/../data"
FILE_TO_WRITE_PATH = DATA_PATH + "/raw/iris_2018.7z"


def test_downlad():
    """test the download of IGN data for shapefiles"""
    download(URL, DATA_PATH + "/raw/iris_2018.7z")


def test_unzip_downloaded_file():
    """test for unziping the downloaded file (in .7z format)"""
    unzip_downloaded_file(FILE_TO_WRITE_PATH, DATA_PATH + "/raw")


def test_prepare_data():
    """test prepare data (transform shapefile to feather file format)"""
    prepare_data_(DATA_PATH)
