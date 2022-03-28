import logging
import time

from data_structure.problem_instance import ProblemInstance
from data_structure.representative_vector import generate_new_rv, RepresentativeVector
from data_structure.subqueue import SubsQueue
from data_structure.subset import Subset

RESULT_TO_STRING = {-1: "KO", 1: "MHS", 0: "OK"}
KO = -1
MHS = 1
OK = 0


def the_best_check_in_the_entire_world(t: Subset, t_rv: RepresentativeVector):
    for component in t.get_components():
        if component not in t_rv.get_values():
            return KO
    return OK if 0 in t_rv.get_values() else MHS


class Solver:

    def __init__(self):
        self.output = None

        self.start = None
        self.end = None

    def main_procedure(self, instance: ProblemInstance):

        self.start = time.time()

        self.output = []

        queue = SubsQueue()
        while queue.size() > 0:
            logging.debug(f"\tQueue size: {queue.size()}")

            delta = queue.dequeue()
            rv1 = instance.get_rv(delta)

            logging.debug(f"\tdelta: {delta} representative vector: {rv1}")
            logging.debug(f"\tdelta_max: {delta.max()}")
            logging.debug(f"\tdelta components: {delta.get_components()}, {hash(delta)}")

            for e in range(delta.max() + 1, instance.M + 1):
                logging.debug(f"\t\t- e: {e} in {range(delta.max() + 1, instance.M)} -")

                t = Subset(delta.get_components())
                t.add(e)
                # optimization: we know it is a singlet so there is a data structure on purpose (an array) so we
                # access it super ez pz lemon sqz
                rv2 = instance.get_singlet_rv(e)
                logging.debug(f"\t\te: {e} representative vector: {rv2}")
                t_rv = generate_new_rv(rv1, rv2, instance.N)
                logging.debug(f"\t\tT: {t} representative vector: {t_rv}")
                instance.add_rv(t, t_rv)

                result = the_best_check_in_the_entire_world(t, t_rv)
                logging.debug(f"\t\tresult: {RESULT_TO_STRING[result]}")

                if result == OK:
                    queue.enqueue(t)
                elif result == MHS:
                    self.output.append(t)
                    logging.debug(f"\t\tMinimal hitting set: {t}")

        self.end = time.time()
        logging.info(f"Processing completato: {len(self.output)} MHS trovati")
        self.output.reverse()

    def print_output(self):
        print(*(x for x in self.output), sep='\n')

    def get_output(self):
        return self.output

    def get_elapsed(self):
        return self.end - self.start
