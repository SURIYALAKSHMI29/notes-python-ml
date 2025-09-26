class MyList:
    def __init__(self):
        self.data = []

    def __getitem__(self, i):
        return self.data[i]

    def __setitem__(self, i, v):
        self.data[i] = v

    def __delitem__(self, i):
        del self.data[i]  # calls python built-in list deletion

    def __contains__(self, v):
        return v in self.data

    def __len__(self):
        return len(self.data)

    def __call__(self, v):
        self.data.append(v)
        # makes my object callable, we can define anything we want here

    # enter, exit -> context manager methods
    # common use: opening/closing files
    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, *args):
        print("Exit")


# Usage
obj = MyList()
obj(10)  # __call__
obj(20)
print(len(obj))  # __len__ → 2
print(obj[0])  # __getitem__ → 10
print(20 in obj)  # __contains__ → True
del obj[1]  # __delitem__

with MyList() as ml:  # __enter__, __exit__
    ml(99)
