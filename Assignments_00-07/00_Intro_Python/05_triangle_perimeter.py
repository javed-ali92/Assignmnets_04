def main():
    #Get the length of the sides of the triangle from user
    side1:float = float(input("\n\033[1;3mWhat is the length of side 1?\033[0m "))
    side2:float = float(input("\033[1;3mWhat is the length of side 2?\033[0m "))
    side3:float = float(input("\033[1;3mWhat is the length of side 3?\033[0m "))
    #Calculate the perimeter of the triangle
    perimeter:float = side1 + side2 + side3
    #Display the perimeter of the triangle  
    print("\n\033[1;3mThe perimeter of the triangle is:\033[0m", perimeter)
    
if __name__ == '__main__':
    main()