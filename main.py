import os
from os import system, name

import launcher
from launcher import *


def main():
    choice = input(main_menu())
    if int(choice) == 1:
        performance_comparison()


def main_menu():
    i = 0
    return "---Welcome to Eils MHS resolver v 1.47---\n" \
           "Please, select an option from the list below\n" \
           f"{i + 1})Performance comparison with standard configuration\n" \
           f"{i + 1})Performance comparison with custom configuration\n" \
           f"{i + 1})MHS resolver with best configuration\n" \
           f"{i + 1})Custom run\n" \
           f"{i + 1})Info\n" \
           ">>> "


def clear_all_close_all():
    print('\n' * 10)


def performance_comparison():
    launcher.performance_comparation()


def info():
    clear_all_close_all()
    return "---INFO SUBMENU---" \
           "This software has been developped by Alessandro Trainini and Francesco Cremascoli for the exam of " \
           "Algoritmo e strutture dati. We are the very best in the world."


def custom_run():
    return "Custom run"

if __name__ == '__main__':
    main()
