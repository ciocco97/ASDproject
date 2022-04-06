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
        # logging.info(f"List of Subsets: {self.matrix_lex}")

        self.X_VAL = -1 * (self.M + 1)
        # the representative vector of the empty subset is the null vector of size N
        singlet_rvs = [[0] * self.N]
        self.add_rv([], tuple([0] * self.N))
        # computation of the representative vectors of the singletties :')
        for singlet in range(1, self.M + 1):
            values = [0] * self.N
            for i, N_i in enumerate(self.matrix_lex):
                values[i] = singlet if singlet in N_i else 0
            singlet_rvs.append(values)
            self.add_rv([singlet], tuple(values))
        self.singlet_representative_vectors = tuple(singlet_rvs)

    def set_M(self, M):
        self.M = M

    def set_N(self, N):
        self.N = N

    def set_matrix_lex(self, matrix_one_zero):
        for row in matrix_one_zero:
            self.matrix_lex.append([k + 1 for k, x in enumerate(row) if x == 1])

    def add_singlet_rv(self, singlet: int, representative_vector: tuple):
        self.singlet_representative_vectors.insert(singlet, representative_vector)

    def add_rv(self, sigma: [], representative_vector: tuple):
        self.representative_vectors[str(sigma)] = representative_vector

    def get_rv(self, sigma):
        return self.representative_vectors[str(sigma)]
