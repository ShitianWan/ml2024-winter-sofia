def main():
    n = int(input("Enter a positive integer: "))
    numbers = []
    for i in range(n):
        num = int(input("Enter number: "))
        numbers.append(num)
    x = int(input("Enter an integer: "))
    for i in range(n):
        if numbers[i] == x:
            return i + 1
    return -1

if __name__ == "__main__":
    print(main())