from data.matrix_parser import MatrixParser
from subset import Subset


class RepresentativeVector:
    X_VAL = -1

    def __init__(self, size):
        self.vector = [0] * size

    def __str__(self) -> str:
        return self.vector_to_str()

    def vector_to_str(self) -> str:
        return ' '.join(map(str, self.vector))

    def set_val_by_index(self, n_i_index, val):
        self.vector[n_i_index] = val

    def get_values(self):
        return self.vector
