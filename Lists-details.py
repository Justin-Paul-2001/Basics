mylist = [1,2,3,4,5.6,7.8,True,False,"hello","world"]

# indexing starts from 0.
print(mylist[0]) #first element
print(mylist[-1]) #last element
print(mylist[1:8]) #Slicing of list
print(mylist[2:]) #second parameter is empty means it will print
                  #all elements till the end.
print(mylist[:9]) #first paramter is empty means it starts from
                  #first element -> index[0]
print(mylist[-8:-1])
print(mylist[-10:-1:2]) #Striding of list
print(mylist[1:10:2]) # third parameter is the increment
print(mylist[::-1]) #reverse of list
mylist[8] = "Justin" #changing element
print(mylist)
print(len(mylist)) #no. of elements of list.
mylist.append("Paul") #adding element at end of list
print(mylist)
mylist.insert(3,4.5) # adding element at specified index
print(mylist)
mylist.remove("world") #removes specified element
mylist.pop(7) #removes element at specified index , if
              #no parameter is given it removes last element.
print(mylist)
mylist.clear() # empties a list
print(mylist)
del mylist #complete list is deleted.


a = [1,2,3,4,5]
b = [6,7,8,9,10]
mylist2 = a + b #list concatenation
print(mylist2)
a.extend(b) # appends list (a) with elements of list (b)
print(a)
