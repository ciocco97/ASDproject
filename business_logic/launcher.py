import copy
import logging
import time

from data_structure.problem_instance import ProblemInstance
from instance_parser import Parser
from business_logic.problem_solver import Solver
from business_logic.pre_process import PreProcess
from our_plotter import OurPlotter


def log_config():
    # For log record attributes visit https://docs.python.org/3/library/logging.html#logrecord-objects
    logging.basicConfig(filename='log/ASD.log', level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
    logging.FileHandler('log/ASD.log', mode='w')


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
        my_plotter = OurPlotter()

        i_start = 0
        i_end = self.parser.get_dir_size()
        for i in range(i_start, i_end):
            matrix = self.parser.parse_file_number_n(i)
            self.pre_process_mode = self.ALL
            time_1 = self.solve(copy.deepcopy(matrix))
            my_plotter.add_data("pre_process_time", time_1[0], OurPlotter.PRE_PROC_TIME)
            my_plotter.add_data("solver_performance", time_1[1], OurPlotter.SOLVER_TIME)

            self.pre_process_mode = self.ZERO
            time_2 = self.solve(copy.deepcopy(matrix))
            my_plotter.add_data("pre_process_time", time_2[0], OurPlotter.PRE_PROC_TIME)
            my_plotter.add_data("solver_low_performance", time_2[1], OurPlotter.SOLVER_TIME)
            my_plotter.plot_data_to_compare(OurPlotter.SOLVER_TIME, "solver_performance", "solver_low_performance")

    def solve_file_number(self, n: int):
        matrix = self.parser.parse_file_number_n(n)
        self.solve(matrix)

    def solve_file_name(self, file_name: str):
        matrix = self.parser.parse_file_named(file_name)
        self.solve(matrix)

    def solve_range(self, start, end):
        if end == -1:
            end = self.parser.get_dir_size()
        for k in range(start, end):
            self.solve_file_number(k)

    def solve(self, matrix):
        pre_proc_start = time.time()
        if self.pre_process_mode != Launcher.ZERO:
            pre_process = PreProcess(matrix)
            if self.pre_process_mode == Launcher.ALL:
                matrix = pre_process.full_pp()
            elif self.pre_process_mode == Launcher.COLUMN:
                matrix = pre_process.cols_pp()
            else:
                matrix = pre_process.rows_pp()
        pre_proc_elapsed = time.time() - pre_proc_start
        instance = ProblemInstance(matrix)
        problem_solver = Solver()
        solver_start = time.time()
        problem_solver.main_procedure(instance)
        solver_elapsed = time.time() - solver_start
        return pre_proc_elapsed, solver_elapsed

    def set_pre_process(self, mode: int):
        self.pre_process_mode = mode