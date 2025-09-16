"""

Question:
Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers,
and ignore any integer that isn’t an accepted denomination.
Accepted coins are 25 cents, 10 cents, and 5 cents.

"""


def main():
    amount = 50
    while amount > 0:
        print(f"Amount owed: {amount}")
        coin = int(input("Insert coin: "))
        if coin in [25, 10, 5]:
            amount -= coin

    print(f"Change owed: {abs(amount)}")


if __name__ == "__main__":
    main()
