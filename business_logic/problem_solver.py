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


def check(t: Subset, t_rv: RepresentativeVector):
    for component in t.get_components():
        if component not in t_rv.get_values():
            return KO
    return OK if 0 in t_rv.get_values() else MHS


class Solver:

    def __init__(self):
        self.output = None

        self.start = None
        self.end = None

        self.max = None
        self.min = None

    def main_procedure(self, instance: ProblemInstance):

        self.start = time.time()

        self.output = []

        queue = SubsQueue()
        while queue.get_size() > 0:

            delta = queue.dequeue()
            rv1 = instance.get_rv(delta)

            for e in range(delta.max() + 1, instance.M + 1):
                # there's no need to generare a new Subset for each new e. We just use the previous delta to make the
                # computation. Only if the new delta is OK, we add a new Subset into the queue.
                t = Subset(delta.get_components())
                t.add(e)

                # optimization: we know it is a singlet so there is a data structure on purpose (an array) so we
                # access it super ez pz lemon sqz
                rv2 = instance.get_singlet_rv(e)
                logging.debug(f"\t\te: {e} representative vector: {rv2}")
                t_rv = generate_new_rv(rv1, rv2, instance.N)

                # optimization: we save the new RV iff the subset it represents is OK! not everytime
                result = check(t, t_rv)
                if result == OK:
                    instance.add_rv(t, t_rv)
                    queue.enqueue(Subset(t.get_components()))
                elif result == MHS:
                    self.output.append(t)

        self.end = time.time()
        self.max = max(len(x.get_components()) for x in self.output)
        self.min = min(len(x.get_components()) for x in self.output)
        logging.info(f"Processing completato ({'{:e}'.format(self.end - self.start, 3)}s): {len(self.output)} MHS "
                     f"trovati")
        logging.info(f"Dimensioni MHS: {self.max} dimensione massima, {self.min} dimensione minima")

    def print_output(self):
        print(*(x for x in self.output), sep='\n')

    def get_output(self) -> list:
        return self.output

    def log_output(self):
        for x in self.output:
            logging.info(str(x))

    def get_elapsed(self) -> float:
        return self.end - self.start


