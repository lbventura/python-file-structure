import pytest
from random_matrix.helper_functions.random_parameters import LENGTH_OF_RANDOM_LIST


def test_length_of_random_list():
    assert LENGTH_OF_RANDOM_LIST < 100


@pytest.mark.xfail(reason="This is the wrong type")
def test_type_length_of_random_list():
    assert type(LENGTH_OF_RANDOM_LIST) is str
