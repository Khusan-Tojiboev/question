# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
# berilgan oy va yil bo'yicha kalendarni ekranga chiqarish
# birinchi yil bilan oy ni user dan olish kerak 
# so'ng calendar modulni ishlatishni bilish kerak
# keyin ekranga chiqarish kerak 

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))



import calendar
the_date = input("Please enter a month and a year separated by a comma: ")
date_list = the_date.split(",")
my_month = int(date_list[0])
my_year = int(date_list[1])

print(calendar.month(my_month, my_year))