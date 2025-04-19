def read_phone_numbers():
    """
    User se naam aur number leke phonebook (dictionary) banata hai.
    """
    phonebook = {}  # Empty dictionary banayi

    while True:
        name = input("\nName: ")
        if name == "":  # Agar naam blank hai to loop break
            break
        number = input("Number: ")
        phonebook[name] = number  # Name ko number ke saath store kiya

    return phonebook


def print_phonebook(phonebook):
    """
    Phonebook ke saare name-number ko print karta hai.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
    """
    User ko allow karta hai phonebook me naam ke through number lookup karne ke liye.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":  # Agar blank input aaye to stop
            break
        if name not in phonebook:
            print(name + " is not in the phonebook\n")
        else:
            print(f"{phonebook[name]}\n")


def main():
    phonebook = read_phone_numbers()  # Phonebook banaya
    print("\n--- Phonebook Entries ---")
    print_phonebook(phonebook)        # Phonebook ko print kiya
    print("\n--- Lookup Mode ---")
    lookup_numbers(phonebook)         # Lookup karne diya


# Python ka boilerplate
if __name__ == '__main__':
    main()