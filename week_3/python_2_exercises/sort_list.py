# sort list of tuples by ordering based on second element

list1 = [(1, 2), (2, 3, 4), (8, 1), (18, 0, 89)]


for t in sorted(list1, key=lambda t: t[1]):
    print(t)

# not as sorted(list1, key=t[1])
# because key expects a function not a value
# and t is undefined there
