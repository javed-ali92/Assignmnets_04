import random

N_NUMBERS: int = 10         # How many numbers to print
MIN_VALUE: int = 1          # Minimum possible number
MAX_VALUE: int = 100        # Maximum possible number

def main():
    for _ in range(N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value, end=" ")  # Print on the same line with space
    print()

if __name__ == '__main__':
    main()