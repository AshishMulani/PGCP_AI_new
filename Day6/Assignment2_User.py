# Create user class with user interface that gives 2 menu options
# 1. Deposit
# 2. Withdraw
# Both options will ask user to enter money to withdraw/deposit
# Display a statement with each transaction and final balance after user exits from the menu
# Identify possible Exceptions and implement them

from Assignment2_Accounts import(Account,SavingsAccount,CurrentAccount)
from Assignment2_Transaction import Transaction

class User:
    def __init__(self,account):
        self._account=account
        self._transaction=Transaction()
        self._statement=[]

    def menu(self):
        print('-------- Bank Menu --------')
        print('1)Deposit')
        print('2)Withdraw')
        print('3)Exit')
        while True:

            choice=int(input('Enter Choice: '))


            try:
                if choice==1:
                    bal = transaction.deposit_to_account(sap)


                    # msg=f'Deposited amount: {amt} | Balance: {bal}'
                    # print(msg)
                    # self._statement.append(msg)

                elif choice == 2:
                    amt = int(input('Enter amount to withdraw: '))
                    bal = self._transaction.withdraw_from_account(self._account, amt)
                    msg = f'Withdraw amount: {amt} | Balance: {bal}'
                    print(msg)
                    self._statement.append(msg)

                elif choice==3:
                    break

                else:
                    print('Invalid Choice')

            except Exception as e:
                print(e)
        self.display_statement()


    def display_statement(self):
        for s in self._statement:
            print(s)

sap=SavingsAccount(101,'Pranita',80000,'corporate')
User(sap).menu()