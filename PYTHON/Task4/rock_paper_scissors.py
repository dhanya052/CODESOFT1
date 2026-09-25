"""
TASK 4 - Rock-Paper-Scissors Game
CodSoft Python Programming Internship

A command-line Rock-Paper-Scissors game against the computer, with
score tracking across multiple rounds and a friendly user interface.

Run:
    python rock_paper_scissors.py
"""

import random

CHOICES = ["rock", "paper", "scissors"]
BEATS = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}
SHORTCUTS = {"r": "rock", "p": "paper", "s": "scissors"}


def get_user_choice():
    while True:
        raw = input("Choose rock, paper, or scissors (or r/p/s): ").strip().lower()
        if raw in CHOICES:
            return raw
        if raw in SHORTCUTS:
            return SHORTCUTS[raw]
        print("Invalid choice. Please type rock, paper, scissors (or r/p/s).")


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    if BEATS[user] == computer:
        return "user"
    return "computer"


def print_banner():
    print("=" * 36)
    print("     ROCK - PAPER - SCISSORS")
    print("=" * 36)


def main():
    print_banner()
    user_score = 0
    computer_score = 0
    round_num = 0

    while True:
        round_num += 1
        print(f"\n--- Round {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose:      {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        again = input("\nPlay another round? [Y/n]: ").strip().lower()
        if again.startswith("n"):
            break

    print("\n===== FINAL SCORE =====")
    print(f"You: {user_score}  |  Computer: {computer_score}")
    if user_score > computer_score:
        print("🏆 You won the match overall! Congratulations!")
    elif user_score < computer_score:
        print("💻 The computer won the match overall. Better luck next time!")
    else:
        print("🤝 The match ended in a tie overall!")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
