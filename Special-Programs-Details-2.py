# Factorial Program Using For Loop

number = int(input("Enter the Number for Factorial: "))
factorial = 1
for num in range(1,number+1):
    factorial *= num
print("The Factorial of {} is {}".format(number,factorial))

# Fibonacci Series With For Loop
# Fibonacci Series -> 0 1 1 2 3 5 8 13 21 34 55 ...
                    # 0+1 = 1 , 1+1 = 2 , 1+2 = 3
                    # 2+3 = 5 , 3+5 = 8 ....

terms = int(input("Enter No. of Terms: "))
first_term = 0
second_term = 1
for x in range(terms):
    if x <= 1:
        print(x , end = " ")
    else:
        next_term = first_term + second_term
        print(next_term, end = "\t") # To give more space between terms
                                     # use \t inside " " of end attribute .
        first_term = second_term
        second_term = next_term

# Star Pattern using For Loop

rows = int(input("\nEnter No. of rows: "))
for x in range(1,rows + 1):
    for y in range(1,x):
        print("*",end = " ")
    print()


# Converting Miles To Feets

def miles_to_feet(miles):
    if miles == 0:
        print("There are 0 feet in",miles,"miles")
    else:
        feet1 = miles * 5280
        print("There are",feet1,"feet in",miles,"miles.")
       
print(miles_to_feet(8))

# Finding Area Of Shapes

def area_trapezium():
    base1 = float(input("Enter the length of one of the bases: "))
    base2 = float(input("Enter the length of the other base: "))
    height = float(input("Enter the height:"))
    area = (1/2) * (base1 + base2) * height
    print("The area of a trapezoid with bases",base1,"and",base2,"and height",height,"is",area)
   
print(area_trapezium())

def area_triangle():
    """ computes area of triangle using Heron's formula. """
    side1 = float(input("Enter length of side one: "))
    side2 = float(input("Enter length of side two: "))
    side3 = float(input("Enter length of side three: "))
    s = .5*(side1 + side2 + side3)
    area = (s*(s-side1)*(s-side2)*(s-side3))**.5
    print("Area of a triangle with sides",a,b,c,"is",area)
    
print(area_triangle())

# Takes date of form mm/dd/yyyy and writes it in form June 17, 2016 

def date_display(month, day, year):
    months = ("January","February","March","April","May","June","July","August",
              "September","October","November","December")
    print(str(months[month - 1])+" "+str(day)+","+" "+str(year))
    
print(date_display(5 , 29, 2020))

# Takes date such as July 17, 2016 and write it as 7/17/2016 

def display_date(mon, day, year):
    months = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,
              "July":7,"August":8,"September":9,"October":10,"November":11,
              "December":12}
    print(str(months[mon])+"/"+str(day)+"/"+str(year))
    
print(display_date("May" , 29, 2020))

# Compute the mean and standard deviation of a list of floats 

import random
num_list = []
random.seed(150)
for i in range(0,25):
    num_list.append(round(100*random.random(),1)) 
def statistics_data(ran_list):
    import statistics
    print(statistics.mean(ran_list))
    print(statistics.stdev(ran_list))
    
print(statistics_data(num_list))
