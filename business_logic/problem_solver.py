import logging
import time
import collections

from data_structure.problem_instance import ProblemInstance
from data_structure.representative_vector import generate_new_rv, RepresentativeVector
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

        self.output = collections.deque()

        queue = collections.deque()
        queue.append(Subset([0]))
        while len(queue) > 0:

            delta = queue.popleft()
            rv1 = instance.get_rv(delta)

            for e in range(delta.max() + 1, instance.M + 1):
                # there's no need to generate a new Subset for each new e. We just use the previous delta to make the
                # computation. Only if the new delta is OK, we add a new Subset into the queue.
                delta.add(e)

                # optimization: we know it is a singlet so there is a data structure on purpose (an array) so we
                # access it super ez pz lemon sqz
                rv2 = instance.get_singlet_rv(e)
                t_rv = generate_new_rv(rv1, rv2, instance.N)

                # optimization: we save the new RV iff the subset it represents is OK! not everytime
                result = check(delta, t_rv)
                if result == OK:
                    instance.add_rv(delta, t_rv)
                    queue.append(Subset(delta.get_components()))
                elif result == MHS:
                    # also in this case we generate the new Subset only if we need it (in this case, we need to append
                    # it onto the output. Otherwise, we use delta to save memory
                    self.output.append(Subset(delta.get_components()))
                delta.pop_right()

        self.end = time.time()
        self.max = len(self.output[len(self.output)-1].get_components())
        self.min = len(self.output[0].get_components())
        logging.info(f"Processing completed ({'{:e}'.format(self.end - self.start, 3)}s): {len(self.output)} MHS "
                     f"found")
        logging.info(f"dimensions of the MHS: {self.max} max size, {self.min} min size")

    def print_output(self):
        print(*(x for x in self.output), sep='\n')

    def get_output(self) -> list:
        return self.output

    def log_output(self):
        for x in self.output:
            logging.info(str(x))

    def get_elapsed(self) -> float:
        return self.end - self.start


