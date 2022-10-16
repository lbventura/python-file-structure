from random_matrix.helper_functions import Metadata


def test_metadata_repr():
    met_1 = Metadata(5)
    assert met_1.__repr__() == "The dimension of this random matrix is 5"
