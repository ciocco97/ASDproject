from data_structure.representative_vector import RepresentativeVector
from data_structure.subset import Subset


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

        RepresentativeVector.X_VAL = -1 * (self.M + 1)
        # the representative vector of the empty subset is the null vector of size N
        rv_zero = RepresentativeVector(self.N)
        self.add_singlet_representative_vector(0, rv_zero)

        # computation of the representative vectors of the singletties :')
        for singlet in range(1, self.M + 1):
            current_repr_vector = RepresentativeVector(self.N)
            for i, N_i in enumerate(self.matrix_lex):
                if singlet in N_i:
                    current_repr_vector.set_val_by_index(i, singlet)
                    # here we put k+1 because the 0 is filled by the empty vector
            self.add_singlet_representative_vector(singlet, current_repr_vector)

    def set_M(self, M):
        self.M = M

    def set_N(self, N):
        self.N = N

    def set_matrix_lex(self, matrix_one_zero):
        for row in matrix_one_zero:
            self.matrix_lex.append([k + 1 for k, x in enumerate(row) if x == 1])

    def add_singlet_representative_vector(self, singlet: int, representative_vector: RepresentativeVector):
        self.singlet_representative_vectors.insert(singlet, representative_vector)

    def add_representative_vector(self, sigma: Subset, representative_vector: RepresentativeVector):
        self.representative_vectors[hash(sigma)] = representative_vector

    def get_representative_vector(self, sigma: Subset) -> RepresentativeVector:
        if sigma.get_size() == 1:
            return self.get_singlet_representative_vector(sigma.get_components()[0])
        return self.representative_vectors[sigma.__hash__()]

    def get_singlet_representative_vector(self, singlet: int) -> RepresentativeVector:
        return self.singlet_representative_vectors[singlet]
