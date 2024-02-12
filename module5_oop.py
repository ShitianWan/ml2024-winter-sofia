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


def main():
    n = int(input("Enter a positive integer: "))
    processor = NumberProcessor()
    processor.read_numbers(n)

    x = int(input("Enter an integer: "))
    result = processor.search_number_index(x)
    print("Result:", result)


if __name__ == "__main__":
    main()
