def add_three_copies(my_list, data):
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    message = input("\033[1;3mEnter a message to copy:\033[0m ")

    messages = []  # Empty list
    print("List before:", messages)

    add_three_copies(messages, message)

    print("List after:", messages)

if __name__ == '__main__':
    main()