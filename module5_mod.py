class NumberProcessor:
    def __init__(self):
        self.numbers = []

    def read_numbers(self, n):
        for _ in range(n):
            num = int(input("Enter a number: "))
            self.numbers.append(num)

    def search_number_index(self, x):
        for i in range(len(self.numbers)):
            if self.numbers[i] == x:
                return i + 1
        return -1
