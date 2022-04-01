import time

from data_structure.subset import Subset
import logging


class PreProcess:

    def __init__(self, matrix_one_zero):
        self.matrix_one_zero = matrix_one_zero

        # this map will be used for the columns pre-processing. It's the maps of all the zeros in the matrix (the
        # positions of the components in the domain that are not in the sets.
        self.zeros = None

        self.num_del_rows = 0
        self.start = None
        self.end = None

    def full_pp(self) -> list:
        self.cols_pp()
        self.rows_pp()
        return self.matrix_one_zero

    def cols_pp(self) -> list:
        start = time.time()

        self.zeros = [0] * len(self.matrix_one_zero[0])
        for row in self.matrix_one_zero:
            for k, e in enumerate(row):
                if e == 1:
                    self.zeros[k] = 1
        indexes = sorted([i for i, z in enumerate(self.zeros) if z == 0], reverse=True)
        for row in self.matrix_one_zero:
            for index in indexes:
                del row[index]

        end = time.time()
        logging.info(
            f"Columns pre-process successfully completed with {len(self.zeros) - len(self.matrix_one_zero[0])}"
            f" removed columns in {end - start}s")
        return self.matrix_one_zero

    def rows_pp(self) -> list:
        start = time.time()

        def row_sum(r: list) -> int:
            return sum(r)

        self.matrix_one_zero.sort(key=row_sum)

        i = 0
        while i < len(self.matrix_one_zero):
            candidate = {x: None for x in range(i + 1, len(self.matrix_one_zero))}
            next_row = False
            for j, e in enumerate(self.matrix_one_zero[i]):
                if e == 1:
                    for c in {k: None for k in candidate}:
                        if self.matrix_one_zero[c][j] == 0:
                            del candidate[c]
                        if len(candidate) == 0:
                            next_row = True
                            break
                            # in questo caso non è rimasta neanche una riga che può contenere la corrente -> si può
                            # passare alla prossima riga.
                    if next_row:
                        break
            for c in sorted(candidate.keys(), reverse=True):
                del self.matrix_one_zero[c]
                self.num_del_rows += 1
            i += 1
        end = time.time()
        logging.info(
            f"Rows pre-process successfully completed with {self.num_del_rows} removed rows in {end - start}s")
        return self.matrix_one_zero

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

    def get_output(self, output) -> list:
        subsets = []
        for sub in output:
            if isinstance(sub, Subset):
                newsub = Subset(self.map(x) for x in sub.get_components())
                subsets.append(newsub)
        return subsets

    def log_output(self, output):
        output_str = "MHS found: "
        for sub in output:
            if isinstance(sub, Subset):
                newsub = Subset([self.map(x) for x in sub.get_components()])
                output_str += f"{newsub}|"
        logging.info(output_str[:-1])

    def get_elapsed(self) -> float:
        return self.end - self.start
