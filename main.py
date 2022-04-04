import os
import sys

from business_logic.launcher import Launcher
from cl_ui import cl_ui

path_separator = ","
PRE = "-p"
F_NAME = "-f"
D_NAME = "-d"
COMP = "-c"
OPTIONS = [PRE, F_NAME, D_NAME, COMP]


def launcher_config(args):
    launcher = Launcher()
    syntax_error = False
    i = 0
    while i < len(args):
        if args[i] in OPTIONS:

            if args[i] == PRE:  # Preprocessing
                all_preprocess = False
                if i + 1 < len(args):
                    ppo: str = args[i + 1]  # pre process option
                    if ppo.isnumeric():
                        if not (int(ppo) in Launcher.PRE_PROCESS_OPTIONS):
                            syntax_error = True
                    elif ppo in OPTIONS:
                        all_preprocess = True
                    else:
                        syntax_error = True
                else:
                    all_preprocess = True

                if all_preprocess:
                    launcher.set_pre_process(Launcher.ALL)
                elif syntax_error:
                    raise Exception(f"Syntax error near {PRE}")
                else:
                    launcher.set_pre_process(int(args[i + 1]))
                    i += 1

            elif args[i] == F_NAME:  # file
                file_path = ""
                if i + 1 >= len(args):
                    syntax_error = True
                else:
                    file_path: str = args[i + 1]
                    if os.path.exists(file_path):
                        pass
                    elif os.path.exists(os.path.abspath(file_path)):
                        file_path = os.path.abspath(file_path)
                    else:
                        syntax_error = True
                if syntax_error:
                    raise Exception(f"Syntax error near {F_NAME}")
                else:
                    launcher.set_file_path(file_path)
                    i += 1

            elif args[i] == D_NAME:  # Directory
                paths = []
                if i + 1 >= len(args):
                    syntax_error = True
                else:
                    for path in args[i + 1].split(path_separator):
                        path = os.path.normpath(path) + "\\"
                        if os.path.exists(path):
                            paths.append(path)
                        elif os.path.exists(os.path.abspath(path)):
                            paths.append(path)
                        else:
                            syntax_error = True
                if syntax_error:
                    raise Exception(f"Syntax error near {D_NAME}")
                else:
                    launcher.set_paths(paths)
                    i += 1
            elif args[i] == COMP:
                launcher.set_comparison(True)
        else:
            raise Exception(f"Option {args[i]} unknown")
        i += 1
    launcher.run_from_terminal()


def main():
    args = sys.argv
    if len(args) == 1:
        cl_ui()
    else:
        del args[0]
        launcher_config(args)


if __name__ == '__main__':
    main()
