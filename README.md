# Python Banking Program

## Overview
This is a simple **Python-based Banking Program** that allows users to perform basic financial transactions such as:
- Checking account balance
- Depositing money
- Withdrawing money

The program runs in a terminal-based menu system and provides simple input-based navigation.

---
## Features
- **Show Balance:** Display the current account balance.
- **Deposit Funds:** Allow users to deposit a positive amount into their balance.
- **Withdraw Funds:** Enable users to withdraw an amount, with validation for sufficient balance.
- **Exit Option:** Quit the banking application gracefully.

---
## How to Run
### Prerequisites
Ensure you have **Python 3.x** installed on your machine.

### Steps to Run
1. Clone this repository or copy the script.
2. Open a terminal and navigate to the directory where the script is saved.
3. Run the program with the following command:
   ```bash
   python banking_program.py
   ```

---
## Usage Guide
1. **Launching the Program:**
   - Upon running the script, a menu will be displayed with options from 1 to 4.

2. **Menu Options:**
   - Enter **1** to show your current balance.
   - Enter **2** to deposit funds.
   - Enter **3** to withdraw funds.
   - Enter **4** to exit the program.

### Example Interaction
```plaintext
************************
     Banking Program    
************************
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
************************
Enter your choice (1-4): 2
************************
Enter an amount to be deposited: 100
************************
```

---
## Code Explanation
### Key Functions
1. `show_balance(balance)`: Displays the current account balance.
2. `deposit()`: Prompts the user to enter a positive amount to deposit and returns the amount.
   - Validates that the deposit amount is not negative.
3. `withdraw(balance)`: Prompts the user to enter an amount to withdraw.
   - Ensures the withdrawal amount does not exceed the current balance and is not negative.
4. `main()`: Handles the main menu logic and user interaction.

### Error Handling
- Prevents negative deposits and withdrawals.
- Displays error messages for invalid amounts and insufficient funds.
- Ensures users can only select valid menu options.

---
## Sample Output
```plaintext
************************
Your balance is $0.00
************************
************************
Enter an amount to be deposited: 150.00
************************
************************
Your balance is $150.00
************************
