
# Importing the random module
import random

#Number of sides on the die
SIDES = 6

def roll_die():
    """Simulate rolling a die."""
    die1: int = random.randint(1, SIDES)
    die2: int = random.randint(1, SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)


def main():
    die1: int = 10
    print("die1 in main() start as: " + str(die1))
    roll_die()
    roll_die()
    roll_die()
    print("die1 in main() end as:" + str(die1))

if __name__ == '__main__':
    main()