# Write a Python program which accepts a sequence of comma-separated 
# numbers from user and generate a list and a tuple with those numbers.
values = input("Input some comma seprated numbers : ")
l = values.split(",")
a = list(values)
t = tuple(l)
print('List : ',l)
print('Tuple : ',t)
# xato ishladi
print(f'Other list {a}')
print('List : ',a)



number=input("Enter numbers separated by a comma:").split(',')
a=list(number)
b=tuple(a)
print ("Your list is: ", a, "\n" ,"Your tuple is:", b)