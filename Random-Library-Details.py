""" Make a list of 10 random reals between 30 and 35 using random library """

def random_library():
    import random
    random.seed(70)
    d = []
    for i in range(10):
        a = random.random()
        b = 5*a
        c = 30+b
        d.append(c)
    print(d)
    
print(random_library())
