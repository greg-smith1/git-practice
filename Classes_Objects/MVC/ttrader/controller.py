from models import Account, load
import views

def logon_loop():
    choice = None
    while choice != "3":
        choice = views.logon_prompt()
        if choice == "1":
            [name, pin] = views.new_user_prompt()
            acct = Account.new(name, pin)
            account_loop(acct)
        if choice == "2":
            [acct_num, pin] = views.login_prompt()
            acct = Account.login(acct_num, pin)
            if acct != None:
                account_loop(acct)
            else:
                views.login_fail()

def account_loop(acct): # takes in an account object
    choice = None
    while choice != "4":
        choice = views.account_prompt()
        if choice == "1":
            views.show_balance(acct)
        if choice == "2":
            amount = views.deposit_prompt()
            acct.deposit(amount)
        if choice == "3":
            amount = views.withdraw_prompt()
            # if the withdraw fails, display not enough
            if not acct.withdraw(amount):
                views.display_not_enough()
    views.logout_screen() # say bye
