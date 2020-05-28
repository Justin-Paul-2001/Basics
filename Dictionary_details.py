mydict = {"Justin":3001,"Simson":3002,"Abhishek":3003,"Aditya":3004,"Ayaan":3005}

print(mydict["Simson"])
print(mydict.keys()) # returns a list containing dictionary keys
print(mydict.values()) # returns a list containing dictionary values
print(mydict.items()) # returns a (key , value) tuple of dictionary items.

# Keys can be changed ,although Values can be appended
# Keys are always immutable items like tuples, hence a list can't be a dictionary key.

mydict["Ayaan"] = 3008
print(mydict)

print(mydict.get("Aditya")) # to get value associated to a particular key.

print(len(mydict)) # to get number of key-value pairs

mydict["Basil"] = 3007 # define a new key-value pair it will append dictionary.
print(mydict)

mydict.pop("Abhishek") # to remove a key-value pair
print(mydict)
mydict.popitem()       # when no parameter is given -> .popitem()
                       # last key-value pair gets removed.
print(mydict)

del mydict

mydict1 = {"Justin":3001,"Simson":3002,"Abhishek":3003,"Aditya":3004,"Ayaan":3005}
mydict2 = {"Vimal":3006,"Evans":3007,"Raiyan":3008,"Imaad":3009}

mydict1.update(mydict2) # to merge values both dictionaries into the
                        # first dictionary -> here {mydict1}
print(mydict1)
