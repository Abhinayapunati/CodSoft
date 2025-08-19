import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def check_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("=== Rock Paper Scissors ===")
    while True:
        user_choice = input("Enter rock, paper or scissors (or 'q' to quit): ").strip().lower()
        if user_choice == 'q':
            print("Thanks for playing!")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(check_winner(user_choice, computer_choice))
        print("-" * 30)

if __name__ == "__main__":
    main()
