"""

Question:
Implement a program that prompts the user for a str of text and then outputs that same text
but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

"""

import re


def shorten(word: str) -> str:
    shortened_word = ""
    for char in word:
        if char not in "aeiouAEIOU":
            shortened_word += char
    return shortened_word

    # Alternative : using regex
    # return re.sub(r"[aeiouAEIOU]", "", word)


def main():
    tweet = input("Input: ")
    print(f"Output: {shorten(tweet)}")


if __name__ == "__main__":
    main()
