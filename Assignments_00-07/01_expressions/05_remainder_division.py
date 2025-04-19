def main():
    number = int(input("Enter a number:"))
    divisor = int(input("Enter a divisor:"))
     
    quotient = number // divisor 
    remainder = number % divisor 
     
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))
if __name__ == '__main__':
    main()