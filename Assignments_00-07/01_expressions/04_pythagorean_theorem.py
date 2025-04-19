import math 

def main():
    ab = float(input("\033[1;3mEnter the length of side AB:\033[0m"))
    ac = float(input("\033[1;3mEnter the length of side BC:\033[0m"))

    # Calculate the length of side BC using the Pythogorean theorem
    bc = math.sqrt(ab**2 +ac**2)

    print(f"The length of hypotenuse is:{bc}")
if __name__ == '__main__':
    main()