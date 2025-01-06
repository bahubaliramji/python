class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")



# single inheritance
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

# multi level inheritance
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("diesel")
print(car1.start())
