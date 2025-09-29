"""usage of defaultdict, missingitem, setdefault, Counter, OrderedDict"""

from collections import Counter, OrderedDict, defaultdict

dic1 = defaultdict(set)  # requires a callable as first argument
dic1["a"].add(2)
print(dic1)  # defaultdict(<class 'set'>, {'a': {2}})
print(dic1["b"])  # set()


# __missing__ example
class MyDict(dict):
    def __missing__(self, key):  # if not implemented, then KeyError raises
        return "Not Found"


dic2 = MyDict()
print(dic2["b"])  # Not Found


# setdefault - if not present, then sets the default value
#            - else doesn't change the default value
d = {}
print(d.setdefault("x", 10))  # 10 (inserted)
print(d.setdefault("x", 99))  # 10 (unchanged)


# Counter
c = Counter("Sahira")
print(c)
print(c.most_common(2))


# OrderedDict
od1 = OrderedDict({"x": 1, "y": 2})
od2 = OrderedDict({"y": 2, "x": 1})
print(od1 == od2)  # False -> order changed
od1.move_to_end("x")
print(od1)  # x moved to end ->  OrderedDict({"y": 2, "x": 1})
