class Car:
    def __init__(self, name, price):
        self._name = "ww"
        self._price = 22  # underscore denotes it's a protected attribute

    # Getter for name
    @property
    def name(self):
        return "rrr"+self._name

    # Setter for name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("Name must be a string")

    # Getter for price
    @property
    def price(self):
        return self._price

    # Setter for price
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            raise ValueError("Price must be positive")

# Usage
car1 = Car("Toyota", 25000)

# Accessing name and price using the getter
print(car1.name)  # Output: Toyota
print(car1.price)  # Output: 25000

# Modifying name and price using the setter
car1.name = "Honda"
car1.price = 27000

# Accessing modified values
print(car1.name)  # Output: Honda
print(car1.price)  # Output: 27000
# car1.price = -27000

# Attempting to set an invalid price
# car1.price = -1000  # This will raise ValueError: Price must be positive
