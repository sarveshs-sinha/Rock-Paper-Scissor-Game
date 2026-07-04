import random

# List of choicess
choices = ["rock", "paper", "scissors"]

# Computer chooses randomly
computer = random.choice(choices)

# User enters a choice
user = input("Enter rock, paper, or scissors: ").lower()

# Check if the input is valid
if user not in choices:
    print("Invalid choice! Please enter rock, paper, or scissors.")

# Check for a draw
elif user == computer:
    print("It's a draw!")
    print("Computer chose:", computer)

# User wins
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
    print("Computer chose:", computer)

# Computer wins
else:
    print("Computer wins!")
    print("Computer chose:", computer)
