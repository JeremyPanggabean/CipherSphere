# Python Slot Machine

## 🎰 Overview

The **Python Slot Machine** is a fun and simple terminal-based game that simulates a slot machine experience. Players can spin the reels, place bets, and win payouts based on symbol combinations.

---

## 🧩 Features

- **Random Reel Spin:** Generates random symbols for each spin.
- **Symbol Payouts:** Different payout multipliers based on symbol matches.
- **User Balance Management:** Tracks the user's current balance.
- **Interactive Gameplay:** Continuous play with the option to quit.

---

## 📜 Game Instructions

### How to Play

1. **Starting Balance:** Players begin with $100.
2. **Place a Bet:** Input a positive bet amount that does not exceed your current balance.
3. **Spin the Reels:** Watch the symbols spin and check if you win.
4. **Payouts:** Win based on the following combinations:
   - 🍒 Cherry : 3x your bet
   - 🍉 Watermelon: 4x your bet
   - 🍋 Lemon : 5x your bet
   - 🔔 Bell : 10x your bet
   - ⭐ Star : 20x your bet
5. **Continue or Quit:** Choose whether to play again or exit.

---

## 💻 How to Run

### Prerequisites

Ensure you have **Python 3.x** installed.

### Steps to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/JeremyPanggabean/Python-Slot_Machine.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Python-Slot_Machine
   ```
3. Run the game:
   ```bash
   python slot_machine.py
   ```

---

## 🔧 Code Breakdown

### Key Functions

- `spin_row()`: Generates a random row of symbols.
- `print_row(row)`: Displays the slot machine row.
- `get_payout(row, bet)`: Calculates the payout based on the row and bet amount.
- `print_game_instructions()`: Displays game instructions.
- `main()`: Handles the main game logic and user interactions.

### Error Handling

- Validates bet amounts (non-negative and within balance).
- Ensures valid input for game continuation.
- Provides user-friendly messages for errors.

---

## 🏆 Sample Gameplay

```plaintext
🎰 WELCOME TO PYTHON SLOT MACHINE 🎰
=== GOOD LUCK! ===

Current balance: $100
Place your bet amount: 10
Spinning...
*************
🍒 | 🍋 | 🍉
*************
Sorry you lost this round

Do you want to spin again? (Y/N): N
*******************************************
Game over! Your final balance is $90
*******************************************
```
