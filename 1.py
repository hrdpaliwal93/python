class Student:
    def __init__(self , name):
        self.name = name
    def getname(self):
        print(self.name)
s1 = Student("hardik")
s1.getname()