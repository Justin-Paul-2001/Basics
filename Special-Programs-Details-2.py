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
