"""'

Question:
dollars_to_float, which should accept a str as input (formatted as $##.##,
wherein each # is a decimal digit), remove the leading $, and return the
amount as a float. For instance, given $50.00 as input, it should return 50.0.
percent_to_float, which should accept a str as input (formatted as ##%,
wherein each # is a decimal digit), remove the trailing %, and return the
percentage as a float. For instance, given 15% as input, it should return 0.15.

"""


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    # print(dollars)
    percent = percent_to_float(input("What percentage would you like to tip?"))
    # print(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the leading $
    modified_d = d[1:]
    # modified_d = d.replace("$", "")
    # modified_d = d.lstrip("$")

    return round(float(modified_d), 1)


def percent_to_float(p):
    modified_p = p[:-1]
    return float(modified_p) / 100


main()
