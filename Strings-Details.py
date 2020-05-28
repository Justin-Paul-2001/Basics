a = " Hello, World "
print(a)

b = a.lower() # Making Each Character of the String to Lower Case
print(b) 

c = a.upper() # Making Each Character of the String to Lower Case
print(c)

d = len(a) # Total No. of Characters including the spaces present in string
print(d)

e = a.strip() # Removing the Extra Spaces at the Start and End of the String
print(e)
# For Removing spaces only at the start use .lstrip()
# For Removing spaces only at the end use .rstrip()

f = a.replace("l","p") # Replacing one Character with other -> Here { 'l' is replaced by 'p'}
print(f)
# This can also be used for removing all the spaces inside the string using -> .replace(" " , "")

g = a.split(",") # To break string and create a list of words using the point of breaking as comma {,} in this case
print(g)
# If the parameter is kept empty, then it would split in terms of spaces

h = a+" "+"I am Justin"
i = a+" "+str(1)+" is the smallest natural number"
print(h)
print(i)
# String Concatenation using only strings and also concatenating a integer with string.

j = "{} + {} = {}"
print(j.format(1,2,3)) # string formatting
