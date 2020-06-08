# learning about classes and objects on edx

class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Person:
    def __init__(self):
        self.name = Name()
        self.eyecolor = '[no eye color]'
        self.age = -1

john = Student('john', 'jason')
print(john.firstname)
