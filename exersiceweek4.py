class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def introduce(self):
        print(f"Good Morning, My name is{self.name}. I am a {self.gender}.I am {self.age}years old")

name=input("Enter your Name:-")
age=int(input("Enter your age:-"))
gender=input("Enter your gender:-")
person1 =Person(name,age,gender)
person1.introduce()