from data.data import Data
from subset import Subset
from subqueue import SubsQueue
from representative_vector import RepresentativeVector
import random

RESULT_TO_STRING = {-1: "KO", 1: "MHS", 0: "OK"}
KO = -1
MHS = 1
OK = 0
XVAL = -1
OUTPUT = []



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
    global data
    data = Data()
    # for symbol in data.get_domain():
    #     print(f"{data.get_representative_vector(symbol)}")

    queue = SubsQueue()
    while queue.size() > 0:
        print(f"\tQueue size: {queue.size()}")
        delta = queue.dequeue()

        print(f"\tdelta: {delta}")
        print(f"\tdelta_max: {delta.max()}")

        for e in range(delta.max() + 1, data.get_domain_size()):

            print(f"\t\tdelta components: {delta.get_components()}, {delta.__hash__()}")

            t = Subset(delta.get_components())

            print(f"\t\tnew delta: {t}")
            # ottimizzazione, il secondo sappiamo che è un singoletto quindi c'è una struttura dati apposta (un array) così ci accediamo super ez
            rv1 = data.get_representative_vector(t)
            rv2 = data.get_singlet_representative_vector(e)
            print(f"{t} - {rv1}")
            print(f"{e} - {rv2}")
            newrv = generate_new_rv(rv1, rv2)
            t.add(e)
            data.add_representative_vector(t, newrv)
            result = the_best_check_in_the_entire_world(t)
            print(f"\t\tresult: {RESULT_TO_STRING[result]}")

            if result == OK:
                queue.enqueue(t)
            elif result == MHS:
                OUTPUT.append(t)
                print(f"Minimal hitting set: {t}")

            print(f"\t\t- e: {e} in {range(delta.max() + 1, data.get_domain_size())} -")


def the_best_check_in_the_entire_world(t):
    rv = data.get_representative_vector(t)
    return round(random.uniform(0, 1))

#this procedure generate the new rv starting from a couple
def generate_new_rv(rv1: RepresentativeVector, rv2: RepresentativeVector) -> RepresentativeVector:
    new = RepresentativeVector(data.N)
    for i, phi1 in enumerate(rv1.get_values()):
        phi2 = rv2.get_values()[i]
        result = phi1 + phi2
        new.set_val_by_index(i, result if result <= max(phi1, phi2) else XVAL)
    return new
