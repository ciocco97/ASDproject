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


class MBase:

    def __init__(self):
        self.data = None
        self.output = None

    def main_procedure(self):
        self.output = []
        self.data = Data()
        data = self.data

        queue = SubsQueue()
        while queue.size() > 0:
            logging.info(f"\tQueue size: {queue.size()}")

            delta = queue.dequeue()
            rv1 = data.get_representative_vector(delta)

            logging.info(f"\tdelta: {delta} representative vector: {rv1}")
            logging.info(f"\tdelta_max: {delta.max()}")
            logging.info(f"\tdelta components: {delta.get_components()}, {delta.__hash__()}")

            for e in range(delta.max() + 1, data.get_domain_size()):
                logging.info(f"\t\t- e: {e} in {range(delta.max() + 1, data.get_domain_size())} -")

                t = Subset(delta.get_components())
                t.add(e)
                # optimization: we know it is a singlet so there is a data structure on purpose (an array) so we access it super ez pz lemon sqz
                rv2 = data.get_singlet_representative_vector(e)
                logging.info(f"\t\te: {e} representative vector: {rv2}")
                t_rv = generate_new_rv(rv1, rv2, data.N)
                logging.info(f"\t\tT: {t} representative vector: {t_rv}")
                data.add_representative_vector(t, t_rv)

                result = self.the_best_check_in_the_entire_world(t)
                logging.info(f"\t\tresult: {RESULT_TO_STRING[result]}")

                if result == OK:
                    queue.enqueue(t)
                elif result == MHS:
                    self.output.append(t)
                    logging.info(f"\t\tMinimal hitting set: {t}")

        print(*(x for x in self.output), sep='\n')

    def the_best_check_in_the_entire_world(self, t: Subset):
        t_rv: RepresentativeVector = self.data.get_representative_vector(t)
        p_c_sigma = set([])
        for ni in t.get_components():
            if ni in t_rv.get_values():
                p_c_sigma.add(ni)
        logging.info(f"\t\t\tp_c_sigma: {p_c_sigma}")
        return round(random.uniform(0, 1))
