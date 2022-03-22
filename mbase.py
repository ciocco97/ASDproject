from matrix_parser import MatrixParser
from subset import Subset
from subqueue import SubsQueue
import random

RESULT_TO_STRING = {-1: "KO", 1: "MHS", 0: "OK"}
KO = -1
MHS = 1
OK = 0


def mbase():
    # matrix_parser = MatrixParser()
    # matrix_parser.parse_file_number_n()
    # matric_lexico = matrix_parser.matrix_lexiconographic()

    # sub1 = Subset(matric_lexico[0])
    # sub2 = Subset(matric_lexico[1])
    # print(f"sub1: {sub1}")
    # print(f"sub2: {sub2}")
    # print(f"sub1 compare sub2: {sub1.compare(sub2)}")
    # print(f"max sub2: {sub2.max()}")

    print(
        "inizio procedura quella vera eh, mica le prove\n\n---INIZIO VERO---\n\n--DA ADESSO IN POI--\n\n"
    )
    main_procedure()


def main_procedure():
    matrix_parser = MatrixParser()
    matrix_parser.parse_file_number_n()

    queue = SubsQueue()
    while queue.size() > 0:
        delta = queue.dequeue()
        
        print(f"delta: {delta}")
        print(f"delta_max: {delta.max()}")
        
        for e in range(delta.max() + 1, matrix_parser.get_domain_size()):
            
            print(f"delta components: {delta.get_components()}")
            
            T = Subset(delta.get_components())
            T.add(e)
            
            print(f"new delta: {T}")
            
            result = the_best_check_in_the_entire_world(T)
            
            print(f"result: {RESULT_TO_STRING[result]}")
            
            if result == OK:
                queue.enqueue(T)
            elif result == MHS:
                print(f"Minimal hitting set: {T}")


def the_best_check_in_the_entire_world(T):
    return round(random.uniform(-1, 1))
