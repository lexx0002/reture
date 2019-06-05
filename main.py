import json

class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, path):
        self.path = path
        with open(self.path) as file:
            file = json.load(file)
        self.file = file
        self.counter = 0
        self.last_line = len(file)

    def __next__(self):
        if self.counter != self.last_line:
            return self.file[self.counter]
            self.counter += 1
        else:
            raise StopIteration




s_iter2 = SimpleIterator('countries.json')
print(s_iter2)
print(s_iter2.__next__())
print(s_iter2.__next__())
