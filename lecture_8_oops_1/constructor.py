class Student:

    #data 
    # object attribute has priority over class attributes
    college = "UIT RGPV" #class attribute
    name = "Anonymous"

    # default constructor
    def __init__(self): #self is compulsary parameter refering the current object instance of the class
        pass

    # parameterized cosntructor
    def __init__(self, name, marks): #self is compulsary parameter refering the current object instance of the class
        self.name = name #attributes object
        self.marks = marks #attributes obeject 

    #methods (functions) first para must be self
    def welcome(self):
        print("Welcome student")

    def get_marks(self):
        return self.marks
    

    

s1 = Student("karan",23) #parentheses for constructor
s1.welcome()
print(s1.name, s1.marks)
print(s1.get_marks())


s2 = Student("Arjun",34) #parentheses for constructor
print(s2.name)
print(s2.marks, "\n", s2.college)


print(Student.college)
print(Student.name)
