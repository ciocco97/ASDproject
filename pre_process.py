import logging
import time

from data_structure.subset import Subset


class PreProcess:

    def __init__(self, matrix_one_zero):
        self.matrix_one_zero = matrix_one_zero

        # this map will be used for the columns pre-processing. It's the maps of all the zeros in the matrix (the
        # positions of the components in the domain that are not in the sets.
        self.zeros = None

        self.start = None
        self.end = None

    def main_procedure(self):
        self.start = time.time()
        self.cols_pp()
        self.end = time.time()
        logging.info(f"Preprocessing completato: {len(self.zeros)} colonne rimosse")
        return self.matrix_one_zero

    def cols_pp(self):
        self.zeros = [0] * len(self.matrix_one_zero[0])
        for row in self.matrix_one_zero:
            for k, e in enumerate(row):
                if e == 1:
                    self.zeros[k] = 1

        indexes = sorted([i for i, z in enumerate(self.zeros) if z == 0], reverse=True)
        for row in self.matrix_one_zero:
            for index in indexes:
                del row[index]

        # for row in self.matrix_one_zero:
        #     remove_index = 0
        #     for k in range(0, len(self.zeros)):
        #         if self.zeros[k] == 0:
        #             row.pop(remove_index)
        #         else:
        #             remove_index += 1

    def rows_pp(self):
        def row_sum(r: list) -> int:
            return sum(r)

        self.matrix_one_zero.sort(key=row_sum)
        for i, row in enumerate(self.matrix_one_zero):
            candidate = {x: None for x in range(i + 1, len(self.matrix_one_zero))}
            for j, e in enumerate(row):
                if e == 1:
                    for k in candidate:
                        if self.matrix_one_zero[k][j] == 0:
                            del candidate[k]
                        if len(candidate) == 0:
                            print("mamma")
                            # in questo caso non è rimasta neanche una riga che può contenere la corrente -> si può
                            # passare alla prossima riga.
            # Quando questo for è concluso, utte le righe con indice candidate possono essere eliminate

    # this method uses the zeros map to obtain the index of a component in the restricted domain, in the original one.
    # this method looks for the index-th 1 in the zeros map. so if the index is 0, it look for the first 1 in the map,
    # and returns its position
    def map(self, index):
        count = 0
        for i, e in enumerate(self.zeros):
            count += e
            if count == index:
                return i + 1

    def print_output(self, output):
        for sub in output:
            if isinstance(sub, Subset):
                newsub = Subset(self.map(x) for x in sub.get_components())
                print(newsub)

    def get_elapsed(self):
        return self.end - self.start
