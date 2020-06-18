############

# NOTE : Create A file named "ReadOnlyFile.txt" preferably in your Directory of Programs
# Run The Below Line Of Code To Create A FIle Named "ReadOnlyFile.txt" . 
# file_1 = open("ReadOnlyFile.txt" , "x")

############

# open( file location , mode )
# modes -> "r" -> read mode {default mode}
         # "a" -> append mode (continuation of data entry)
         # "w" -> overwrite mode (editing data)
         # "x" -> create mode

# Opening File In Read Mode ->

file_1 = open("ReadOnlyFile.txt" , "r")

# Method 1 :- To Display File Contents

for line in file_1:
    print(line , end = " ")

file_1.close()
file_1 = open("ReadOnlyFile.txt" , "r")
    
print("\n\n")

print(file_1.read(5)) # 5 signifies no. of characters to be displayed.

file_1.close() # IMPORTANT : Remember To Close The File After use of file
file_1 = open("ReadOnlyFile.txt" , "r")

print(file_1.readline()) # .readline() will display first line of the file.

file_1.close()
file_1 = open("ReadOnlyFile.txt" , "r")

# Method 2 :- To Display File Contents

print(file_1.read())  # .read() displays the text inside a text file.

file_1.close()

# Opening File In Append Mode ->

file_1 = open("ReadOnlyFile.txt" , "a")
file_1.write("\nThis IS the Additional Content That is being written.")
file_1.close()

file_1 = open("ReadOnlyFile.txt" , "r")
print(file_1.read())
file_1.close()

# Opening File In OverWrite Mode ->

### NOTE : Using Overwrite Mode "w" , will delete the old contents of the file.

file_1 = open("ReadOnlyFile.txt" , "w")
file_1.write("This Is the Overwritten Information Content That is being written.")
file_1.close()

file_1 = open("ReadOnlyFile.txt" , "r")
print(file_1.read())
file_1.close()

# Opening File In Create Mode ->

### NOTE : Using Create Mode "x" , will create new in directory.

file_1 = open("ReadOnlyFile_New.txt" , "x") # The File Name In Create Should Be Name of New Created File.
file_1.write("This Is the NewFile Information Content")
file_1.close()

file_1 = open("ReadOnlyFile_New.txt" , "r")
print(file_1.read())
file_1.close()

# Removing A File ->

import os
os.remove("ReadOnlyFile_New.txt")
# NOTE : The File Created Using Create Mode is being Deleted in Above Line of Code.

# To Check Existance of A file ->

if os.path.exists("ReadOnlyFile.txt"):
    print("File Exists")
