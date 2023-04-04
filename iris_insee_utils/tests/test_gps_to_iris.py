from iris_insee_utils.gps_to_iris import gps_to_iris

def test_gps_to_iris():
    assert gps_to_iris(43.23871,5.36413) == 132080302
    