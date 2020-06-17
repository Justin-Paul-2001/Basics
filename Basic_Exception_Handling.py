# Exception Handling Programs ->

# 1.) Basic Error Handling :-

x = input("Enter Something In Numbers: ")
try:
    x = int(x)
except:
    print("Exception has occured")
    
# 2.) Using Error - Specific Handling And Use else Statement:-

try:
    print(a)         # Exception {NameError} will exceute.
    #print("Welcome") # Else Part Will be Exceuted.
except NameError:
    print("When Variable Is Not Defined , Then NameError Occurs.")
else:
    print("No Errors Are Present.")

# 3.) Using Try-Except-Else Statements :-
try:
    print(c)
except:
    print("Inialize the Variable!!!")
else:
    print("No Errors Are Present.")

# 4.) Using Try-Except-Finally Statements :-

try:
    print(b)
except:
    print("NameError Has Occured.")
finally:
    print("Try And Except Exceution has been Done.")

# 5.) File-Handling Exception :-

try:
    file = open("ReadOnlyFile.txt")
    file.write("Content is To Be written In read-only file")
except:
    print("Error : Default Opening of file will open read-only file mode.")
finally:
    file.close()
    print("Please Add the write mode parameter in .open() code.")

# 6.) Raising An Exception :-

x = 10
if x > 0:
    raise Exception("Variable Holds A Non-Negative Number.")

## NOTE : Comment the first error thrown to see the below error exceution.

y = "We are the Best"
if not type(y) is int:
    raise Exception("TypeError : Required A Integer, Got A String In Variable.")
