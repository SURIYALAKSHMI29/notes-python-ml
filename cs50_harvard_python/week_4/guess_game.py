"""

Question:
Implement a program that:

Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
   - If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
   - If the guess is larger than that integer, the program should output Too large! and prompt the user again.
   - If the guess is the same as that integer, the program should output Just right! and exit.

"""

import random


def start_game(hidden):
    while True:
        guess = get_number("Guess: ")
        if guess < hidden:
            print("Too small")
        elif guess > hidden:
            print("Too large")
        else:
            break

    print("Just right!")


def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            continue


def main():
    level = get_number("Level: ")
    hidden = random.randint(1, level)
    start_game(hidden)


main()
