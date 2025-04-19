def main():
    #Ask the favorite animal from user 
    animal = input("\033[1;3mWhat is yout favorite animals?\033[0m")
    animal = animal.lower()

    #Give the response on your favorite animal
    print("\nMy favorite animals are", animal)
if __name__ == '__main__':
    main()