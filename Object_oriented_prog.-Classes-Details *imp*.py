# OOP Programs ->

# 1. Creating a Basic Class ->
class Person:
    age = 23

# Creating an Object Of the Defined Class ->
man = Person()
print(man.age)

# 2. Creating a  Class ->
class Personal_Data:
    def __init__(self , name , age , gender):
        self.name   = name
        self.age    = age
        self.gender = gender

# Creating an Object Of the Defined Class ->
person_1 = Personal_Data("Justin",19,"Male")
print("Name:",person_1.name)
print("Age:",person_1.age)
print("Gender:",person_1.gender)

# 3. Creating a  Class ->
class Personal_Data:
    def __init__(self , name , age , gender):
        self.name   = name
        self.age    = age
        self.gender = gender
    def show(self):
        return ("My Name is {}. I am {} years old. I am a {}.".format(self.name,self.age,self.gender))

# Creating an Object Of the Defined Class ->
person_2 = Personal_Data("Justin",19,"Boy")
print(person_2.show())

person_3 = Personal_Data("Alan",19,"Boy")
person_3.age = 14 # Changing Values of Defined Variables After Initialising.
print(person_3.show())

del person_3 # Deleting of An Object.

# 1.) Basic Program ->

class Employee:
    def __init__(self,name,age,address,salary):
        self.name    = name
        self.age     = age
        self.address = address
        self.salary  = salary
    def show(self):
        print(f"Employee Name is {self.name} having Age {self.age} and resides in {self.address}.")
        commission = int((self.salary * 10) / 100)
        print(f"His Salary is {self.salary + commission}.")

name = input("Enter Your Name: ")
age  = int(input("Enter Your Age: "))
address = input("Enter Your Residential Address: ")
salary  = int(input("Enter Your Monthly Salary: "))

Employee_1 = Employee(name,age,address,salary)
Employee_1.show()

# 2.) Program To Perform Basic Mathematical Operations

class Math_Operations:
    def __init__(self,first_number,second_number):
        self.first_number = first_number
        self.second_number = second_number
    def addition(self):
        return self.first_number + self.second_number
    def subtraction(self):
        return self.first_number - self.second_number
    def multiplication(self):
        return self.first_number * self.second_number
    def floor_division(self):
        return self.first_number // self.second_number
    def division(self):
        return self.first_number / self.second_number
    def remainder(self):
        return self.first_number % self.second_number
    def power(self):
        return self.first_number ** self.second_number

choice = " "

while choice.lower != "q":
    print("Enter 1 for addition: ")
    print("Enter 2 for subtraction: ")
    print("Enter 3 for multiplication: ")
    print("Enter 4 for floor_division: ")
    print("Enter 5 for division: ")
    print("Enter 6 for remainder: ")
    print("Enter 7 for first_number raised to second_number: ")
    print("Enter q to Quit")
    choice = input("Enter Your Choice: ")

    if choice != "q":
        first_number  = int(input("Enter First Number: "))
        second_number = int(input("Enter Second Number: "))
    if choice == "1":
        object_any = Math_Operations(first_number,second_number)
        print(object_any.addition())
    elif choice == "2":
        object_any = Math_Operations(first_number,second_number)
        print(object_any.subtraction())
    elif choice == "3":
        object_any = Math_Operations(first_number,second_number)
        print(object_any.multiplication())
    elif choice == "4":
        object_any = Math_Operations(first_number,second_number)
        print(object_any.floor_division())
    elif choice == "5":
        object_any = Math_Operations(first_number,second_number)
        print(object_any.division())
    elif choice == "6":
        object_any = Math_Operations(first_number,second_number)
        print(object_any.remainder())
    elif choice == "7":
        object_any = Math_Operations(first_number,second_number)
        print(object_any.power())
    else:
        break
    
if choice == "q":
    print("Thanks For Enjoying Math Operations")
else:
    print("Your Choice is Incorrect!!")
    
# Program To Calculate Area/Perimeter Of Shapes :

# 1.) For Circle ->

import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius

# 2.) For Square ->

class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return (self.side ** 2)
    def perimeter(self):
        return 4 * self.side    
    
shape = input("Enter Name Of the Shape: ")

if shape.lower() == "circle":
    radius = int(input("Enter Radius of Circle: "))
    object_any = Circle(radius)
    print("Area = ",round(object_any.area(),2))
    print("Perimeter = ",round(object_any.perimeter(),2))
    
elif shape.lower() == "square":
    side = int(input("Enter Side of Square: "))
    object_any = Square(side)
    print("Area = ",round(object_any.area(),2))
    print("Perimeter = ",round(object_any.perimeter(),2))    
        
else:
    print("Shape Not Recognised!!")
