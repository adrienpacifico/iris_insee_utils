[![codecov](https://codecov.io/gh/adrienpacifico/iris_insee_utils/branch/master/graph/badge.svg?token=ZZItjohsp9)](https://codecov.io/gh/adrienpacifico/iris_insee_utils)
The goal of this pandas repository is to provide an easy solution to determine to which iris gps point correspond to.
This could be extended to an transformation from adress to iris.

Due to legal uncertainties, you will have to download the IGN dataset first. 

### Usage:

 ```python

>>>from iris_insee_util import gps_to_iris

>>>gps_to_iris(lat, long, iris_year=2018)
 ```