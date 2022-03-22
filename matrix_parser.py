import os
import re


class MatrixParser:

    def __init__(self, path='Benchmarks/benchmarks1/'):

        self.dictionary = {}

        self.domain = []
        self.matrix_one_zero = []

        self.path = path
        self.file_list = os.listdir(path)

    def parse_file_number_n(self, n=0):
        self.dictionary = {}
        self.matrix_one_zero = []
        selected_file = self.file_list[n]
        with open(self.path + selected_file) as file:
            for line in file:
                if not line.startswith(';;'):
                    row = []
                    for num in line.split(' '):
                        if not num == '-\n':
                            row.append(int(num))
                    self.matrix_one_zero.append(row)
                else:
                    tonio = line.split()
                    if tonio[1] == "Map":
                        del tonio[:2]
                        # tonio = tonio[2:len(tonio)]
                        for num_element in tonio:
                            element = re.findall(r'\(.*?\)', num_element)[0]
                            num = int(num_element.replace(element, ""))
                            element = element[1:-1]
                            self.dictionary[num] = element
                            self.domain.append(num)

    def matrix_domain(self):
        # return [x if x not in self.dictionary else self.dictionary[k + 1] for y in self.matrix for k, x in enumerate(y)]
        # return [self.dictionary[k + 1] for y in self.matrix for k, x in enumerate(y) if x != 0]
        sets = []
        for row in self.matrix_one_zero:
            # sets.append([self.dictionary[k + 1] for k, x in enumerate(row) if x != 0])
            sets.append([x if x not in self.dictionary else self.dictionary[k + 1] for k, x in enumerate(row)])
        return sets

    def matrix_lexiconographic(self):
        sets = []
        for row in self.matrix_one_zero:
            sets.append([self.domain[k] for k, x in enumerate(row) if x != 0])
        return sets

    def list_files_in_path(self):
        for x in os.listdir(self.path):
            if x.endswith(".matrix"):
                print(x)

    def get_matrix_one_zero(self):
        return self.matrix_one_zero

    def get_dictionary(self):
        return self.dictionary

    def get_domain(self):
        return self.domain
