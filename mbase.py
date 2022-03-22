from matrix_parser import MatrixParser
from subset import Subset
from subqueue import SubsQueue


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


    print("inizio procedura quella vera eh, mica le prove\n\n---INIZIO VERO---\n\n--DA ADESSO IN POI--\n\n")
    main_procedure()

def main_procedure():
    matrix_parser = MatrixParser()
    matrix_parser.parse_file_number_n()

    queue = SubsQueue()
    while queue.mamma() > 0:
        delta = queue.dequeue()
        for e in range(delta.max() + 1, matrix_parser.get_domain_size()):
            print(f"delta:{delta}")
            T = Subset(delta, e)
            result = the_best_check_in_the_entire_world(T)
            print(f"new delta: {T}")
    

def the_best_check_in_the_entire_world(T):
    print("mamma")