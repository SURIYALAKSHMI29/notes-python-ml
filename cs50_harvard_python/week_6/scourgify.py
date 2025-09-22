"""

Question:
Implement a program that:

Expects the user to provide two command-line arguments:
    the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
    the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

"""

import csv
import sys


def valid_extension(file):
    return file.endswith(".csv")


def scourgify(file_1, file_2):
    try:
        with open(file_1, "r") as infile, open(file_2, "w") as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for dict in reader:
                name = dict["name"]
                last, first = map(str.strip, name.split(","))

                writer.writerow({"first": first, "last": last, "house": dict["house"]})

            # By default, the csv module uses quotechar='"'.
            # It removes the surrounding quotes from fields when reading

    except FileNotFoundError as e:
        print(f"Could not read {file_1}")
        sys.exit(1)


def main():

    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    file_1 = sys.argv[1]
    file_2 = sys.argv[2]

    if not valid_extension(file_1) or not valid_extension(file_2):
        print("Invalid file extension(s)")
        sys.exit(1)

    scourgify(file_1, file_2)


if __name__ == "__main__":
    main()
