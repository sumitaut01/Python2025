from copyreg import constructor

import pytest

@pytest.mark.usefixtures("setup")
class Tests:

# PyTest wont accept below constructor
    # def __init__(self):
    #     print("Test inside class")

    def test_first(self):
        print("executed firstcase from class")

        def test_second(self):
        print("executed second from class")


    def test_third(self,datawith_params):
        print("executed third from class")
