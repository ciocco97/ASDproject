import logging
import os
import time
import collections
from threading import Thread

import numpy
import psutil
from data_structure.problem_instance import ProblemInstance

RESULT_TO_STRING = {-1: "KO", 1: "MHS", 0: "OK"}
KO = -1
MHS = 1
OK = 0


def check(delta: [], values: []):
    for component in delta:
        if component not in values:
            return KO
    return OK if 0 in values else MHS


def generate_new_rv(rv1: tuple, rv2: tuple, X_VAL) -> []:
    values = list(rv1)
    i = 0
    for phi1, phi2 in zip(rv1, rv2):
        if phi2 and phi1 != X_VAL:
            result = phi1 + phi2
            values[i] = result if 0 <= result <= max(phi1, phi2) else X_VAL
        i += 1
    return values


class Solver:

    def __init__(self):
        self.output = collections.deque()

        self.start = None
        self.end = None

        self.start_memory = 0.0
        self.end_memory = 0.0

        self.running = True
        self.out_of_time = False
        self.time_limit = None

    def memory_fun(self):
        while self.running:
            process = psutil.Process(os.getpid())
            self.end_memory = process.memory_info().rss if process.memory_info().rss > self.end_memory else self.end_memory
            time.sleep(0.5)

    def timeout_fun(self):
        i = 0
        time_limit = self.time_limit * 2
        while i < time_limit and self.running:
            time.sleep(0.5)
            i += 1
        if self.running:
            self.running = False
            self.out_of_time = True

    def main_procedure(self, instance: ProblemInstance):

        queue = collections.deque()
        queue.append([])
        M = instance.M

        X_VAL = instance.X_VAL

        memory_thread = Thread(target=self.memory_fun)
        memory_thread.start()

        if self.time_limit:
            time_out_thread = Thread(target=self.timeout_fun)
            time_out_thread.start()

        self.start = time.time()
        self.start_memory = psutil.Process(os.getpid()).memory_info().rss

        while len(queue) > 0 and self.running:

            delta = queue.popleft()
            rv1 = instance.get_rv(delta)

            for e in range(max(delta) + 1 if len(delta) > 0 else 1, M + 1):
                # there's no need to generate a new Subset for each new e. We just use the previous delta to make the
                # computation. Only if the new delta is OK, we add a new Subset into the queue.
                delta.append(e)

                # optimization: we know it is a singlet so there is a data structure on purpose (an array) so we
                # access it super ez pz lemon sqz
                rv2 = instance.singlet_representative_vectors[e]
                values = generate_new_rv(rv1, rv2, X_VAL)

                # optimization: we save the new RV iff the subset it represents is OK! not everytime
                result = check(delta, values)
                if result == OK and e != M:
                    instance.add_rv(delta, tuple(values))
                    queue.append(delta.copy())
                elif result == MHS:
                    # also in this case we generate the new Subset only if we need it (in this case, we need to append
                    # it onto the output. Otherwise, we use delta to save memory
                    self.output.append(tuple(delta))
                delta.pop()

        self.end = time.time()
        self.running = False
        max_size = min_size = 0
        if len(self.output):
            min_size = len(self.output[0])  # the first element is the smallest
            max_size = len(self.output[-1])  # the last element is the biggest
        resocont = ""
        if self.out_of_time:
            resocont += f"Time limit exceeded. Process not terminated in "
        else:
            resocont += f"Processing completed "
        logging.info(resocont + f"in {'{:e}'.format(self.end - self.start, 3)}s: {len(self.output)} MHS found")
        logging.info(f"Dimensions of the MHS: {max_size} max size, {min_size} min size")
        logging.info(f"Memory usage for this run: {(self.end_memory - self.start_memory) / 10 ** 6}MB")

    def print_output(self):
        print(*(x for x in self.output), sep='\n')

    def get_output(self):
        return self.output

    def log_output(self):
        output_str = "MHS found: "
        for x in self.output:
            output_str += str(x) + "|"
        logging.info(output_str[:-1])

    def log_output_one_zero(self, M: int):
        logging.info("MHS found: ")
        indexes = range(0, M)
        new_sub_template = ['0'] * M
        for sub in self.output:
            new_sub = new_sub_template.copy()
            for e in sub:
                new_sub[e-1] = '1'
            logging.info(' '.join(new_sub) + " -")

    def get_elapsed(self) -> float:
        return self.end - self.start

    def set_time_limit(self, time_limit: int):
        self.time_limit = time_limit
