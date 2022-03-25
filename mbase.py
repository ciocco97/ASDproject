import logging

from data.data import Data
from subset import Subset
from subqueue import SubsQueue
from representative_vector import RepresentativeVector
from representative_vector import generate_new_rv
import random

RESULT_TO_STRING = {-1: "KO", 1: "MHS", 0: "OK"}
KO = -1
MHS = 1
OK = 0


def the_best_check_in_the_entire_world(t: Subset, t_rv: RepresentativeVector):

    for component in t.get_components():
        if component not in t_rv.get_values():
            return KO
    return OK if 0 in t_rv.get_values() else MHS


class MBase:

    def __init__(self, path: str):
        self.data = Data(path)
        self.output = None

    def main_procedure(self, file_number: int):
        self.output = []
        self.data.setup_data_for_file_n(file_number)
        data = self.data

        queue = SubsQueue()
        while queue.size() > 0:
            logging.debug(f"\tQueue size: {queue.size()}")

            delta = queue.dequeue()
            rv1 = data.get_representative_vector(delta)

            logging.debug(f"\tdelta: {delta} representative vector: {rv1}")
            logging.debug(f"\tdelta_max: {delta.max()}")
            logging.debug(f"\tdelta components: {delta.get_components()}, {delta.__hash__()}")

            for e in range(delta.max() + 1, data.M + 1):
                logging.debug(f"\t\t- e: {e} in {range(delta.max() + 1, data.get_domain_size())} -")

                t = Subset(delta.get_components())
                t.add(e)
                # optimization: we know it is a singlet so there is a data structure on purpose (an array) so we access it super ez pz lemon sqz
                rv2 = data.get_singlet_representative_vector(e)
                logging.debug(f"\t\te: {e} representative vector: {rv2}")
                t_rv = generate_new_rv(rv1, rv2, data.N)
                logging.debug(f"\t\tT: {t} representative vector: {t_rv}")
                data.add_representative_vector(t, t_rv)

                result = the_best_check_in_the_entire_world(t, t_rv)
                logging.debug(f"\t\tresult: {RESULT_TO_STRING[result]}")

                if result == OK:
                    queue.enqueue(t)
                elif result == MHS:
                    self.output.append(t)
                    logging.debug(f"\t\tMinimal hitting set: {t}")

        self.output.reverse()
        print(*(x for x in self.output), sep='\n')
        print("Fine")

    def get_num_file_in_path(self):
        return self.data.get_num_file_in_path()

