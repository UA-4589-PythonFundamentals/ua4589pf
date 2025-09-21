class BankAccount:

    def __init__(self, account_number, account_holder, balance=0.0):
        self.__account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance

    def account_holder(self):
        return self.__account_holder

    def deposit(self, amount):
        self.deposit_add = amount
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.deposit_min = amount
        if self.__balance > amount:
            self.__balance -= amount
            return self.__balance
        else:
            return print('Insufficient funds')

    def check_balance(self):
        return self.__balance

    @property
    def account_holder(self):
        return self._account_holder