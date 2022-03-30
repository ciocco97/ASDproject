from business_logic import launcher
from business_logic.launcher import *

SOLVER_DICTIONARY = {Launcher.ZERO: "no pre-pocess", Launcher.ROW: "only rows pre-process",
                     Launcher.COLUMN: "only columns pre-process", Launcher.ALL: "full pre-process"}
launcher = Launcher()


def main():
    while True:
        choice = int(input(main_menu() + ">>>"))
        if choice == 1:
            performance_comparison()
        elif choice == 2:
            custom_performance_comparison()
        elif choice == 3:
            best_solver()
        elif choice == 4:
            custom_run()
        elif choice == 5:
            info()
        else:
            break


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
    print('\n' * 10)


def performance_comparison():
    clc()
    message = " --- PERFORMANCE COMPARISON SUBMENU ---\n"
    message += "You have selected to run the standard comparison between with and without pre-process\n"
    if confirmation(message, performance_comparison):
        launcher.performance_comparison()
    process_end()


def custom_performance_comparison():
    clc()
    message = " --- CUSTOM PERFORMANCE COMPARISON SUBMENU ---\n"
    message += "You have selected to run the custom performance comparison between with and without pre-process\n"
    if confirmation(message, performance_comparison):
        launcher.performance_comparison()
    process_end()


def best_solver():
    clc()
    message = " --- BEST RESOLVER SUBMENU ---\n"
    message += "You have selected to run all the tests with the most performing configuration\n"
    if confirmation(message, best_solver):
        launcher.set_pre_process(Launcher.ALL)
        launcher.solve_range(0, -1)
    process_end()


def info():
    clc()
    i = 1
    text = "---INFO SUBMENU---\n" \
           "This software has been developped by Alessandro Trainini and Francesco Cremascoli (Eils team) for the " \
           "exam of Algoritmi e strutture dati.\n" \
           "Down below is reported the details of the main menu entry:\n"
    text += f"{i})Performance comparison with standard configuration\n"
    text += "\tWith this option you'll be able to compare the performance of this resolver with and without the pre-process\n"
    text += "\tIn this configuration, all the files available will be executed all in one execution\n"
    i += 1
    text += f"{i})Performance comparison with custom configuration\n"
    text += "\tWith this option you'll be able to compare the performance of this resolver with and without the pre-process\n"
    text += "\tIn this configuration, will be the user to specify the files that will be executed\n"
    i += 1
    text += f"{i})MHS resolver with best configuration\n"
    text += "\tWith this option, the resolver will execute all the available files with the best configuration, in order\n"
    text += "\tto process the files in the shortest time possible\n"
    i += 1
    text += f"{i})Custom run\n"
    text += "\tWith this option, the user will specify which files and the configuration the files will be executed with\n"
    i += 1
    text += f"{i})Info\n"
    i += 1
    text += f"{i})Exit\n"
    text += "press enter to get back to main menu"
    input(text)
    main_menu()


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

    if confirmation(message, custom_run):
        launcher.set_pre_process(pp_choice)
        if input_type == 1:
            launcher.solve_file_name(filename)
        elif input_type == 2:
            launcher.solve_file_number(file_number)
        else:
            launcher.solve_range(start, end)
    process_end()


def confirmation(message, callback) -> bool:
    message += "Do you want to run this configuration?\n"
    message += "1) Run it\n"
    message += "2) Back to previous submenu\n"
    message += "3) Back to main menu\n"

    choice = int(input(message + ">>>"))
    print(choice)
    if choice == 1:
        return True
    elif choice == 2:
        callback()
    else:
        main_menu()
    return False


def process_end():
    message = "The run has concluded successfully, you can find details of the result in the log file\n"
    message += "1) Back to main menu\n"
    message += "2) Exit\n"
    choice = int(input(message + ">>>"))
    print(choice)
    if choice == 1:
        main_menu()
    else:
        exit(0)


if __name__ == '__main__':
    main()
