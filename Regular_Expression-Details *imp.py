import re

text = "Hello how are you? I am Justin from Pune studying Mechatronics from Chennai"

string_match = re.search("^Hello.*ai$",text)
string_match_2 = re.search("\s",text)
print("The First occurence of Blank Space is ",string_match_2.start())


# .start() returns first occurence.

#  ^  -> Starting with.
#  .  -> Any Characters can follow.
#  *  -> Atleast one or more occurence.
#  $  -> Ending with.
#  \s -> White Space.

if string_match :
    print("Match Found!!")
else:
    print("No Match.")


list_match_found = re.findall("from",text)
list_match_found_2 = re.findall("not",text)
print(list_match_found)
print(list_match_found_2)

# .findall( ) -> returns a list of all matches.

# Use of Split() method of re ->

split_string_list = re.split("\s",text)
print(split_string_list)

# Counter Usage - (third Paramter of .split( ) method of re .)

split_string_list_1 = re.split("\s",text,3) # 3 signifies return string upto first 3 occurences.
                                            # as words and remaining as a single entity.
print(split_string_list_1)

# Use of sub() method of re ->
# It replaces the matches with the user text.

user_changed_string = re.sub("\s","_",text)
print(user_changed_string)

# Use of group() method of re ->

grouped_string = re.search(r"\bJ\w+",text)

# \b   -> Beginning tag for start of word
# \w+  -> Ending tag for word
# r    -> read string command.

print(grouped_string.group())
