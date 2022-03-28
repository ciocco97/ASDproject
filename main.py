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


def plot_data(i: int, data: list):
    plt.title("Solving time")
    plt.xlabel("Problem n°")
    plt.ylabel("Seconds")
    plt.grid()
    plt.plot(range(1, i + 2), data, 'r')
    plt.pause(0.5)


def main():
    log_config()
    parser = Parser(["Benchmarks/benchmarks1/", "Benchmarks/benchmarks2/"])
    elapsed = []
    for i in range(0, parser.num_file_in_paths):
        matrix_one_zero = parser.parse_file_number_n(i)
        pre_process = PreProcess(matrix_one_zero)
        new_matrix_one_zero = pre_process.main_procedure()
        instance = ProblemInstance(new_matrix_one_zero)
        problem_solver = Solver()
        print(f" - Inizio elaborazione file {i} - ")

        problem_solver.main_procedure(instance)
        problem_solver.print_output()
        pre_process

        print(f" - Fine elaborazione file {i} - \n")
        elapsed.append(problem_solver.get_elapsed())
        plot_data(i, elapsed)


if __name__ == '__main__':
    main()
