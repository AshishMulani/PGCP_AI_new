# Q.2 Create an Account class Hierarchy
# Account with super class (acc_id, name, balance)
# methods - withdraw and deposit
#


# Create user class with user interface that gives 2 menu options
# 1. Deposit
# 2. Withdraw
# Both options will ask user to enter money to withdraw/deposit
# Display a statement with each transaction and final balance after user exits from the menu
# Identify possible Exceptions and implement them

from abc import ABC,abstractmethod

class Account(ABC):
    def __init__(self,accid,name,balance):
        self._accid=accid
        self._name=name
        self._balance=balance

    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass

    def __str__(self):
        return f'name:{self._name} balance:{self._balance}'
#--------------------------------------------------
# Create SavingsAccount as sub class of account - additional field (type - personal/corporate etc)
# implement withdraw and deposit such that
# - maximum upto 1 lak can be deposited in an account at a time
# - Min balance 5000 must be maintained while withdrawal (if type = corporate you withdraw full amount = balance)

class SavingsAccount(Account):
    def __init__(self,accid,name,balance,type):
        super().__init__(accid,name,balance)
        self._type=type

    def withdraw(self,amount):
        if self._type.lower()=='personal':
            if self._balance-amount<5000:
                raise Exception('Cannot withdraw:Account below min balance')
            else:
                self._balance=self._balance-amount
            return self._balance

        # else:
        #     raise Exception('Entered wrong Account type')

        if self._type.lower() == 'corporate':
            if self._balance<amount:
                raise Exception('Cannot withdraw:Insufficient balance')
            else:
                self._balance = self._balance - amount
            return self._balance

        else:
            raise Exception('Entered wrong Account type')

    def deposit(self,amount):
        if amount>100000:
            raise Exception('Cannot add more than 1 lak in account')
        else:
            self._balance+=amount
        return self._balance
#--------------------------------------------------
# Create CurrentAccount as sub class of account
# implement withdraw and deposit such that
# - maximum upto 2 lak can be deposited in an account at a time
# - Min balance 10000 must be maintained while withdrawal

class CurrentAccount(Account):
    def __init__(self,accid,name,balance):
        super().__init__(accid,name,balance)

    def withdraw(self,amount):
        if self._balance - amount < 10000:
            raise Exception('Cannot withdraw:Account below min balance')
        else:
            self._balance = self._balance - amount
        return self._balance


    def deposit(self,amount):
        if amount > 200000:
            raise Exception('Cannot add more than 1 lak in account')
        else:
            self._balance += amount
        return self._balance

#---------------------------------------------------

# Create Bank App with Transaction class
# Create Method withdraw_from_account(account : Account)  and deposit_to_account(account : Account)
# These methods will return the new balance after deposit/withdraw

class Transaction:

    @staticmethod
    def withdraw_from_account(account : Account,amount):
        print(f'Balance after withdraw: {account.withdraw(amount)}')

    @staticmethod
    def deposit_to_account(account: Account,amount):
        print(f'Balance after deposit: {account.deposit(amount)}')

sap=SavingsAccount(101,'Pranita',80000,'personal')
sac=SavingsAccount(101,'Dhriti',180000,'corporate')
ca=CurrentAccount(101,'Ashish',280000)

print(sap)
Transaction.withdraw_from_account(sap,5000)
Transaction.deposit_to_account(sap,10000)
print('==================================')

print(sac)
Transaction.withdraw_from_account(sac,80000)
Transaction.deposit_to_account(sac,50000)
print('==================================')

print(ca)
Transaction.withdraw_from_account(ca,50000)
Transaction.deposit_to_account(ca,25000)
print('==================================')