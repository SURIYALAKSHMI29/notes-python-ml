"""

Question:
implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

"""


def get_input():

    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if x > y or y == 0:
                continue

            return (x, y)

        except ValueError:
            pass


def get_percentage():
    x, y = get_input()
    percentage = (x / y) * 100

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return round(percentage)


def main():
    percentage = get_percentage()
    if percentage in ["E", "F"]:
        print(percentage)
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
