# For loop iterating over a list

mylist1 = [1,2,3,4,5,6,7,8,9,10]
for num in mylist1:
    print(num, end = " ")

print("\n")

# For loop iterating over a string

mystr1 = "Hello How Are You?"
for char in mystr1:
    print(char, end = " ")

print("\n")

# Usage of break and continue

mylist2 = ["justin","paul","suja","alan","vincy","julie","seby","swapna","meressa"]
for name in mylist2:
    if name == "seby":
        break
    if name == "alan":
        continue
    print("\n")
    print(name)


print("\n")

# Using range in for loop

for num in range(1,11,3):
    print(num,end = " ")

for num1 in range(1,11):
    print("\n",num1,end = " ")

for num2 in range(10):
    print("\n",num2,end = " ")

# Usage of else statement in for loop

mylist3 = ["justin","paul","suja","alan","vincy","julie","seby","swapna","meressa"]
for name in mylist3:
    if name == "alan" or name == "suja" or name == "swapna":
        continue
    print("\n")
    print(name)
else:
    print("\n All names are displayed")

print("\n")

# Nested For Loop

list1 = [1,2,3,4,5,6]
for x in list1:
    for y in list1:
        print("[",x,"|",y,"]",end = " ")
    print("\n")
