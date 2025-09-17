"""

Question:

"""

import random
import sys

from pyfiglet import Figlet


def get_font(fonts):
    if len(sys.argv) == 1:
        return random.choice(fonts)

    if sys.argv[1] not in ["-f", "--font"]:
        print("Error: Flag must be -f or --font")
        sys.exit(1)

    if len(sys.argv) < 3:
        print("Error: No font name provided")
        sys.exit(1)

    return sys.argv[2]


def set_font(f, figlet):
    try:
        figlet.setFont(font=f)
    except Exception:
        print(f"Error: Invalid font '{f}'")
        sys.exit(1)


def main():
    figlet = Figlet()
    user_input = input("Input:")
    font = get_font(figlet.getFonts())
    set_font(font, figlet)
    print(figlet.renderText(user_input))


main()
