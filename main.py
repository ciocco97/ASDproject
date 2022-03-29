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


def plot_data(i: int, data1: list, data2: list):
    plt.title("Solving time")
    plt.xlabel("Problem n°")
    plt.ylabel("Seconds")
    plt.grid()
    x = range(1, i + 2)
    plt.plot(x, data1, label="preprocess")
    plt.plot(x, data2, label="no preprocess")
    plt.legend()
    plt.pause(0.5)


def main():
    log_config()
    parser = Parser(["Benchmarks/benchmarks1/", "Benchmarks/benchmarks2/"])
    elapsed_performance = []
    elapsed_low_performance = []
    for i in range(0, 25):
        matrix_one_zero = parser.parse_file_number_n(i)
        pre_process = PreProcess(copy.deepcopy(matrix_one_zero))
        new_matrix_one_zero = pre_process.main_procedure()
        instance_performance = ProblemInstance(new_matrix_one_zero)
        problem_solver = Solver()
        print(f" - Inizio elaborazione file {i} - ")

        problem_solver.main_procedure(instance_performance)
        output_1 = pre_process.get_output(problem_solver.get_output())

        print(f" - Fine elaborazione file {i} - \n")

        elapsed_performance.append(problem_solver.get_elapsed())

        print(f" - Inizio elaborazione file {i} (low performance) - ")
        instance_low_performance = ProblemInstance(matrix_one_zero)
        problem_solver.main_procedure(instance_low_performance)
        elapsed_low_performance.append(problem_solver.get_elapsed())
        output_2 = problem_solver.get_output()
        print(f" - Fine elaborazione file {i} (low performance) - \n")

        for ind in range(0, len(output_1)):
            print(f"{output_1[ind]}\t{output_2[ind]}")
        plot_data(i, elapsed_performance, elapsed_low_performance)


if __name__ == '__main__':
    main()
