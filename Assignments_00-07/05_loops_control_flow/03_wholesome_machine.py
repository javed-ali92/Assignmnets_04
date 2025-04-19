def get_affirmation():
    affirmation = "I am capable of doing anything I put my mind to."

    while True:
        user_input = input(f"Please type the following affirmation: {affirmation} ")

        if user_input == affirmation:
            print("That's right! 🎉😊")
            break
        else:
            print("Hmmm 😔 That was not the affirmation. Please try again. 🔄")

if __name__ == "__main__":
    get_affirmation()