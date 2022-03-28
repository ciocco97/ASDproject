from data_structure.representative_vector import RepresentativeVector
from data_structure.subset import Subset


class ProblemInstance:

    def __init__(self, matrix_one_zero):
        self.M = 0
        self.N = 0

        # this map will be used for the columns pre-processing. It's the maps of all the zeros in the matrix (the
        # positions of the components in the domain that are not in the sets.
        self.zeros = None

        self.matrix_lex = []
        self.singlet_representative_vectors = []
        self.representative_vectors = {}

        # here starts the pre-processing
        self.cols_pp(matrix_one_zero)

        self.conf(matrix_one_zero)

    def conf(self, matrix_one_zero):

        self.N = len(matrix_one_zero)
        self.M = len(matrix_one_zero[0])

        self.set_matrix_lex(matrix_one_zero)

        RepresentativeVector.X_VAL = -1 * (self.M + 1)
        # the representative vector of the empty subset is the null vector of size N
        rv_zero = RepresentativeVector(self.N)
        self.add_singlet_rv(0, rv_zero)

        # computation of the representative vectors of the singletties :')
        for singlet in range(1, self.M + 1):
            current_repr_vector = RepresentativeVector(self.N)
            for i, N_i in enumerate(self.matrix_lex):
                if singlet in N_i:
                    current_repr_vector.set_val_by_index(i, singlet)
                    # here we put k+1 because the 0 is filled by the empty vector
            self.add_singlet_rv(singlet, current_repr_vector)

    def cols_pp(self, matrix_one_zero):
        print(matrix_one_zero)
        self.zeros = [0] * len(matrix_one_zero[0])
        for row in matrix_one_zero:
            for i, ni in enumerate(row):
                if ni == 1:
                    self.zeros[i] = 1
        for row in matrix_one_zero:
            remove_index = 0
            for i in range(0, len(self.zeros)):
                if self.zeros[i] == 0:
                    row.pop(remove_index)
                else:
                    remove_index += 1
        print(matrix_one_zero)
        print(self.zeros)
        return matrix_one_zero

    # this method uses the zeros map to obtain the index of a component in the restricted domain, in the original one.
    # this method looks for the index-th 1 in the zeros map. so if the index is 0, it look for the first 1 in the map,
    # and returns its position
    def map(self, index):
        count = 0
        for i, e in enumerate(self.zeros):
            count += e
            if count == index:
                return i+1

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
        if sigma.get_size() == 1:
            return self.get_singlet_rv(sigma.get_components()[0])
        return self.representative_vectors[hash(sigma)]

    def remove_rv(self, sigma: Subset):
        self.representative_vectors.pop(sigma)

    def get_singlet_rv(self, singlet: int) -> RepresentativeVector:
        return self.singlet_representative_vectors[singlet]
