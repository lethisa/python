class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """ this class generates checking account object"""
    
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee
    
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

jack_checking = Checking("jack.txt", 10)
jack_checking.transfer(100)
print(jack_checking.balance)
jack_checking.commit()
print(jack_checking.type)

john_checking = Checking("john.txt", 5)
john_checking.transfer(100)
print(john_checking.balance)
john_checking.commit()
print(john_checking.type)
print(jack_checking.__doc__)