# Programs On Inheritance :

# Creating A Parent / Base Class ->

class Person:
    def __init__(self,name,address):
        self.name    = name
        self.address = address
    def show(self):
        print(f"Person is Called {self.name}, residing in {self.address}.")

# Creating An Object ->

Person_1 = Person("Allwyn","Jabalpur")
Person_1.show()

# Creating Derived / Child Classes ->

class Child(Person):
    pass # Keyword "pass" is used for Defining Empty Class.

class Teacher(Person):
    def __init__(self,name,address,salary):

        super().__init__(name,address) # super() function is used for 
                                       # Using same __init__ function
                                       # from Parent Class {here , Person}
        
        self.salary = salary
        
    def income(self,profession = "Teacher"):
        print(f"\n{self.name} is a {profession} Having A Salary Of Rs. {self.salary}/- per month.\n")
        
class Student(Person):
    def __init__(self,name,address,age,roll_number,standard,contact):

        super().__init__(name,address) # super() function is used for 
                                       # Using same __init__ function
                                       # from Parent Class {here , Person}
        
        self.roll_number = roll_number
        self.standard = standard
        self.contact = contact
        self.age = age
        
    def profile(self,profession = "Student"):
        print(f"\n{self.name} is a {profession}, aged {self.age} years old , having Roll-Number. {self.roll_number}.")
        print(f"\n{self.name} is studying in {self.standard} \nHaving Contact-Number. {self.contact}.")
        

# Creating Object Of Derived Class ->

Person_2 = Teacher("Rosy","Kolkata",50000)
Person_2.show()
Person_2.income()

Person_3 = Student("Justin","Pune",19,19130003,"1st B.Tech Mechatronics","******4075")
Person_3.show()
Person_3.profile()
