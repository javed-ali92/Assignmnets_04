def print_ones_digit(num):
    print(f"The ones digit is {num % 10}")

def main():
    number = int(input("\n\033[1;3mEnter a number: \033[0m"))
    print_ones_digit(number)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()