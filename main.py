import logging
import time

from instance_parser import Parser
from data_structure.problem_instance import ProblemInstance
from problem_solver import Solver


def log_config():
    # For log record attributes visit https://docs.python.org/3/library/logging.html#logrecord-objects
    logging.basicConfig(filename='ASD.log', level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
    logging.FileHandler('ASD.log', mode='w')


def main():
    log_config()
    parser = Parser(["Benchmarks/benchmarks1/", "Benchmarks/benchmarks2/"])
    instance = parser.get_problem_instance_n(5)
    print(instance.map(3))
        # problem_solver = Solver()
        # print(f" - Inizio elaborazione file {i} - ")
        # problem_solver.main_procedure(instance)
        # problem_solver.print_output()
        # print(f" - Fine elaborazione file {i} - \n")
        # time.sleep(1)


if __name__ == '__main__':
    main()
