# static methods doesn't need obejct

class Student:
    #data 
    # object attribute has priority over class attributes
    college = "UIT RGPV" #class attribute
    name = "Anonymous"

    # parameterized cosntructor
    def __init__(self, name, marks): #self is compulsary parameter refering the current object instance of the class
        self.name = name #attributes object
        self.marks = marks #attributes obeject 

    @staticmethod #decorator
    def hello():
        print("hello")
    

    

s1 = Student("karan",23) #parentheses for constructor
print(s1.name, s1.marks)
s1.hello()
