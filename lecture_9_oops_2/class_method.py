class Person:
    name = "anonymous"

    def changeName(self, name):
        # self.name = name
        # Person.name = name #class 
        self.__class__.name = "zsxcdvfg" #class 

    # decorator
    @classmethod #cls argument 

    def change_name(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("ram ji")
# p1.change_name("hello ram ji")
print(p1.name)
print(Person.name)