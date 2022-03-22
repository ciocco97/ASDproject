from data.matrix_parser import MatrixParser
from subset import Subset


class RepresentativeVector:

    def __init__(self, size, sigma):
        self.vector = [0] * size
        self.set = sigma

    def set_sigma_i_val(self, n_i_index, val):
        self.vector[n_i_index] = val
