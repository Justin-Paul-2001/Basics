# Programs To Find Date ->

# 1.) Current Date ->

import datetime as dt

current_date = dt.datetime.now()
print(current_date)

# 2.) Year-Month-Weekday ->

date_info = dt.datetime.now()

print(date_info.year) # Returns The Year 
print(date_info.strftime("%a")) # Returns The Weekday
                                # %a -> short form of weekday {fri -> Friday}
                                # %A -> full form of Weekday

print(date_info.strftime("%b")) # %b or %h -> short form of Month
                        
print(date_info.strftime("%c")) # %c -> Day_of_week-Date-Time 

print(date_info.strftime("%d")) # %d -> Day of the Month {12th or 3rd}

print(date_info.strftime("%m")) # %m -> Month of the Year -> {June -> 06}

print(date_info.strftime("%Y")) # %y -> last 2 digits of year
                                # %Y -> Complete year.

print(date_info.strftime("%p")) # %p -> returns AM or PM

print(date_info.strftime("%H")) # %H -> Capital H - returns hours

print(date_info.strftime("%M")) # %M -> Capital M - returns minutes

print(date_info.strftime("%S")) # %S -> Capital S - returns seconds

print(date_info.strftime("%I")) # %I -> Capital I - returns hours in 12 hours format

# Creating Own Date / Custom Date ->

cust_date = dt.datetime(2020,6,15,12,36,28)
# dt.datetime(yyyy,month,day,hours,minutes,seconds)

print(cust_date)

# Exploring Strftime() Function On Custom Date ->

explore_func_1 = dt.datetime(2120,8,18,12,36,48)

print(explore_func_1.strftime("%Y"))
print(explore_func_1.strftime("%p")) # %p -> returns AM or PM
