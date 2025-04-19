def main():
    #Get the number from user
    num = input("\033[1;3mEnter a number to be squared: \033[0m")
    num = float(num)

    #Square the number
    square = num * num
    print("\nThe square of the number is:", square)
if __name__ == '__main__':
    main()