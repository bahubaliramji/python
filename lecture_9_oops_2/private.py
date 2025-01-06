class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #pvt by __
    
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12344556", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())


class Person:
    __name = "anpnymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()


p1 = Person()
# print(p1.__hello())
# print(p1.__name)
print(p1.welcome())