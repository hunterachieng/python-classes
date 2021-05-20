class Student:
    school = "AkiraChix"
    # constructor method
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #method
    def greet(self):
        print(f"Hello {self.name}")

    def introduction(self):
        print(f"Hello, my name is {self.name} aged {self.age} I am studying in {self.school}")
    
    def origin(self,race):
        self.race=race
        print(f"I am from the {self.race}")
student = Student("Eunice",23)
student.greet()
student.introduction()
student.origin("African descent")
print(student.school)
print(student.name)
print(student.age)
        