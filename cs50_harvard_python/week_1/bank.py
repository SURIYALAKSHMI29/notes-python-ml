"""

Question:
mplement a program that prompts the user for a greeting. If the greeting
starts with “hello”, output $0. If the greeting starts with an “h” (but not
“hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in
the user’s greeting, and treat the user’s greeting case-insensitively.

"""


def dollars_earned(greeting: str) -> int:
    lowered_greeting = greeting.lower().lstrip()
    if lowered_greeting.startswith("hello"):
        return 0
    elif lowered_greeting.startswith("h"):
        return 20
    else:
        return 100


def main():
    greeting = input("Hello!\nGreeting:")
    print(f"${dollars_earned(greeting)}")


main()
