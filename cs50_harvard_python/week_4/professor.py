"""

Question:
Implement a program that:

Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative
integer with 𝑛 digits. No need to support operations other than addition (+).

Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the
program should output EEE and prompt the user again, allowing the user up to three tries in total for that
problem. If the user has still not answered correctly after three tries, the program should output the correct answer.

The program should ultimately output the user’s score: the number of correct answers out of 10.

"""

import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        score += solve_math_problem(level)
    print(f"Score: {score}")


def solve_math_problem(level):
    x = generate_integer(level)
    y = generate_integer(level)
    correct_ans = x + y
    for i in range(3):
        answer = input(f"{x} + {y} = ")
        try:
            if int(answer) == x + y:
                return 1
        except ValueError:
            pass
        print("EEE")
    print(f"{x} + {y} = {correct_ans}")
    return 0


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level <= 3:
                return level

        except ValueError:
            continue


def get_range(level):
    if level == 1:
        return (1, 9)
    elif level == 2:
        return 10, 99
    return 100, 999


def generate_integer(level):
    start, end = get_range(level)
    return random.randint(start, end)


if __name__ == "__main__":
    main()
