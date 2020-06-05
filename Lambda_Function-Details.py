# Use Of Lambda Function

x = lambda a : a + 10 # Here the Function is saved in Variable x
                      # Argument is {a} and Expression is {a + 10}
print(x(7))

y = lambda a,b : a * b # Here the Function is saved in Variable y
                       # Argument is {a , b} and Expression is {a * b}
print(y(8,12))

# Program on Armstrong Number Using Lambda Function ->

z = lambda digits : digits ** 3
number = int(input("Enter A Number : "))
original_number = number
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += z(digit)
    number = number // 10
if sum_of_digits == original_number :
    print("{} is a armstrong number".format(original_number))
else:
    print("{} is not a armstrong number".format(original_number))
    
# Using Lambda Function inside Another Function :

def show_data(n):
    return lambda a : a * n

new_function = show_data(2) # Here inside new_function the lambda function is
                            # saved as lambda a : a * 2 bcoz. n = 2

print(new_function(12)) # Now the Lambda function is executed that is stored inside
                        # new_function.

# Program to Write Table of Number :

def table_of_number(number):
    return lambda a : a * number

number = int(input("Enter the Number whose Table is Required : "))
table = table_of_number(number) # The lambda function is stored in 'table' variable.

for i in range(1,11):
    print(number,"x",i,"=",table(i)) # NOTE : 'table' variable contains the lambda function. 
                       
