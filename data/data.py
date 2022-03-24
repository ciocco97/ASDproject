import copy

from data.matrix_parser import MatrixParser
from representative_vector import RepresentativeVector


class Data:

    def __init__(self, file_number: int = 0):
        self.matrix_parser = MatrixParser()
        self.matrix_parser.parse_file_number_n(file_number)

        self.singlet_representative_vector = {}
        self.representative_vector_size = self.matrix_parser.get_sets_number()

        # calcolo dei vettori rappresentativi dei singoletti
        for symbol in self.matrix_parser.get_domain():
            current_repr_vector = RepresentativeVector(self.representative_vector_size, [symbol])
            for k, n_i in enumerate(self.matrix_parser.matrix_lexiconographic()):
                if symbol in n_i:
                    current_repr_vector.set_sigma_i_val(k, symbol)
            self.singlet_representative_vector[symbol] = current_repr_vector

    def get_representative_vector(self, symbol: int) -> RepresentativeVector:
        return self.singlet_representative_vector[symbol]

    def get_domain_size(self):
        return self.matrix_parser.get_domain_size()

    def get_domain(self):
        return self.matrix_parser.get_domain()
