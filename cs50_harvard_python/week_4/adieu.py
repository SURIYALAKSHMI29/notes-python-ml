"""

Question:
Implement a program that prompts the user for names, one per line, until the user inputs control-d.
Assume that the user will input at least one name. Then bid adieu to those names, separating two names
with one and, three names with two commas and one and, and 𝑛 names with 𝑛 −1 commas and one and.

"""

import sys


def main():

    names = []
    while True:
        try:
            name = input("Name:")
            names.append(name)
        except EOFError:
            if len(names) == 1:
                output_names = names[0]
            elif len(names) == 2:
                output_names = f"{names[0]} and {names[1]}"
            else:
                output_names = ", ".join(names[:-1]) + f", and {names[-1]}"
            print("\nAdieu, adieu, to", output_names)
            sys.exit(0)


main()
