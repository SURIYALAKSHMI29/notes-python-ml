# new dunder methods in mapping related types


dic1 = {"a": 1, "b": 2, "c": 3}
dic1_keys = dic1.keys()

dic2 = {"a": 1, "f": 4, "e": 5}
dic2_keys = dic2.keys()

print(dic1_keys)  # dict_keys(['a', 'b', 'c'])
print(dic2_keys)  # dict_keys(['a', 'f', 'e'])


print(dic1_keys | dic2_keys)  # {'b', 'e', 'a', 'f', 'c'}

print(dic1_keys & dic2_keys)  # {'a'}


# new dunder methods:
# | -> __or__
# & -> __and__
# - -> __sub__
# ^ -> symmetric difference
