import pandas as pd
import numpy
from random_matrix.helper_functions import create_random_integer, Metadata


class RandomDataFrame:
    def __init__(self):
        self.metadata = Metadata(create_random_integer())

    def generate_random_dataframe(self) -> pd.DataFrame:
        random_mat_dimen = self.metadata.matrix_dimension
        random_df = pd.DataFrame(
            numpy.random.random((random_mat_dimen, random_mat_dimen))
        )
        return random_df
