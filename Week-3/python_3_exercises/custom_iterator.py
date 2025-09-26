class MyIter:
    def __init__(self, data):
        self.data = list(data)  # data -> should be a sequence, as it is index based
        self.index = 0

    def __iter__(self):
        return self  # iterator returns itself

    def __next__(self):
        if self.index >= len(self.data):
            print("Reached end")
            raise StopIteration
            # usually raises StopIteration, by default for loop handles it

        value = self.data[self.index]
        self.index += 1
        return value


list1 = [1, 4, 6, 9]
iter_list1 = MyIter(list1)

for element in iter_list1:
    print(element)
