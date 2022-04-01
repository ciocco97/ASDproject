from data_structure.representative_vector import RepresentativeVector
from data_structure.subset import Subset
import logging


class ProblemInstance:

    def __init__(self, matrix_one_zero):
        self.M = 0
        self.N = 0

        self.matrix_lex = []
        self.singlet_representative_vectors = []
        self.representative_vectors = {}

        self.conf(matrix_one_zero)

    def conf(self, matrix_one_zero):

        self.N = len(matrix_one_zero)
        self.M = len(matrix_one_zero[0])

        self.set_matrix_lex(matrix_one_zero)
        # logging.info(f"List of Subsets: {self.matrix_lex}")

        RepresentativeVector.X_VAL = -1 * (self.M + 1)
        # the representative vector of the empty subset is the null vector of size N
        rv_zero = RepresentativeVector([0]*self.N)
        self.add_singlet_rv(0, rv_zero)

        # computation of the representative vectors of the singletties :')
        for singlet in range(1, self.M + 1):
            values = [0] * self.N
            for i, N_i in enumerate(self.matrix_lex):
                values[i] = singlet if singlet in N_i else 0
            self.add_singlet_rv(singlet, RepresentativeVector(values))

    def set_M(self, M):
        self.M = M

    def set_N(self, N):
        self.N = N

    def set_matrix_lex(self, matrix_one_zero):
        for row in matrix_one_zero:
            self.matrix_lex.append([k + 1 for k, x in enumerate(row) if x == 1])

    def add_singlet_rv(self, singlet: int, representative_vector: RepresentativeVector):
        self.singlet_representative_vectors.insert(singlet, representative_vector)

    def add_rv(self, sigma: Subset, representative_vector: RepresentativeVector):
        self.representative_vectors[hash(sigma)] = representative_vector

    def get_rv(self, sigma: Subset) -> RepresentativeVector:
        size = sigma.get_size()
        if size > 1:
            return self.representative_vectors[hash(sigma)]
        elif size == 1:
            return self.singlet_representative_vectors[sigma.get_components()[0]]
        else:
            return self.singlet_representative_vectors[0]

    def get_singlet_rv(self, singlet: int) -> RepresentativeVector:
        return self.singlet_representative_vectors[singlet]
