"""

Question:
Implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art
using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

"""

import csv
import sys

from tabulate import tabulate


def valid_extension(file: str) -> bool:
    return file.endswith(".csv")


def tabulate_csv(file):
    try:
        with open(file, "r") as file:
            reader = csv.DictReader(file)  # it has iterator of dictionaries
            data = list(reader)  # converting as list of dictionaries
    except FileNotFoundError as e:
        print("File not found", e)
        sys.exit(1)

    print(
        tabulate(data, headers="keys", tablefmt="grid")
    )  # tabulate expects list of list or list of dictionaries


def main():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    file = sys.argv[1]

    if not valid_extension(file):
        print("Not a CSV file")
        sys.exit(1)

    tabulate_csv(file)


if __name__ == "__main__":
    main()
