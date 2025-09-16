"""

Question:
Implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636.
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

"""


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
        date = input("Date: ")
        try:
            if date[0].isalpha():
                month_day, year = date.split(",")
                month, day = month_day.split(" ")
                month = month.lower()

                if month not in month_map:
                    continue
                month = month_map.index(month) + 1
                day = int(day)
                year = int(year.strip())
            elif date.count("/") != 2:
                continue
            else:
                month, day, year = map(int, date.split("/"))
                # map(int, ...) applies int() to each item in the list

            if 1 <= month <= 12 and 1 <= day <= 31 and 999 < year <= 9999:
                return (year, month, day)
        except ValueError:
            continue


def main():
    year, month, day = get_date()
    print(f"{year}-{int(month):02}-{int(day):02}")


main()
