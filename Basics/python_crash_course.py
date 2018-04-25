# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 09:35:15 2018

@author: aniketsha
"""

# Data Types

# Integer
i = 1
print (i, type(i))
## 1 <class 'int'>


# Float
i = 0.5
print (i, type(i))
## 0.5 <class 'float'>


# Exponent 
i = 2 ** 4
print(i)
## 16


# Python follows the orders of operations
i = 2 + 3 * 5 + 5
print(i)
## 22


# mod functionality
i = 4 % 2
print(i)
## 0
i = 5 % 2
## 1


# Variable names shouldn't start with numbers and special characters
#pass variable names in strings
age = 15
name = 'Sam'
detail = 'My name is {} and my age is {}'.format(name, age)
print (detail)
## My name is Sam and my age is 15


# String
var = 'abcdefghijk'
print (var[0])
## a
print (var[0:3])
## abc
print (var[3:6])
## def


# List
my_list = ['a','b','c',1,2,3]
print(my_list)
##['a', 'b', 'c', 1, 2, 3]
print (my_list[0])
## a
print (my_list[1:3])
## ['b', 'c']
my_list[0] = 'new'
print(my_list)
## ['new', 'b', 'c', 1, 2, 3]
nest = [1,2,[3,4]]
print (nest[2][1])
## 4
nest = [1,2,[3,4,['target']]]
print (nest[2][2][0])
## target
#nest.pop(), nest.append()
#'x' in [1,2,3] ==> False
#'x' in ['x','y','z'] ==> True

# Dictionary- Doesn't follow any sequence, only key value pairs
d = {'key1':'value1', 'key2':123}
print (d['key1'])
## value1
d = {'key1':[1,2,3]}
print(d['key1'][0:2])
## [1, 2]
d = {'key1':{'innerkey1':[1,2,3,4],'innerkey2':['target']}}
print (d['key1']['innerkey2'][0])
## target
#d.values(), d.keys(), d.items()


# Tuple are immutable i.e. you can't change or reassign the existing value unlike we can do it in list.Lists are mutable
t = (1,2,3,4,5)
print (t[0:3])
## (1,2,3)
t[0] = 'new'
## TypeError: 'tuple' object does not support item assignment


# Sets : Collection of unique elements 
s = {1,2,3,4}
print (s)
## {1, 2, 3, 4}
s = {1,1,1,2,3,3,3,4,4}
print (s)
## {1, 2, 3, 4}
s = set([1,2,3,3,4,4,5])
print(s)
## {1, 2, 3, 4, 5}
s.add(6)
print (s)
## {1, 2, 3, 4, 5, 6}
s.add(6)
print (s)
##{1, 2, 3, 4, 5, 6}


#Logical and comparison operators
l = 1 < 2 and 2 < 3
print (l)
## True
l = 1 < 2 or 2 > 3
print (l)
## True


# If conditions
if 1 == 2:
    print('First')
elif 2 == 2:
    print('Middle')
else:
    print('Last')
## Middle
    

# for loop
name_list = ['a','b','c','d']
for name in name_list:
    print ('Hello, {}'.format(name))
'''
Hello, a
Hello, b
Hello, c
Hello, d
'''

## While loop
i = 1
while (i < 5):
    print (i)
    i = i + 1
'''
1
2
3
4
'''

# Range Function
for i in range(0,5):
    print (i)
'''
0
1
2
3
4
'''
l = list(range(0,10,2))
print (l)
##[0, 2, 4, 6, 8]


# List comprehension
# *function* for x in *iterable*
sq_l = [num**2 for num in l]
print (sq_l)
## [0, 4, 16, 36, 64]


# Functions
def myFunc(param1):
    print ('Hello ' + param1)
myFunc('Sam')
## Hello Sam
def myFunc2(name='Jerry'):
    print('Hello ' + name)
myFunc2()
myFunc2('Tom')
myFunc2(name='Spiderman')
'''
Hello Jerry
Hello Tom
Hello Spiderman
'''

#  map(): if we want to apply certain function to every element of the iterable
def times(var):
    return var * 5
seq = [1,2,3,4,5,6]
times_list = list(map(times, seq))
print (times_list)
## [5, 10, 15, 20, 25, 30]


# lambda function
lam_list = list(map((lambda num : num*3), seq))
print (lam_list)
## [3, 6, 9, 12, 15, 18]


# filter function
fil_list = list(filter((lambda num : num%2 == 0), times_list))
print (fil_list)
## [10, 20, 30]


# String functions
s = 'My name is Sam'
print (s.lower())
## my name is sam
print (s.upper())
## MY NAME IS SAM
print (s.split(' '))
## ['My', 'name', 'is', 'Sam']

