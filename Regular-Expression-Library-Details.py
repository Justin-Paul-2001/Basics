import re # Importing Regular Expression Library

# Opening The Text File
text_file = open(r"file-location\Regular_Expression_Sum.txt")

list_numbers = list()

for line in text_file:
    line = line.strip()
    numbers = re.findall('[0-9]+' , line)
    for num in numbers :
        num = int(num)
        list_numbers.append(num)

print(sum(list_numbers))
