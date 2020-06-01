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
