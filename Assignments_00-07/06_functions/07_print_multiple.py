def print_multiple(message, repeats):
  for _ in range(repeats):
    print(message, end=" ")
  print()

def main():
  user_message = input("Please type a message: ")
  num_repeats = int(input("Enter a number of times to repeat your message: "))
  print_multiple(user_message, num_repeats)

if __name__ == "__main__":
  main()