class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc_no = acc

    # debit 
    def debit(self, amount):
        self.bal -= amount
        print("Rs.", amount, "was debited")
        print("total balance is Rs.", self.get_balance())

    def credit(self, amount):
        self.bal += amount
        print("Rs.", amount, "was credited")
        print("total balance is Rs.", self.get_balance())

    def get_balance(self):
        return self.bal



acc1 = Account(120,1222222)
print(acc1.bal)
print(acc1.acc_no)
acc1.debit(1000)
acc1.credit(21100)
acc1.credit(40000)
acc1.debit(10000)