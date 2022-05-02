class ProblemInstance:

    def __init__(self, matrix_one_zero):
        self.M = 0
        self.N = 0

        self.X_VAL = -1

        self.matrix_lex = []
        self.singlet_representative_vectors = None
        self.representative_vectors = dict()

        self.conf(matrix_one_zero)

    def conf(self, matrix_one_zero):

        self.N = len(matrix_one_zero)
        self.M = len(matrix_one_zero[0])

        self.set_matrix_lex(matrix_one_zero)

        self.X_VAL = -1 * (self.M + 1)
        # this will be the temporary list we store the rvs values in, and the first rv is the empty rv
        singlet_rvs = [tuple([0] * self.N)]
        # and we add the same empry rv in the dictionary
        self.add_rv([], tuple([0] * self.N))
        # computation of the representative vectors of the singletties :')
        for singlet in range(1, self.M + 1):
            values = [0] * self.N
            for i, N_i in enumerate(self.matrix_lex):
                values[i] = singlet if singlet in N_i else 0
            rv = tuple(values)
            singlet_rvs.append(rv)
            self.add_rv([singlet], rv)
        self.singlet_representative_vectors = tuple(singlet_rvs)

    def set_matrix_lex(self, matrix_one_zero):
        for row in matrix_one_zero:
            self.matrix_lex.append([k + 1 for k, x in enumerate(row) if x == 1])

    def add_singlet_rv(self, singlet: int, representative_vector: tuple):
        self.singlet_representative_vectors.insert(singlet, representative_vector)

    def add_rv(self, sigma: [], representative_vector: tuple):
        self.representative_vectors[str(sigma)] = representative_vector

    def get_rv(self, sigma):
        return self.representative_vectors[str(sigma)]
