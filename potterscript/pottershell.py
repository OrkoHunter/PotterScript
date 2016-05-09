#!/usr/bin/env python3
import atexit
import os
import platform
import rlcompleter
import readline
import sys
import traceback

from potterscript import release

def main():

    histfile = os.path.join(os.path.expanduser("~"), ".python_history")

    try:
        readline.read_history_file(histfile)
    except FileNotFoundError:
        pass

    atexit.register(readline.write_history_file, histfile)

    uname = platform.uname()

    readline.parse_and_bind('tab: complete')
    print("Python {} {}".format(platform.python_version(), platform.python_build()))
    print()
    print("PotterScript {} ({})".format(release.__version__, release.__date__))
    print("[{}] on {} {}".format(platform.python_compiler(), uname.system, uname.release))
    print("Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.")
    print()

    Q_NO = 1  # Prompt index

    class colors:
        INPUT = '\033[92m'
        OUTPUT = '\033[91m'
        ENDC = '\033[0m'

    while(True):
        try:
            query = input("In [" + colors.INPUT + str(Q_NO) + colors.ENDC + "]: ")
            if query != '':
                if query[-1] == ":":
                    # Take subsequent queries
                    while(True):
                        query_ = input("   ...: ")
                        if query_ != "":
                            query += "\n" + query_
                        else:
                            break
                # Process
                try:
                    out = eval(query)
                    if not "print(" in query:
                        print(colors.OUTPUT + "Out[" + str(Q_NO) + "]:" + colors.ENDC, end=" ")
                        print(out)
                    print()
                except SyntaxError:
                    try:
                        exec(query)
                    except SyntaxError as e:
                        print(colors.OUTPUT, end="")
                        print("-------------------------------------------------")
                        print(e)
                        print(colors.ENDC, end="")
                        print("Syntax Error in last line.")
                    except ImportError as e:
                        module = str(e).split()[-1]
                        print(colors.OUTPUT, end="")
                        print("-------------------------------------------------")
                        print("ImportError    Traceback (most recent call last):")
                        print(colors.ENDC, end="")
                        traceback.print_stack()
                        print("\n{}: import of {} blocked by dementors.".format(type(e).__name__, module))
                    except NameError as e:
                        name = str(e).split()[1]
                        print(colors.OUTPUT, end="")
                        print("-------------------------------------------------")
                        print("NameError      Traceback (most recent call last):")
                        print(colors.ENDC, end="")
                        traceback.print_stack()
                        print("\n{}: Bloody Hell, what is {} ?".format(type(e).__name__, name))
                    except Exception as e:
                        print(colors.OUTPUT, end="")
                        print("-------------------------------------------------")
                        print("Exception      Traceback (most recent call last):")
                        print(colors.ENDC, end="")
                        traceback.print_stack()
                        print("\n{}: {}".format(type(e).__name__, e))
                    print()
                except Exception as e:
                    print(colors.OUTPUT, end="")
                    print("-------------------------------------------------")
                    print("{}:".format(type(e).__name__) + colors.ENDC, end=" ")
                    print("{}".format(e))
                    print()

                Q_NO += 1
            else:
                print()
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