import random  # Importing the random module to pick random symbols for the slot machine

# Constants (UPPERCASE by convention)
MAX_LINES = 3     # Maximum number of lines a player can bet on
MAX_BET = 100     # Maximum bet allowed per line
MIN_BET = 1       # Minimum bet allowed per line

ROWS = 3  # Number of rows in the slot machine
COLS = 3  # Number of columns in the slot machine

# Dictionary: symbol -> how many times it appears in the slot machine "pool"
symbol_count = {
    "A": 2,  # 'A' appears twice in the pool
    "B": 4,  # 'B' appears four times
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # List to hold all symbols based on their count
    for symbol, count in symbols.items():  # Loop through dictionary items
        for _ in range(count):  # Add each symbol 'count' times
            all_symbols.append(symbol)

    columns = []  # Final slot machine columns
    for _ in range(cols):  # For each column
        column = []  # Start empty column
        current_symbols = all_symbols[:]  # Copy of the full symbol pool
        for _ in range(rows):  # Fill each row in the column
            value = random.choice(current_symbols)  # Pick random symbol
            current_symbols.remove(value)  # Remove so it can't repeat in the same column
            column.append(value)
        columns.append(column)  # Add completed column
    return columns

def deposit():
    """Ask the player how much money they want to deposit"""
    while True:
        amount = input("What would you like to deposit? $")  # Ask user for input
        if amount.isdigit():  # Check if input is a number
            amount = int(amount)  # Convert string to integer
            if amount > 0:  # Must be positive
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount  # Return the valid deposit amount

def get_number_of_lines():
    """Ask how many lines the player wants to bet on"""
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():  # Check if it's a number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:  # Check within allowed range
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Enter a number.")
    return lines

def get_bet():
    """Ask how much the player wants to bet per line"""
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:  # Check bet within limits
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def main():
    balance = deposit()  # Get starting balance from player
    lines = get_number_of_lines()  # Ask how many lines to bet on

    while True:
        bet = get_bet()  # Ask for bet per line
        total_bet = bet * lines  # Total bet = bet per line × number of lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount, your current balance is: ${balance}")
        else:
            break  # Exit loop if bet is valid

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

# Run the game
main()
