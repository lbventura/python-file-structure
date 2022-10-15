from random_matrix.generate_random_dataframe import generate_random_dataframe


def test_random_dataframe_dimension():
    assert len(generate_random_dataframe()) < 100
