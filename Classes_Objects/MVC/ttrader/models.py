import json
import random

BANK_FILE = 'bank.json'
BANK = {}

def load():
  global BANK
  with open(BANK_FILE, 'r') as f:
      BANK = json.load(f)

class Account:

    def __init__(self, acct_num, name, pin, balance):
        self.account_number = acct_num
        self.name = name
        self.pin = pin
        self.balance = balance

    def save(self):
        global BANK
        info = {"name": self.name, "pin": self.pin, "balance": self.balance}
        # add info dictionary to BANK dictionary
        BANK[self.account_number] = info
        # now save to a file
        with open(BANK_FILE, 'w') as f:
            json.dump(BANK, f)

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            self.save()

    def withdraw(self, amount):
        fee=1.0
        if self.balance >= amount and amount >= 0:
            self.balance -= (amount+fee)
            self.save()
            return True
        return False

    @classmethod
    def new(cls, name, pin):
        # generate a probably unique account number
        account_num = round(random.randint(0,9)*1e7)
        while account_num in BANK: # ensure it's unique
            account_num = round(random.randint(0,9)*1e7)
        # now make the account object
        acct = Account(account_num, name, pin, 0)
        acct.save() # make sure it's saved in the BANK
        return acct # new Account object ready for use

    @classmethod
    def login(cls, acct_num, pin):
        if acct_num in BANK:
            if BANK[acct_num]['pin'] == pin:
                # create and return the Account object
                name = BANK[acct_num]['name']
                balance = BANK[acct_num]['balance']
                acct = Account(acct_num, name, pin, balance)
                return acct
        # failed either condition return None
        return None


greg = Account.new("Greg", "1234")
greg.withdraw(12)
