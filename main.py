# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Bella quebec, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import logging

from mbase import MBase


def main():
    # For log record attributes visit https://docs.python.org/3/library/logging.html#logrecord-objects
    logging.basicConfig(filename='ASD.log', level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")
    logging.FileHandler('ASD.log', mode='w')

    for i in range(0, 23):
        print(f"{i}")
        mamma = MBase()
        mamma.main_procedure(4)


if __name__ == '__main__':
    main()
