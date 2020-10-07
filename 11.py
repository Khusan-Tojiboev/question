# Write a Python program to print the documents (syntax, description etc.)
# of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

print(abs.__doc__)

'''
https://www.geeksforgeeks.org/python-docstrings/
'''

import builtins

fun = input("Enter the function of which you want to check description:")
my_str = getattr(builtins, fun)
print(my_str.__doc__)