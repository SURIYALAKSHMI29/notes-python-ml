"""

Question:

"""


def convert(time: str) -> float:
    hrs, min = time.split(":")
    hours = float(hrs) + float(min) / 60
    return hours


def check_meal(time: float) -> str:
    if 7 <= time <= 8:
        return "Breakfast time"
    elif 12 <= time <= 13:
        return "Lunch time"
    elif 18 <= time <= 19:
        return "Dinner time"
    return None


def main():
    time = input("What time is it? ")
    time = convert(time)
    meal = check_meal(time)
    if meal:
        print(meal)


if __name__ == "__main__":
    main()


# When you run a file directly (python myfile.py), Python sets the special variable __name__ = "__main__".
# When you import that same file from another module, __name__ becomes the module’s filename (e.g., "myfile"), not "__main__".
# So it ensures that the main() function runs only if the file is executed directly.
# If the file is imported, it won’t auto-run
