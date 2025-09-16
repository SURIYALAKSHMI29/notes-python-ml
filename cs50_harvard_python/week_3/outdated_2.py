"""

Question:
Implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636.
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

"""


def parse_numeric(date):
    try:
        if date.count("/") != 2:
            return None
        month, day, year = map(int, date.split("/"))
        return (year, month, day)
    except ValueError:
        return None


def parse_textual(date, month_map):
    try:
        month_day, year = date.split(",")
        month, day = month_day.split()
        month = month.lower()

        if month not in month_map:
            return None

        month = month_map.index(month) + 1
        day = int(day)
        year = int(year.strip())
        return (year, month, day)
    except ValueError:
        return None


def check_valid(date):
    year, month, day = date
    return 1 <= month <= 12 and 1 <= day <= 31 and 999 < year <= 9999


def get_date():
    month_map = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]

    while True:
        date = input("Date: ").strip()
        parsed_date = (
            parse_textual(date, month_map) if date[0].isalpha() else parse_numeric(date)
        )

        if parsed_date and check_valid(parsed_date):
            return parsed_date


def main():
    year, month, day = get_date()
    print(f"{year}-{int(month):02}-{int(day):02}")


main()
