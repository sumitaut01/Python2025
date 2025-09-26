import pytest

@pytest.mark.usefixtures("setup")
class Tests:

    def __init__(self):
        print("Test inside class")

    def test_first(self,):
        print("executed firstcase from class")

    def test_second(self):
        print("executed second from class")
