import json

import pytest

path="data/data.json"
with open(path) as f:
    data = json.load(f)

@pytest.mark.parametrize("multivariable",data["data"])
def test_second(multivariable):
    print(print(multivariable["username"]))
