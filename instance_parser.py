import logging
import os


class Parser:

    def __init__(self, paths: list):
        self.file_list = []
        for path in paths:
            self.file_list += [path + x for x in os.listdir(path) if x.endswith(".matrix")]
        self.dir_size = len(self.file_list)

    def parse_file_number_n(self, n: int) -> list:
        matrix_one_zero = []
        selected_file = self.file_list[n]
        logging.info("Selected file for parsing: " + selected_file)
        with open(selected_file) as file:
            for line in file:
                if not line.startswith(';;'):
                    row = []
                    for num in line.split(' '):
                        if num != '-\n':
                            row.append(int(num))
                    matrix_one_zero.append(row)
        logging.info(
            f"Parsing complete: {len(matrix_one_zero[0])} domain elements and {len(matrix_one_zero)} subsets")
        return matrix_one_zero

    def parse_file_named(self, file_name: str) -> list:
        for index, file in enumerate(self.file_list):
            if file.endswith(file_name):
                return self.parse_file_number_n(index)

    def parse_file_by_path(self, path) -> list:
        self.file_list = [path]
        return self.parse_file_number_n(0)

    def get_dir_size(self) -> int:
        return self.dir_size

    def get_file_name_by_index(self, index):
        return self.file_list[index]
