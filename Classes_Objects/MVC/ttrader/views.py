

def logon_prompt():
    menu = """
    1) Create Account
    2) Login
    3) Exit
    """
    print(menu)
    choice = input('What do you want to do? ')
    return choice

def new_user_prompt():
    name = input('Enter your name: ')
    pin = input('Enter your pin: ')
    return [name, pin]

def login_prompt():
    account_num = input('Enter your account number: ')
    pin = input('Enter your pin: ')
    return [account_num, pin]

def login_fail():
    print('Incorrect account number or pin! Please try again')

def welcome(acct):
    print(f'Welcome! Account #{acct.account_number}')

def account_prompt():
    menu = """
    1) Show balance
    2) Deposit
    3) Withdraw
    4) Logout
    """
    print(menu)
    choice = input('Enter your choice: ')
    return choice

def show_balance(acct):
    print(f'Account #{acct.account_number} has a balance of ${acct.balance}')

def deposit_prompt():
    amount = float(input('How much would like to deposit? $'))
    return amount

def withdraw_prompt():
    amount = float(input('How much would like to withdraw? $'))
    return amount

def display_not_enough():
    print('Sorry you don\'t have sufficient funds for that withdraw')

def logout_screen():
    print('See you later!')

if __name__ == "__main__":
    logon_prompt()
