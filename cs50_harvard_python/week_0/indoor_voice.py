'''
Question: 
Implement a program in Python that prompts the user for input and then outputs 
that same input in lowercase. Punctuation and whitespace should be outputted 
unchanged

'''


def main(): 
    user_input = input("Please enter a string: ")
    print(user_input.lower())


main()