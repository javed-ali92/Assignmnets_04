# ------------------------------
# 📌 Index Game Functions
# ------------------------------

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."


# ------------------------------
# 🎮 Index Game Runner
# ------------------------------

def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("\n🔢 Welcome to the Index Game!\n")
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    
    operation = input("\nEnter operation: ").lower()

    if operation == "access":
        index = int(input("Enter index to access: "))
        print("Result:", access_element(lst, index))
    
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print("Updated List:", modify_element(lst, index, new_value))
    
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Sliced List:", slice_list(lst, start, end))
    
    else:
        print("Invalid operation.")


# ------------------------------
# 🍓 List Practice Code
# ------------------------------

def list_practice():
    print("\n🍉 Welcome to the List Practice!")

    # Initial fruit list
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print("Initial fruit list length:", len(fruit_lst))

    # Add 'mango' at the end
    fruit_lst.append('mango')

    # Print the updated list
    print("Updated fruit list:")
    for fruit in fruit_lst:
        print("🍍", fruit)


# ------------------------------
# 🏁 Main Function
# ------------------------------

def main():
    list_practice()
    index_game()

if __name__ == '__main__':
    main()