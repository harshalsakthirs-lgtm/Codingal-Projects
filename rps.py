import random
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

choices = ["rock", "paper", "scissors"]

def winner(player, computer):
    if player == computer:
        return "tie"
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "player"
    return "computer"

def get_player_choice():
    while True:
        choice = input(Fore.CYAN + "Choose rock, paper, or scissors (or 'quit'): ").strip().lower()
        if choice in choices or choice == "quit":
            return choice
        print(Fore.RED + "Invalid choice! Try again.\n")

def main():
    print(Fore.MAGENTA + Style.BRIGHT + "\n🎮 ROCK • PAPER • SCISSORS 🎮")
    print(Fore.YELLOW + "Best of 3 — let's play!\n")

    player_score = 0
    comp_score = 0

    while player_score < 2 and comp_score < 2:
        player = get_player_choice()
        if player == "quit":
            print(Fore.YELLOW + "Goodbye! 👋")
            return

        computer = random.choice(choices)
        print(Fore.BLUE + f"Computer chose: {computer}")

        result = winner(player, computer)
        if result == "tie":
            print(Fore.WHITE + "It's a tie!\n")
        elif result == "player":
            player_score += 1
            print(Fore.GREEN + "✅ You win this round!\n")
        else:
            comp_score += 1
            print(Fore.RED + "❌ Computer wins this round!\n")

        print(Fore.YELLOW + f"Score → You: {player_score}  |  Computer: {comp_score}\n")

    if player_score > comp_score:
        print(Fore.GREEN + Style.BRIGHT + "🎉 You won the match!")
    else:
        print(Fore.RED + Style.BRIGHT + "💻 Computer won the match. Better luck next time!")

if __name__ == "__main__":
    main()
