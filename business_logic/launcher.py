import copy
import logging
import os
import time
import shutil

from data_structure.problem_instance import ProblemInstance
from instance_parser import Parser
from business_logic.problem_solver import Solver
from business_logic.pre_process import PreProcess
from our_plotter import OurPlotter

log_path = 'ASD.log'


def log_config():
    # For log record attributes visit https://docs.python.org/3/library/logging.html#logrecord-objects
    log_format = "%(asctime)s: %(levelname)s: %(message)s"
    logging.basicConfig(filename=log_path, level=logging.INFO, format="")
    logging.FileHandler(log_path, mode='w+')


def reset_log():
    with open(log_path, 'w'):
        pass


def save_log(file_name: str):
    original = os.path.abspath(log_path)
    target = file_name.split('/')
    result_file_name = target[-1]
    target[-1] = "results"
    target_folder = os.path.abspath('/'.join(target))
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    target.append(result_file_name)
    target = os.path.abspath('/'.join(target))
    shutil.copyfile(original, target)
    reset_log()


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
        try:
            for i in range(i_start, i_end):
                file_name = self.parser.get_file_name_by_index(i)
                matrix = self.parser.parse_file_number_n(i)
                self.pre_process_mode = self.ALL
                result_1 = self.solve(copy.deepcopy(matrix), file_name, False)
                my_plotter.add_data("pre_process_time", result_1[0], OurPlotter.PRE_PROC_TIME)
                my_plotter.add_data("solver_performance", result_1[1], OurPlotter.SOLVER_TIME)

                self.pre_process_mode = self.ZERO
                result_2 = self.solve(copy.deepcopy(matrix), file_name)
                my_plotter.add_data("pre_process_time", result_2[0], OurPlotter.PRE_PROC_TIME)
                my_plotter.add_data("solver_low_performance", result_2[1], OurPlotter.SOLVER_TIME)
        except KeyboardInterrupt:
            my_plotter.plot_data_to_compare(OurPlotter.SOLVER_TIME, "solver_performance", "solver_low_performance")

    def solve_file_number(self, n: int):
        matrix = self.parser.parse_file_number_n(n)
        self.solve(matrix, self.parser.get_file_name_by_index(n))

    def solve_file_name(self, file_name: str):
        matrix = self.parser.parse_file_named(file_name)
        self.solve(matrix, file_name)

    def solve_range(self, start, end):
        if end == -1:
            end = self.parser.get_dir_size()
        for k in range(start, end):
            self.solve_file_number(k)

    def solve(self, matrix: list, file_name: str, save_result=True):
        print(f"Process file {file_name}, {self.pre_process_mode}")
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

        if self.pre_process_mode == Launcher.ALL or self.pre_process_mode == Launcher.COLUMN:
            pre_process.log_output(problem_solver.get_output())
        else:
            problem_solver.log_output()
        if save_result:
            save_log(file_name)
        return pre_proc_elapsed, solver_elapsed

    def set_pre_process(self, mode: int):
        self.pre_process_mode = mode
