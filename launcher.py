import copy
import logging
import matplotlib.pyplot as plt

from data_structure.problem_instance import ProblemInstance
from instance_parser import Parser
from pre_process import PreProcess
from problem_solver import Solver


def log_config():
    # For log record attributes visit https://docs.python.org/3/library/logging.html#logrecord-objects
    logging.basicConfig(filename='ASD.log', level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
    logging.FileHandler('ASD.log', mode='w')


def plot_data_to_compare(i_start: int, i_end: int, data1: list, data2: list):
    fig, axs = plt.subplots(2)
    x = range(i_start, i_end + 1)

    axs[0].set_title("Solving time")
    # axs[0].xlabel("Problem n°")
    # axs[0].ylabel("Seconds")
    # axs[0].grid()
    axs[0].plot(x, data1, label="preprocess")
    axs[0].plot(x, data2, label="no preprocess")
    # axs[0].legend()

    # axs[1].title("Delta time")
    # axs[1].xlabel("Problem n°")
    # axs[1].ylabel("Seconds")
    # axs[1].grid()
    axs[1].plot(x, [data1[i] - data2[i] for i in x], label="difference")
    # axs[1].legend()

    plt.pause(0.5)


class Launcher:
    ZERO = 0
    ROW = 1
    COLUMN = 2
    ALL = 3

    def __init__(self):
        log_config()
        self.parser = Parser(["Benchmarks/benchmarks1/", "Benchmarks/benchmarks2/"])

        self.pre_process_mode = Launcher.ALL

    def performance_comparison(self):
        elapsed_performance = []
        elapsed_low_performance = []
        i_start = 0
        i_end = self.parser.num_file_in_paths
        for i in range(i_start, i_end):
            matrix = self.parser.parse_file_number_n(i)
            self.pre_process_mode = self.ALL
            self.solve(matrix)

            # elapsed_performance.append(problem_solver.get_elapsed())

            self.pre_process_mode = self.ZERO
            self.solve(matrix)
            # elapsed_low_performance.append(problem_solver.get_elapsed())

            # plot_data_to_compare(i_start, i, elapsed_performance, elapsed_low_performance)

    def solve_file_number(self, n: int):
        matrix = self.parser.parse_file_number_n(n)
        self.solve(matrix)

    def solve_file_name(self, file_name: str):
        matrix = self.parser.parse_file_named(file_name)
        self.solve(matrix)

    def solve_range(self, start, end):
        for k in range(start, end):
            self.solve_file_number(k)

    def solve(self, matrix):
        if self.pre_process_mode != Launcher.ZERO:
            pre_process = PreProcess(matrix)
            if self.pre_process_mode == Launcher.ALL:
                matrix = pre_process.full_pp()
            elif self.pre_process_mode == Launcher.COLUMN:
                matrix = pre_process.cols_pp()
            else:
                matrix = pre_process.rows_pp()
        instance = ProblemInstance(matrix)
        problem_solver = Solver()
        problem_solver.main_procedure(instance)

    def set_pre_process(self, mode: int):
        self.pre_process_mode = mode
