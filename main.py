# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Bella quebec, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import logging

from mbase import mbase


def main():
    logging.basicConfig(filename='ASD.log', encoding='utf-8', level=logging.DEBUG)
    mbase()


if __name__ == '__main__':
    main()
