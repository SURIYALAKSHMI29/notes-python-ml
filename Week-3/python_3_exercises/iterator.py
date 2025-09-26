# Iterables vs Iterators

# Iterable
lst = [1, 2, 3]
print(hasattr(lst, "__iter__"))  # True
print(hasattr(lst, "__next__"))  # False

# Iterator
it = iter(lst)  # creates iterator from iterable
print(hasattr(it, "__iter__"))  # True
print(hasattr(it, "__next__"))  # True

# Iterating
for x in it:
    print(x)
