"""

Question:
Implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
and outputs the number of lines of code in that file, excluding comments and blank lines. If the user
does not specify exactly one command-line argument, or if the specified file’s name does not end in .py,
or if the specified file does not exist, the program should instead exit via sys.exit.

"""

import sys


def valid_extension(file: str) -> bool:
    return file.endswith(".py")


def count_lines(file):
    try:
        with open(file, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File does not exist!")
        sys.exit(1)

    count = 0
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            count += 1
    return count


def main():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    file = sys.argv[1]

    if not valid_extension(file):
        print("Not a python file")
        sys.exit(1)

    lines_count = count_lines(file)
    print(lines_count)


if __name__ == "__main__":
    main()
