# function for sum numbers
def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num 
    return total

def main():
    numbers = [1,2,3,4,5]

    sumOfNum = sum_of_numbers(numbers)
    print(sumOfNum)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()