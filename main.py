import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {'A':2, 'B':4, 'C':6, 'D':8}

symbol_values = {'A':5, 'B':4, 'C':3, 'D':2}

def get_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): 
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = columns[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings = values[symbol] * bet  
            winning_lines.append(line + 1)
    return winnings, winning_lines

             
            
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)    
    
    return columns


def print_slot_machine(columns):
    print()
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:    
                print(column[row], end = '')
             
        print()        
        
                    

def deposit():
    while True:
        amount = input('Please enter your deposit $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Deposit should be greater than 0')
        else:
            print('Please enter a number') 
    return amount               


def get_no_of_lines():
    while True:
        lines = input(f'Please enter the number of lines you want to bet on (1-{MAX_LINES})')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Please enter valid amount of lines to bet')
        else:
            print('Please enter a number') 
    return lines  


def get_bet():
    while True:
        bet = input('Enter your bet on each line $') 
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'The bet must between ${MIN_BET} and ${MAX_BET}')
        else:
            print('Please enter a number')        
    return bet

def spin(balance):
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You don't have enough balance to bet that amount, your current balance is ${balance}") 
        else: 
            break
         
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}')
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = get_winnings(slots, lines, bet, symbol_values)
    print(f"You won on ${winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        keep_going = input('Press q to quit. Press enter to keep going!')
        if balance == 0:
            break
        elif keep_going == 'q':
            break      
        else:
            balance += spin(balance)
            print(f'You left with ${balance}')
                      
        
main()        