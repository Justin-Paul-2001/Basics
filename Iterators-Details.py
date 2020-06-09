# PROGRAMS BASED ON ITERATORS ->

# 1.) Tuple / List ->

cities = ("Pune","Mumbai","Delhi","Chennai","Goa","Kerala")

my_iter = iter(cities)

# No. Of Times next() function == No. of Elements in list/tuple {here, cities}

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# 2.) String ->

my_city = "Mumbai"

my_iter = iter(my_city)

# No. Of Times next() function == No. of Elements in string {here, my_city}

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# 3.) Loops ->

cities = ("Pune","Mumbai","Delhi","Chennai","Goa","Kerala")

for city in cities: # Here , 'city' is the iterator.
    print(city , end = " ")
print("\n")

# 4.) Class(OOP) ->

#1.)

class My_Number:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

object_1 = My_Number()

my_iter = iter(object_1)

# No. Of Times next() function == No. of Elements

print(next(my_iter)) # 1
print(next(my_iter)) # 2
print(next(my_iter)) # 3
print(next(my_iter)) # 4
print(next(my_iter)) # 5
print(next(my_iter)) # 6

# 2.)

class My_Number:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else :
            raise StopIteration # Special Method to Abandon Iteration.

object_1 = My_Number()

my_iter = iter(object_1)
for x in my_iter: # This Iteration By Default Calls next() Function.
    print(x)
