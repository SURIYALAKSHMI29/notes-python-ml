"""
Question:
Implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case.
"""


def convert_to_snake_case(camel_case: str) -> str:
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_"
        snake_case += char.lower()
    return snake_case.lstrip("_")

    # using Regex
    # return re.sub(r"([A-Z])", r"_\1", camel_case).lower().lstrip("_")


def main():
    camel_case = input("CamelCase: ")
    print(f"snake_case: {convert_to_snake_case(camel_case)}")


main()

"""

# Alternative solution using regex
Syntax:
    re.sub(pattern, repl, string, count=0, flags=0)

Parameters:

pattern → The regex pattern you want to search for.
Example: r"[A-Z]" (any uppercase letter).

repl → The replacement string or function.

If a string, it can use backreferences like \1, \2 … for captured groups.

If a function, it will be called with each match and return the replacement.

string → The input string to perform the replacement on.

count (optional) → Max number of replacements.

Default 0 → replace all matches.

Example: count=1 → only replace the first match.

flags (optional) → Regex flags like re.IGNORECASE, re.MULTILINE, etc.



def convert_to_snake_case(camel_case: str) -> str:
    return re.sub(r"([A-Z])", r"_\1", camel_case).lower().lstrip("_")
    
"""
