"""
Show that function is first class object
"""


def arithmetic(func, x, y):  # passing as parameter
    return func(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def operation(name):  # return from function
    if name == "add":
        return add
    else:
        return sub


add_func = add  # assigned to a variable
print(add_func(4, 9))  # 13

arithmetic_func = [add, sub]  # stored in a list
print(arithmetic_func[1](4, 1))  # sub(4,1) -> 3


print(arithmetic(add, 4, 9))  # 13

op = operation("sub")
print(op(9, 8))  # sub(9,8) -> 1
