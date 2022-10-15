import pandas as pd
import numpy
from random_matrix.helper_functions import create_random_integer


def generate_random_dataframe() -> pd.DataFrame:
    random_mat_dimen = create_random_integer()
    random_df = pd.DataFrame(numpy.random.random((random_mat_dimen, random_mat_dimen)))
    return random_df
