'''

Question:

'''


def convert_to_joules(mass_kg):
    energy_joules = mass_kg * (3 * 10**8) ** 2
    return energy_joules


def main():
    mass = int(input("Enter mass (in kg): "))
    energy = convert_to_joules(mass)
    print(f"Energy equivalent: {energy} joules")


main()