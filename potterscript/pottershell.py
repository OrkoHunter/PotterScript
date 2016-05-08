#!/usr/bin/env python3
import atexit
import os
import platform
import readline
import sys

histfile = os.path.join(os.path.expanduser("~"), ".python_history")

try:
    readline.read_history_file(histfile)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, histfile)

uname = platform.uname()

def main():
    print("Python {} {}".format(platform.python_version(), platform.python_build()))
    print()
    print("PotterScript 0.0.1 (default, July 31 2016, 00:09:34)")
    print("[{}] on {} {}".format(platform.python_compiler(), uname.system, uname.release))
    print("Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.")
    print()

    P_NO = 1  # Prompt number
    class colors:
        INPUT = '\033[92m'
        OUTPUT = '\033[93m'
        ENDC = '\033[0m'

    while(True):

        try:
            query = input("In [" + colors.INPUT + str(P_NO) + colors.ENDC + "]: ")
            print()
            if query != '':
                # Process
                P_NO += 1
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt\n")
        except EOFError:
            try:
                prompt = input("\nDo you really want to exit ([y]/n)? ")
                if not prompt.strip() in ('n', 'N'):
                    sys.exit(0)
                else:
                    print()
            except EOFError:
                print()
                sys.exit(0)

if __name__ == '__main__':
    main()