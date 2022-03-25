import logging
import os
import re


class MatrixParser:

    def __init__(self, path='Benchmarks/benchmarks1/'):

        self.M = 0
        self.N = 0

        self.matrix_one_zero = []

        self.path = path
        self.file_list = os.listdir(path)

    def parse_file_number_n(self, n=0):
        self.matrix_one_zero = []
        selected_file = self.file_list[n]
        logging.debug("File selezionato per il parsing: " + selected_file)

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

        logging.debug(
            f"Parsing completato: {self.M} elementi del dominio e {self.N} insiemi")

    def matrix_lexiconographic(self):
        sets = []
        for row in self.matrix_one_zero:
            sets.append([k + 1 for k, x in enumerate(row) if x == 1])
        return sets

    def list_files_in_path(self):
        for x in os.listdir(self.path):
            if x.endswith(".matrix"):
                print(x)

    def get_file_names_in_path(self):
        return len([x for x in os.listdir(self.path) if x.endswith(".matrix")])

    def get_matrix_one_zero(self):
        return self.matrix_one_zero

    def get_M(self):
        return self.M

    def get_N(self):
        return self.N
