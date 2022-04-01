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
        self.output = []

        self.start = None
        self.end = None

    def main_procedure(self, instance: ProblemInstance):

        queue = collections.deque()
        queue.append(Subset([]))
        N = instance.N
        M = instance.M
        self.start = time.time()
        while len(queue) > 0:

            delta = queue.popleft()
            rv1 = instance.get_rv(delta)

            for e in range(delta.max() + 1, M+1):
                # there's no need to generate a new Subset for each new e. We just use the previous delta to make the
                # computation. Only if the new delta is OK, we add a new Subset into the queue.
                delta.add(e)

                # optimization: we know it is a singlet so there is a data structure on purpose (an array) so we
                # access it super ez pz lemon sqz
                rv2 = instance.get_singlet_rv(e)
                t_rv = generate_new_rv(rv1, rv2, N)

                # optimization: we save the new RV iff the subset it represents is OK! not everytime
                result = check(delta, t_rv)
                if result == OK and e != M:
                    instance.add_rv(delta, t_rv)
                    queue.append(Subset(delta.get_components()))
                elif result == MHS:
                    # also in this case we generate the new Subset only if we need it (in this case, we need to append
                    # it onto the output. Otherwise, we use delta to save memory
                    self.output.append(Subset(delta.get_components()))
                delta.popright()

        self.end = time.time()
        max_size = min_size = 0
        if len(self.output):
            min_size = self.output[0].get_size()  # the first element is the smallest
            max_size = self.output[len(self.output) - 1].get_size()  # the last element is the biggest
        logging.info(f"Processing completed ({'{:e}'.format(self.end - self.start, 3)}s): {len(self.output)} MHS "
                     f"found")
        logging.info(f"Dimensions of the MHS: {max_size} max size, {min_size} min size")

    def print_output(self):
        print(*(x for x in self.output), sep='\n')

    def get_output(self) -> list:
        return self.output

    def log_output(self):
        output_str = "MHS found: "
        for x in self.output:
            output_str += str(x) + "|"
        logging.info(output_str[:-1])

    def get_elapsed(self) -> float:
        return self.end - self.start
