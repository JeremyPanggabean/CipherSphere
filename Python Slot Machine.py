# Python Slot Machine
import random
def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20

    return 0

def get_play_again_input():
    while True:
        play_again = input("Do you want to spin again? (Y/N): ").upper()
        if play_again in ['Y', 'N']:
            return play_again
        print("Enter a valid choice between (Y/N)")

def print_game_instructions():
    print("\n🎰 WELCOME TO PYTHON SLOT MACHINE 🎰")
    print("\n=== HOW TO PLAY ===")
    print("1. You start with $100 balance")
    print("2. Place your bet for each spin")
    print("3. Match 3 symbols to win!")
    print("\n=== WINNING COMBINATIONS ===")
    print("🍒 Cherry    : 3x your bet")
    print("🍉 Watermelon: 4x your bet")
    print("🍋 Lemon     : 5x your bet")
    print("🔔 Bell      : 10x your bet")
    print("⭐ Star      : 20x your bet")
    print("\n=== GOOD LUCK! ===\n")

    while True:
        user = input("Press Enter to start playing: ")
        if user == "":
            break
        print("Please press Enter to continue...")


def main():
    balance = 100

    print_game_instructions()

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        if balance <= 0:
            play_again = get_play_again_input()
            if play_again == 'Y':
                print(f"\nCan't continue the game because your balance is ${balance}")
                break

        play_again = get_play_again_input()
        if play_again == 'N':
            print("Thank you for Playing!")
            break

    print("*******************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("*******************************************")

if __name__ == '__main__':
    main()
