from copyreg import constructor

import pytest

@pytest.mark.usefixtures("data")
@pytest.mark.usefixtures("setup")
class TestsWithData:



    def test_first(self,data):
        print("using data from fixture")
        print(data)

#learning/pytestdata/test_08Classwithdatafixture.py::TestsWithData::test_first PASSED [100%]using data from fixture
#['sumit', 'raut', 35]
