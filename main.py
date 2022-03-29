import os
from os import system, name

import launcher
from launcher import *

SOLVER_DICTIONARY = {Launcher.ZERO: "no pre-pocess", Launcher.ROW: "only rows pre-process",
                     Launcher.COLUMN: "only columns pre-process", Launcher.ALL: "full pre-process"}
launcher = Launcher()


def main():
    end = False
    while not end:
        choice = int(input(main_menu() + ">>>"))
        if choice == 1:
            launcher.performance_comparison()
        elif choice == 2:
            launcher.custom_performance_comparison()
        elif choice == 3:
            launcher.best_resolver()
        elif choice == 4:
            custom_run()
        elif choice == 5:
            info()
        else:
            end = True


def main_menu():
    clc()
    i = 1
    text = "---Welcome to Eils MHS resolver v 1.47---\n"
    text += "Please, select an option from the list below\n"
    text += f"{i})Performance comparison with standard configuration\n"
    i += 1
    text += f"{i})Performance comparison with custom configuration\n"
    i += 1
    text += f"{i})MHS resolver with best configuration\n"
    i += 1
    text += f"{i})Custom run\n"
    i += 1
    text += f"{i})Info\n"
    i += 1
    text += f"{i})Exit\n"
    return text


def clc():
    print('\n' * 0)


def performance_comparison():
    launcher.performance_comparison()


def info():
    clc()
    return "---INFO SUBMENU---" \
           "This software has been developped by Alessandro Trainini and Francesco Cremascoli (Eils team) for the " \
           "exam of Algoritmi e strutture dati. We are the very best in the entire world."


def custom_run():
    clc()
    message = "You selected to run "
    i = 1
    text = "---CUSTOM RUN SUBMENU---\n"
    text += "How do you want to specify the input file?\n"
    text += f"{i})By filename\n"
    i += 1
    text += f"{i})By index\n"
    i += 1
    text += f"{i})By range\n"
    input_type = int(input(text + ">>>"))

    if input_type == 1:
        filename = input("filename to run: >>>")
        message += f"a file named {filename} "
    elif input_type == 2:
        file_number = int(input("number of file to run: >>>"))
        message += f"a file indexed by {file_number} "
    else:
        start = int(input("from file number: >>>"))
        end = int(input("to file number: >>>"))
        message += f"multiple files indexed from {start} to {end} "

    i = 0
    text = "Which kind of pre-process do you want to run?\n"
    text += f"{i + 1}){SOLVER_DICTIONARY[i]}\n"
    i += 1
    text += f"{i + 1}){SOLVER_DICTIONARY[i]}\n"
    i += 1
    text += f"{i + 1}){SOLVER_DICTIONARY[i]}\n"
    i += 1
    text += f"{i + 1}){SOLVER_DICTIONARY[i]}\n"
    pp_choice = int(input(text + "type of pre-process: >>>")) - 1
    launcher.set_pre_process(pp_choice)
    message += f"with {SOLVER_DICTIONARY[pp_choice]}\n"

    message += "Do you want to run it?\n"
    message += "1) Run it\n"
    message += "2) Back to custom run submenu\n"
    message += "3) Back to main menu\n"
    choice = int(input(message + ">>>"))

    if choice == 1:
        print(" - Custom run in process... please wait - \n")
        if input_type == 1:
            launcher.solve_file_name(filename)
        elif input_type == 2:
            launcher.solve_file_number(file_number)
        else:
            launcher.solve_range(start, end)
        print(" - End of the operation - ")
    elif choice == 2:
        custom_run()
    else:
        main_menu()


if __name__ == '__main__':
    main()
