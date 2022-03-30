from business_logic import launcher
from business_logic.launcher import *

SOLVER_DICTIONARY = {Launcher.ZERO: "No pre-pocess", Launcher.ROW: "Only rows pre-process",
                     Launcher.COLUMN: "Only columns pre-process", Launcher.ALL: "Full pre-process"}
launcher = Launcher()


def main():
    while True:
        choice = int(input(main_menu()))
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


def get_menu(sentence: str, options: list, show_input: bool = True):
    text = sentence
    for index, option in enumerate(options):
        text += f"\t{index + 1})" + str(option) + "\n"
    return text + (">>>" if show_input else "")


def main_menu():
    clc()
    return get_menu("---Welcome to Eils MHS resolver v 1.47---\nPlease, select an option from the list below\n",
                    [
                        "Performance comparison with standard configuration",
                        "Performance comparison with custom configuration",
                        "MHS resolver with best configuration",
                        "Custom run",
                        "Info",
                        "Exit"
                    ])


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
    sentence = "---INFO SUBMENU---\n" \
               "This software has been developped by Alessandro Trainini and Francesco Cremascoli (Eils team) for the exam of Algoritmi e strutture dati.\n" \
               "Down below is reported the details of the main menu entry:\n"
    sentence += get_menu(sentence,
                         [
                             "Performance comparison with standard configuration\n\tWith this option you'll be able to compare the performance of this resolver with and without the pre-process\n\tIn this configuration, all the files available will be executed all in one execution",
                             "Performance comparison with custom configuration\n\tWith this option you'll be able to compare the performance of this resolver with and without the pre-process\n\tIn this configuration, will be the user to specify the files that will be executed",
                             "MHS resolver with best configuration\n\tWith this option, the resolver will execute all the available files with the best configuration, in order\n\tto process the files in the shortest time possible",
                             "Custom run\n\tWith this option, the user will specify which files and the configuration the files will be executed with",
                             "Info",
                             "Exit"
                         ], False
                         )
    input(sentence + "press enter to get back to main menu")
    main_menu()


def custom_run():
    clc()
    message = "You selected to run "
    text = "---CUSTOM RUN SUBMENU---\nHow do you want to specify the input file?\n"
    input_type = int(input(get_menu(text, ["By filename",
                                           "By index",
                                           "By range (from one to another)"
                                           ])))
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

    text = "Which kind of pre-process do you want to run?\n"
    pp_choice = int(input(get_menu(text, SOLVER_DICTIONARY.values()))) - 1
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
    message += get_menu(message, ["Run it",
                                  "Back to previous submenu",
                                  "Back to main menu"])
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
    get_menu(message, ["Back to main manu",
                       "Exit"])
    choice = int(input(message + ">>>"))
    print(choice)
    if choice == 1:
        main_menu()
    else:
        exit(0)


if __name__ == '__main__':
    main()
