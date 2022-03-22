from matrix_parser import MatrixParser
from subset import Subset


def mbase():
    matrix_parser = MatrixParser()
    matrix_parser.parse_file_number_n()
    matric_lexico = matrix_parser.matrix_lexiconographic()

    sub1 = Subset(matric_lexico[0])
    sub2 = Subset(matric_lexico[1])
    print(f"sub1: {sub1}")
    print(f"sub2: {sub2}")
    print(f"sub1 compare sub2: {sub1.compare(sub2)}")
    print(f"max sub2: {sub2.max()}")
