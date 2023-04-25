import iris_insee_utils
from iris_insee_utils.download_data import download, unzip_downloaded_file
from iris_insee_utils.prepare_data import prepare_data_




url = "https://wxs.ign.fr/1yhlj2ehpqf3q6dt6a2y7b64/telechargement/inspire/CONTOURS-IRIS-2018-01-02$CONTOURS-IRIS_2-1__SHP__FRA_2018-01-01/file/CONTOURS-IRIS_2-1__SHP__FRA_2018-01-01.7z"

data_path = iris_insee_utils.__path__[0]+'/../data'

#def test_downlad():
#    download(url, "data/to_trash666.25avril")

#def test_unzip_downloaded_file():
#    unzip_downloaded_file(data_path+"/to_trash666.25avril")

def test_prepare_data():
    prepare_data_()



if __name__ == "__main__":
    test_gps_to_iris()