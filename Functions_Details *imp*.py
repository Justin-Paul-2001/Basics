# Defining and Calling A Function:

def number_squared(number): # Defining A Function
                            # Note : Try always to return
                            # A value from the function instead
                            # of printing something

                            # Here 'number' is argument
    return number ** 2

print(number_squared(5)) # Calling the Function
                         # Here '5' is parameter
  
# Program For Default Parameter :

def getName(name = "JUSTIN"):
    return ("My Name is {}".format(name))

print(getName())    # If no Parameter is given then the default paramter
                    # is used.

print(getName("PAUL")) # When parameter is given then default parameter is
                       # overwritten by given argument.

# Finding The Hypotenuse of Right Angle Triangle:

def side_squared(side):
    return side ** 2

def hypotenuse_right_angle_traingle(base,perpendicular):
    return (side_squared(base) + side_squared(perpendicular))** .5

print(hypotenuse_right_angle_traingle(3,4))

# Program Using Arbitrary Argument:

# When we want to pass arguments as a list use {*arg_name}

def getName(*name):  # When we don't know number of
                     # arguments we use {*} before the
                     # argument and use indexing while
                     # writing the body of function.
    return ("The Name is " + name[2])

print(getName("Justin","Paul","Suja","Alan","Meressa","Seby","Swapna"))

# When we want to pass arguments as a dictionary use {**arg_name}

def getName1(**name):
    return ("The Name Is "+ name["name5"])

print(getName1(name1 = "Justin",name2 = "Paul",name3 = "Suja",name4 = "Alan",name5 = "Meressa",name6 = "Swapna"))
