"""

Question:
Implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the
equivalent number of Joules as an integer. Assume that the user will input an integer.

"""


def convert_to_joules(mass_kg):
    energy_joules = mass_kg * (3 * 10**8) ** 2
    return energy_joules


def main():
    mass = int(input("Enter mass (in kg): "))
    energy = convert_to_joules(mass)
    print(f"Energy equivalent: {energy} joules")


main()
