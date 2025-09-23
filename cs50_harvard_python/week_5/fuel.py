"""

Question:
convert():
    Convert a fraction string "X/Y" into a percentage (rounded int 0-100).

    Raises:
        ValueError: if X or Y is not an integer, or X > Y
        ZeroDivisionError: if Y is 0

gauge():
    Return the fuel gauge string:
        - "E" if percentage <= 1
        - "F" if percentage >= 99
        - "Z%" otherwise

"""


def main():
    fraction = input("Fraction (X/Y): ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print(e)


def convert(fraction):
    try:
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)
    except ValueError:
        raise ValueError("Both X and Y must be integers")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x > y:
        raise ValueError("X cannot be greater than Y")
    if x < 0 or y < 0:
        raise ValueError("X and Y must be positive")

    percentage = round((x / y) * 100)
    return max(0, min(100, percentage))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
