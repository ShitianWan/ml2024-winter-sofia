from module5_mod import NumberProcessor

def main():
    n = int(input("Enter a positive integer: "))
    processor = NumberProcessor()
    processor.read_numbers(n)

    x = int(input("Enter an integer: "))
    result = processor.search_number_index(x)
    print("Result:", result)

if __name__ == "__main__":
    main()