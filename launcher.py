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


def plot_data(i_start: int, i_end: int, data1: list, data2: list):
    plt.title("Solving time")
    plt.xlabel("Problem n°")
    plt.ylabel("Seconds")
    plt.grid()
    x = range(i_start, i_end + 2)
    plt.plot(x, data1, label="preprocess")
    plt.plot(x, data2, label="no preprocess")
    plt.legend()
    plt.pause(0.5)


def performance_comparation():
    log_config()
    parser = Parser(["Benchmarks/benchmarks1/", "Benchmarks/benchmarks2/"])
    elapsed_performance = []
    elapsed_low_performance = []
    i_start = 20
    i_end = 30
    for i in range(i_start, i_end):
        matrix_one_zero = parser.parse_file_number_n(i)
        pre_process = PreProcess(copy.deepcopy(matrix_one_zero))
        new_matrix_one_zero = pre_process.main_procedure()
        instance_performance = ProblemInstance(new_matrix_one_zero)
        problem_solver = Solver()
        print(f" - Inizio elaborazione file {i} - ")

        problem_solver.main_procedure(instance_performance)

        print(f" - Fine elaborazione file {i} - \n")

        elapsed_performance.append(problem_solver.get_elapsed())

        print(f" - Inizio elaborazione file {i} (low performance) - ")
        instance_low_performance = ProblemInstance(matrix_one_zero)
        problem_solver.main_procedure(instance_low_performance)
        elapsed_low_performance.append(problem_solver.get_elapsed())
        print(f" - Fine elaborazione file {i} (low performance) - \n")

        plot_data(i_start, i_end, elapsed_performance, elapsed_low_performance)
