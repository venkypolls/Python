import os
import sys
import random

'''dictionaries'''
employee = {'name':'anna',
            'age':'28',
            'designation':'developer',
            'works_with':['venky','niki']}

print(employee)
#prints all the keys of a dictionary
print(employee.keys())
#prints all the values of the dictionary
print(employee.values())
#deletes the mentioned key-value from the dictionary
del employee['age']
print(employee)
#adds or edits a dictionary key-value
employee['age'] = 30
#prints the length of the dictionary
print(len(employee))
#another way to get a key-value of a dictionary
print(employee.get('works_with'))

'''condtionals'''
c=10
a=8
b=7
#if condition with usage of (and,or) having a semi-colon after the if condition
if((a>=b and a>0)or(c>b and c>0)):
    print('condition true')
#if elif and usage of not
if(a>10):
    print('a')
elif b>10:
    print('b')
elif not(c>10):
    print('c')
'''for loops'''
#for loop syntax in python iterating over a range of 10 from 0 upto 10
for x in range(0,10):
    print(x,end=" ")
print('\n')
#for loop syntax in python iterating over a list of items
for x in [2,5,3,6,8,5]:
    print(x,end=' ')
print('\n')
#for loop iterating over list of lists
num_lists = [[1,2,3,4],[11,22,33,44]]
for x in num_lists:
    for y in x:
        print(y,end=" ")
    print('\n')

'''while loop'''
rand = random.randrange(0,10)
#while is used when limit of iteration is not known
#basic while syntax runs until the random number ain't 5
while (rand!=5):
    print(rand)
    rand = random.randrange(0,10)
#while loop with if elif etc and continue and break
count=0
while count<=20:
    if(count%2 == 0):
        print(count,end=" ")
    elif (count==15):
        break #breaks from the loop itself
    else :
        count+=1
        continue  #does not execute anything after this statement for that iteration
    count+=1

