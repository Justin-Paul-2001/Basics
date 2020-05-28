number = int(input("Enter a number: "))
if number % 2 == 0:
    print("{} is a even number".format(number))
else:
    print("{} is a odd number".format(number))

# Positive / Negative or Number -> Zero

number1 = int(input("Enter a number: "))
if number1 > 0:
    print("{} is a positive number".format(number1))
elif number1 < 0:
    print("{} is a negative number".format(number1))
else :
    print("You Have Entered Zero")

# Greatest of Three Numbers

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a > b and a > c:
    print("{} is largest number of the three numbers".format(a))
elif b > a and b > c:
    print("{} is largest number of the three numbers".format(b))
else:
    print("{} is largest number of the three numbers".format(c))
    
# Nested If ->

x = int(input("Enter A Number: "))

if x > 10:
    print("{} is greater than 10".format(x))
    if x > 20:
        print("{} is greater than 20".format(x))
    else:
        print("{} is less than 20".format(x))
else:
    print("{} is less than 10".format(x))
