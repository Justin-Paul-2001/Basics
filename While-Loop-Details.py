# while (condition):
    # body of loop
    # incrementation / decrementation

# 1.) Display Even Nos. upto 50

i = 0
while i <= 50:
    if i % 2 == 0:
        print(i,end = " ")
    i += 1

# 2.) Display Sum of odd numbers upto 50

i,sum_odd = 0,0
while i <= 50:
    if i % 2 == 1:
        sum_odd += i
    i += 1
print("\nSum of all odd numbers upto 50 is {} ".format(sum_odd))

# Usage of break and continue keywords

i = 0
while i <= 50:
    if i < 20:
        continue
    elif i > 45:
        break
    i += 1
    print ("\n",i,end = " ")

##### 3.) program to find out palindrome number #####

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
