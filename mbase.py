import logging

from data.data import Data
from subset import Subset
from subqueue import SubsQueue
from representative_vector import RepresentativeVector
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

            logging.info(f"\tdelta: {delta}")
            logging.info(f"\tdelta_max: {delta.max()}")
            logging.info(f"\tdelta components: {delta.get_components()}, {delta.__hash__()}")

            for e in range(delta.max() + 1, data.get_domain_size()):

                t = Subset(delta.get_components())

                logging.info(f"\t\tnew delta: {t}")
                # optimization: the second we know it is a singlet so there is a data structure on purpose (an array) so we access it super ez pz lemon sqz
                rv1 = data.get_representative_vector(t)
                rv2 = data.get_singlet_representative_vector(e)
                logging.info(f"\t\t{t} - {rv1}")
                logging.info(f"\t\t{e} - {rv2}")
                new_rv = self.generate_new_rv(rv1, rv2)
                t.add(e)
                data.add_representative_vector(t, new_rv)
                result = self.the_best_check_in_the_entire_world(t)
                logging.info(f"\t\tresult: {RESULT_TO_STRING[result]}")

                if result == OK:
                    queue.enqueue(t)
                elif result == MHS:
                    self.output.append(t)
                    logging.info(f"\t\tMinimal hitting set: {t}")

                logging.info(f"\t\t- e: {e} in {range(delta.max() + 1, data.get_domain_size())} -")

        print(*(x for x in self.output), sep='\n')

    # this procedure generate the new rv starting from a couple
    def generate_new_rv(self, rv1: RepresentativeVector, rv2: RepresentativeVector) -> RepresentativeVector:
        new = RepresentativeVector(self.data.N)
        for i, phi1 in enumerate(rv1.get_values()):
            phi2 = rv2.get_values()[i]
            result = phi1 + phi2
            new.set_val_by_index(i, result if result <= max(phi1, phi2) else RepresentativeVector.X_VAL)
        return new

    def the_best_check_in_the_entire_world(self, t):
        rv = self.data.get_representative_vector(t)
        return round(random.uniform(0, 1))
