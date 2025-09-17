"""

Question:
Implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str,
converting any codes (or aliases) therein to their corresponding emoji.

"""

from emoji import emojize


def convert_emojis(inp):
    words = inp.split()
    for word in words:
        if word.startswith(":") and word.endswith(":"):
            emoji = emojize(word, language="alias")
            if emoji:
                inp = inp.replace(word, emoji)
    return inp


def main():
    text = input("Input: ")
    emojized_text = convert_emojis(text)
    print(emojized_text)


main()
