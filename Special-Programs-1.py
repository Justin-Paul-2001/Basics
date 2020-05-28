# Armstrong Number Program
# 407 = 4^3 + 0^3 + 7^3
    # = 407

a = int(input("Enter A Number : "))
b = a
sum_digits_cube = 0
while a != 0:
    digit = a % 10
    sum_digits_cube += digit**3
    a //= 10

if b == sum_digits_cube :
    print("{} is a Armstrong Number".format(b))
else :
    print("{} is not a Armstrong Number".format(b))

# Factorial of A Number
# 5! = 5 x 4 x 3 x 2 x 1
#    = 120

c = int(input("Enter A Number : "))
d = c
factorial = 1
if c < 0:
    print("Factorial of {} is not defined.".format(c))
elif c == 0:
    print("Factorial of 0 is 1")
else:
    while c > 1:
        factorial *= c
        c -= 1
    print("Factorial of {} is {}.".format(d,factorial))
if d == 1:
    print("Factorial of {} is 1.".format(c))

##### Program to find out palindrome number #####

# Palindrome Number -> Number which Remains the Same Even if order of digits is
# reversed . eg. 121 , 1348431

a = int(input("Enter a number : "))
b = a
sum_nos = 0
while a != 0:
    remainder = a % 10
    sum_nos = sum_nos * 10 + r
    a //= 10

if b == sum_nos:
    print("\n{} is a palindrome no.".format(b))
else:
    print("\n{} is not a palindrome no.".format(b))

# Usage of Else statement along with While loop 

e = int(input("Enter A Number : "))
limit = int(input("Enter A limit : "))
while e > limit:
    print(e,end = " ")
    e -= 1
else:
    print("\nValue has Become Less than the defined limit")
