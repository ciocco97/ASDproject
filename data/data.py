from data.matrix_parser import MatrixParser
from representative_vector import RepresentativeVector
from subset import Subset


class Data:

    def __init__(self, file_number: int = 0):
        self.matrix_parser = MatrixParser()
        self.matrix_parser.parse_file_number_n(file_number)

        self.N = self.matrix_parser.get_sets_number()
        RepresentativeVector.X_VAL = -1 * (self.matrix_parser.get_domain_size() + 1)

        self.singlet_representative_vectors = {}
        self.representative_vectors = {}
        # the representative vector of the empty subset is the null vector of size N
        self.singlet_representative_vectors[0] = RepresentativeVector(self.N)

        # calcolo dei vettori rappresentativi dei singoletti
        for symbol in self.matrix_parser.get_domain():
            current_repr_vector = RepresentativeVector(self.N)
            for k, n_i in enumerate(self.matrix_parser.matrix_lexiconographic()):
                if symbol in n_i:
                    current_repr_vector.set_val_by_index(k, symbol)
            self.singlet_representative_vectors[symbol] = current_repr_vector

    def get_representative_vectors(self) -> dict:
        return self.representative_vectors

    def get_representative_vector(self, index_set: Subset) -> RepresentativeVector:
        if index_set.get_size() == 1:
            return self.get_singlet_representative_vector(index_set.get_components()[0])
        return self.representative_vectors[index_set.__hash__()]

    def get_singlet_representative_vector(self, symbol: int) -> RepresentativeVector:
        return self.singlet_representative_vectors[symbol]

    def add_representative_vector(self, sigma: Subset, representative_vector: RepresentativeVector):
        self.representative_vectors[hash(sigma)] = representative_vector

    def get_domain_size(self):
        return self.matrix_parser.get_domain_size()

    def get_domain(self):
        return self.matrix_parser.get_domain()
