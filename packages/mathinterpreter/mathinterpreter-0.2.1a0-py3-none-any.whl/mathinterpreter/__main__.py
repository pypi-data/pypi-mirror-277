import argparse
import readline
import sys

from mathinterpreter.calculate import calc


def main():

    if len(sys.argv) != 1:
        cli()
    else:
        while True:

            try:
                expression = input("calc > ")
            except (KeyboardInterrupt, EOFError) as error:
                print("\n", type(error).__name__)
                break
            else:
                expression = expression.strip().lower()
                if expression in ["q", "quit"]:
                    break

                print_value(expression)


def print_value(expression):
    value = calc(expression)
    if value:
        print(value)


def cli():

    parser = argparse.ArgumentParser(
        description="A simple math interpreter with a command line interface and an interactive mode.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "expression",
        nargs="*",
        help="Evaluate expression, which must be in one of the following forms:\n"
        "  1+1/2^4\n"
        "  1 + 1 / 2^4\n"
        "  1 + 1 / '(2^(4/2))'\n"
        "Note that to properly include parenthesis on command line calls it is necessary to"
        " use single or double quotes, ' or \", enclosing the expression.\n"
        "Default: interactive mode.",
    )

    args = parser.parse_args()
    expression = "".join(args.expression)
    print_value(expression)


if __name__ == "__main__":
    main()
