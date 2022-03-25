import logging
import os


class MatrixParser:

    def __init__(self, path='Benchmarks/benchmarks1/'):
        self.path = path
        self.file_list = os.listdir(path)
        self.M = 0
        self.N = 0
        self.matrix_one_zero = []

    def parse_file_number_n(self, n=0):
        self.matrix_one_zero = []
        selected_file = self.file_list[n]
        logging.info("File selezionato per il parsing: " + selected_file)

        with open(self.path + selected_file) as file:
            for line in file:
                if not line.startswith(';;'):
                    row = []
                    for num in line.split(' '):
                        if not num == '-\n':
                            row.append(int(num))
                    self.matrix_one_zero.append(row)

        self.M = len(self.matrix_one_zero[0])
        self.N = len(self.matrix_one_zero)

        logging.info(
            f"Parsing completato: {self.M} elementi del dominio e {self.N} insiemi")

    def matrix_lexiconographic(self):
        sets = []
        for row in self.matrix_one_zero:
            sets.append([k + 1 for k, x in enumerate(row) if x == 1])
        return sets

    def get_file_names_in_path(self):
        return [x for x in self.file_list if x.endswith(".matrix")]

    def get_num_file_in_path(self):
        return len(self.get_file_names_in_path())

    def get_matrix_one_zero(self):
        return self.matrix_one_zero

    def get_M(self):
        return self.M

    def get_N(self):
        return self.N
