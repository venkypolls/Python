import random
import os
import sys

# comment

# use single or double quote it is the same in python
print('hey hi!')
print("hello hi!")

'''multi line
comment'''

# variable can store any value no data type to be specified
# 5 data types are strings,numbers,tuples,dictionaries,lists

variable = 'hey'

# the variable can be assigned to a number later as well
variable = 15
# result - 15
print(variable)

# arithmetic operators **(exponent) //(floor division ignores remainder)
# result - 3
print(20//6)
# result - 8
print(2**3)

# arithmetic follows BODMAS rule of computing
# print can have any number of values printed which can be specified one after the other followed by a comma
print('cost of 10 loafs of bread -',2*10-5 )
print('cost of','a few chocolates -', 2*(10-5))

# quote in a string use backslash
str1 ="\"The Great Bandit\""
# multi line string
str2 = '''hey what's up i'm in the
 2nd line right now beautiful right!'''
# use %s in print to print string
print("%s %s" %(str1,str2))
# even str1 + str2 can be used

# print string 5 times
print('hey\n' * 5)

# don't end print of a string with new line
print('no new line after this print ',end="")
print('check this out!!')
