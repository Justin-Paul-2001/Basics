mytuple = (1,2,3,4,5.6,7.8,True,False,"Justin","Paul")
print(mytuple[0]) # First Element
print(mytuple[-1]) # Last Element
print(mytuple[2:9]) # Slicing
print(mytuple[-9:-2])
print(mytuple[3:])
print(mytuple[:8])
print(mytuple[-9:-1:2]) # Striding
print(mytuple[1:10:3])
print(mytuple[::-1]) # Reverse Dispalying of Tuple

# Tuples are Immutable and .append() , .remove() etc. can't be used.
# Then to edit the tuple -> The Methodology can be implemented as follows -

mylist = list(mytuple)
mylist[1] = 2.3
mytuple = tuple(mylist)
print(mytuple)

#########################

print(len(mytuple)) # No. of elements   

del mytuple

mytuple2 = (1,) # add a comma ( ,) at the end of a single element tuple.
print(mytuple2)

a = ("a","b","c",1,2,3,4,5)
b = (6,7,8,9,10,"d","e","f")
c = a + b #concatenation of tuples
print(c) 
