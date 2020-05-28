myset = {1,2,3,4,5,6,7,8,9,1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,6,6,7,7,7}

print(myset) # no duplicate values will be printed

print(6 in myset)

myset.add(10) # adding single element in sets
print(myset)

myset.update([11,12,13,14,15]) #adding multiple elements in sets
print(myset)

print(len(myset)) # Note : returns no. of unique elements inside set.

myset.remove(6)
print(myset)

myset.discard(9) # if in case element that is being discarded isn't present
                 # still .discard() won't throw a error/traceback.
print(myset)

myset.clear() # Empties a Set 
print(myset)

del myset

x = {1,2,3,4,5}
y = {6,7,8,9,10}
z = x.union(y) # Joining Two Sets
print(z)
