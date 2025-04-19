
def main():
    current_value = int(input("\n\033[1;3mEnter a number: \033[0m"))
    while current_value < 100:
        current_value = current_value * 2
        print(current_value , end = " ")
       
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()