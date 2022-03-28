import logging
import time

from data_structure.subset import Subset
from instance_parser import Parser
from problem_solver import Solver


def log_config():
    # For log record attributes visit https://docs.python.org/3/library/logging.html#logrecord-objects
    logging.basicConfig(filename='ASD.log', level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
    logging.FileHandler('ASD.log', mode='w')


def main():
    log_config()
    parser = Parser(["Benchmarks/benchmarks1/", "Benchmarks/benchmarks2/"])
    # for i in range(4, 5):
    i = 22
    instance = parser.get_problem_instance_n(i)
    problem_solver = Solver()
    print(f" - Inizio elaborazione file {i} - ")
    problem_solver.main_procedure(instance)
    problem_solver.print_output()

    # debug of the columns pp
    output = problem_solver.get_output()
    print("map debug")
    for sub in output:
        if isinstance(sub, Subset):
            newsub = Subset(instance.map(x) for x in sub.get_components())
            print(newsub)
    # end debug

    print(f" - Fine elaborazione file {i} - \n")
    time.sleep(1)


if __name__ == '__main__':
    main()
