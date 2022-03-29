import logging
import os


class Parser:

    def __init__(self, paths: list):
        self.file_list = []
        for path in paths:
            self.file_list += [path + x for x in os.listdir(path) if x.endswith(".matrix")]
        self.num_file_in_paths = len(self.file_list)

    def parse_file_number_n(self, n: int) -> list:
        matrix_one_zero = []
        selected_file = self.file_list[n]
        logging.info("File selezionato per il parsing: " + selected_file)
        with open(selected_file) as file:
            for line in file:
                if not line.startswith(';;'):
                    row = []
                    for num in line.split(' '):
                        if not num == '-\n':
                            row.append(int(num))
                    matrix_one_zero.append(row)
        logging.info(
            f"Parsing completato: {len(matrix_one_zero[0])} elementi del dominio e {len(matrix_one_zero)} insiemi")
        return matrix_one_zero