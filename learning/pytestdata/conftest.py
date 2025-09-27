import pytest

@pytest.fixture(scope="function")
def setup():
    print("setup")
    yield
    print("teardown")


@pytest.fixture()
def data():
   return ["sumit","raut",35]


@pytest.fixture(params=[1,2,3,4])
def datawith_params(request):
   return request.param

