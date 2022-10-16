class Metadata:
    def __init__(self, matrix_dimension: int):
        self.matrix_dimension = matrix_dimension

    def __repr__(self):
        return f"The dimension of this random matrix is {self.matrix_dimension}"
