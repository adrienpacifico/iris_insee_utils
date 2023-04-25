"""This module is test that gps coordinates are linking to the correct IRIS."""

from iris_insee_utils.gps_to_iris import gps_to_iris


def test_gps_to_iris():
    """
    test that gps point output the correct iris
    """
    result_df = gps_to_iris(5.36413, 43.23871)
    assert result_df.CODE_IRIS.values[0] == "132080302"
