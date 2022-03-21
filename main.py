# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from matrix_parser import MatrixParser


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Bella quebec, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def main():
    print("Prosciutto")
    parser = MatrixParser()
    parser.parse_file_number_n()
    for line in parser.sets_viewable_using_domain():
        print(*line, sep="\t")


if __name__ == '__main__':
    main()
