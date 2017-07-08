# list comprehension: in addition to sequence operation on list methods, python includes more advanced operations called 
# list comprehension. list comprehension allows us to build a list using a different notation. you can think of it eventually
# a one line built of for loop within brackets.
list = []
for letter in "word":
	list.append(letter)
print list

l1 = [y for y in "word"]
print l1

list = [x**2 for x in range(0,11)]
print list


list2 = [number for number in range(11) if number%2==0]
print list2

list2 = []
for number in range(11):
	if number%2==0:
		list2.append(number)
print list2


for number in [0,1,2]:
	print number

for number in range(3):
	print number
print range(5)
list1 = range(10)
list1.append(6)
list1.remove(4)
list1.pop(7)
print list1

celsius = [0,10,20.2,30.5]
farenheit = [(temp*(9/5.0)+32) for temp in celsius]
print farenheit

import numpy as np
a = np.mat("1,3;1,-1")
print "The matrix coeffecient is: ", a
b = np.array([5,1])
print "the vector intercept is: " ,b
x = np.linalg.solve(a,b)
print "The solution of the 2 equations is" ,x
print x[0]**2 +x[1]**2


list = [x**2 for x in [x**2 for x in range(11)]]
print list

#Iterators: It is an object that represents the stream of data and the elements at a time. Any objects that supports iteration is called
#iterable. Strings and list are iterable.
string = "0123456789"
for char in string:
	print char
my_iter = iter(string)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)

my_list = ["mon","tue","wed","thur","fri","sat","sun"]
my_iter = iter(my_list)
for i in range(0,len(my_list)):
	next_item = next(my_iter)
	print next_item

#Ranges: in python3 it is built in types. in python2 it is implemented as function.

my_list = list(range(10))
print (my_list)

print (range(10))

even = list(range(0,10,3))
odd = list(range(1,10,3))
print even,odd

my_string = "abcdefghijklmnopqrstuvwxyz"
print my_string.index('e')
print my_string[4]

decimals = range(0,10)
print decimals[4]

odd = range(1,10000,2)
print odd[985]

sevens = range(7,1000000,7)
x = input("please enter the number less than 1 million")
if x in sevens:
	print "{0} is divisible by seven".format(x)
else:
	print "{0} is not divisible by seven".format(x)

decimals = range(0,100)
print decimals

my_decimals = decimals[3:40:3]
print my_decimals


for i in range(3,40,3):
	print i
print my_decimals == range(3,40,3)




























































































