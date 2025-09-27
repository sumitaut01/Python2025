import pytest


@pytest.mark.smoke
def test_marked():
    print("executed test")


@pytest.mark.skip
def test_skipped():
    print("executed test")