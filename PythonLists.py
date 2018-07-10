import os
import random
import sys

'''lists'''
#setting values to a list
fruits = ['orange','banana','mango','mango']
#printing first value
print(fruits[0])
#printing values from 0th index upto 2nd index excluding the 2ndth index values
print(fruits[0:2])
#forming another list and appending it to grocery list forming one list having two internal lists
vegetables = ['onion','potato']
grocery = [fruits,vegetables]
print(grocery[0][1])

#append for a list
fruits.append('apple')
print(fruits[3])
#insert value at required index other elements to the right of the inserted element move a step to the right
fruits.insert(1,'berrys')
print(fruits)
#remove a value from the list only one
fruits.remove('mango')
print(fruits)
#sorts the values in the list
fruits.sort()
print(fruits)
#reverse sorts the values in the list (descending order)
fruits.reverse()
print(fruits)
#deletes a value in the list at the specified index
del fruits[2]
print(fruits)
#appending vegetables and fruits lists to form a bigger list
groceryList = vegetables+fruits
print(groceryList)
#gives u the length values and max,min values of the lists
print(len(groceryList))
print(min(groceryList))
print(max(groceryList))


'''tuples - unlike lists tuples cannot be changed after it is created'''
#initiating a tuple
tuples = (1,2,5,4)
#tuple to list conversion
lists = list(tuples)
#list to tuple conversion
new_tuple = tuple(lists)
len(tuples)
max(tuples)
min(tuples)
print(tuples)