# Program On Factorial Of A Number using Recursion :

number = int(input("Enter the number whose Factorial is needed : "))
fact_num = 1
def factorial_number(num):
    if num <= 1:
        return num
    else:
        fact_num = num * factorial_number(num - 1)
    return fact_num

print(factorial_number(number))

# Program On Fibonacci Series Using Recursion :

terms = int(input("Enter number of terms of Fibonacci Series : "))
def fibonacci_series(term):
    if term <= 1:
        return term
    else:
        return fibonacci_series(term - 1) + fibonacci_series(term - 2)
    
for i in range(terms):
    print(fibonacci_series(i))
    
# Program on Armstrong Number for Recursion :

# Armstrong Number : Number whose sum of cube of each digit is equal
#                    to the original number.
# Example : 153 -> 1^3 + 5^3 + 3^3
        #       =  153
# Some Other Armstrong Nos. -> 407 , 370 , 371 ....  

number = int(input("Enter the number to check if it is Armstrong : "))
original_number = number
sum_of_digit = 0

def is_armstrong(number):
    global sum_of_digit # It is stating that a variable defined outside the
                        # Function is to be used.
    if number > 0:
        remainder = number % 10
        sum_of_digit += remainder ** 3
        number = is_armstrong(number // 10) # Recursion is occuring here.
    return sum_of_digit

new_number = is_armstrong(number)
if original_number == new_number:
    print("{} is a Armstrong Number. ".format(original_number))
else:
    print("{} is not a Armstrong Number. ".format(original_number))

# Program for Palindrome Number Using Recursion:

# Number which Reamins the Same when Digits are reversed in order.
# Example -> 121 , 12321 , 24542

number = int(input("Enter the number to check if it is Palindrome : "))
original_number = number
sum_of_digit = 0

def is_palindrome(number):
    global sum_of_digit # It is stating that a variable defined outside the
                        # Function is to be used.
    if number > 0:
        remainder = number % 10
        sum_of_digit = sum_of_digit * 10 + remainder # Logic Of Palindrome Program
        
        number = is_palindrome(number // 10) # Recursion is occuring here.
    return sum_of_digit

new_number = is_palindrome(number)
if original_number == new_number:
    print("{} is a Palindrome Number. ".format(original_number))
else:
    print("{} is not a Palindrome Number. ".format(original_number))

# Program For Prime Number Using Recursion :

number = int(input("Enter the number to check if it Prime Number : "))
def is_prime(number , i = 2):
    if number <= 2:
        return True if number == 2 else False
    if number % i == 0: # To Check If Number Gets divided By Any Number
        return False
    if i * i > number :
        return True
    return is_prime(number , i + 1) # Recursion Will Occur Here As This Will
                                    # Keep Running till it Checks For All Number
                                    # Dividing Original Number upto SQRT(original number)
                                    # And Finds Prime or not.

if  is_prime(number):
    print("{} is a Prime Number".format(number))
else:
    print("{} is not a Prime Number".format(number))
