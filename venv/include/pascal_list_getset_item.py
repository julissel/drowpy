class PascalList:
    def __init__(self, original_list=None):
        self.container = original_list or []

    def __getitem__(self, index):
        return self.container[index - 1]

    def __setitem__(self, index, value):
        self.container[index - 1] = value

    def __str__(self):
        return self.container.__str__()


numbers = PascalList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(numbers)
print(numbers[1])
print()
numbers[5] = 25
print(numbers)
