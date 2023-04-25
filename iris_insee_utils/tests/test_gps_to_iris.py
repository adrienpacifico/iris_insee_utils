from iris_insee_utils.gps_to_iris import gps_to_iris
print(gps_to_iris(5.36413,43.23871))


from iris_insee_utils.gps_to_iris import gps_to_iris

def test_gps_to_iris():
    df = gps_to_iris(5.36413,43.23871)
    print(df)
    assert df.CODE_IRIS.values[0] == '132080302'

if __name__ == "__main__":
    test_gps_to_iris()

    