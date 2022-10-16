from random_matrix.generate_random_dataframe import RandomDataFrame


def test_random_dataframe_dimension():
    r1 = RandomDataFrame()
    assert r1.metadata.matrix_dimension < 100
