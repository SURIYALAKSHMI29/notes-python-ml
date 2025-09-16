"""

Question:
mplement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No

"""


def is_correct(answer):

    answer = answer.lower().strip()

    return answer in ["42", "forty-two", "forty two"]

    # match answer:
    #     case "42" | "forty two" | "forty-two":
    #         return True
    # return False


def main():
    answer = input(
        "What is the answer to the Great Question of Life, the Universe and Everything? "
    )

    print("Yes" if is_correct(answer) else "No")


main()
