class Student:
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks
    
    def print_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)


s1 = Student("Amrendra",[99,98,97])
s1.print_avg()

s1.name = "Bahubali"
s1.print_avg()