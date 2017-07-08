r = range(0,100)
print (r)

for i in range(0,100)[::-2]:
	print (i)
print ("="*40)
for i in range(99,0,-2):
	print (i)

print ("="*40)

print (range(0,100)[::-2]==range(99,0,-2))

# sets are collection of dictionary keys and set members are hashed. elements in the set must be immutable. 

even = set(range(0,40,2))
print even
square_tuple = (4,9,16,25)
squares = set(square_tuple)
print squares
print len(even)
print len(squares)
union = even.union(squares)
print len(union)
union1 = squares.union(even)
print len(union1)

intersection = even.intersection(squares)
print len(intersection)

print even & squares
differ = even.difference(squares)
print sorted(differ)
print squares.discard(4)
print squares.remove(16)
print squares

even = set(range(0,40,2))
square_tuple = (4,9,16,25)
squares = set(square_tuple)
if squares.issubset(even):
	print ("square is a subset of even")
else:
	print ("hello")
if squares.issuperset(even):
	print ("square is a subset of even")
else:
	print ("hello")

#Functions: formally function is a useful device that groups together a set of structures. So, they can be run in more than once.
# They can also let us specify parameters that can serve as input to functions. on a more fundamental level, functions allow us 
# not to have repeatedly write the same code again and again. So, we have used the function 'len' to get the length of string.
# since checking the length of the sequence is common task so we can repeatedly do this method in order to write the statement again and
#again. def is the built in keyword telling python that you are about to create function. some of the built in keywords are abs(),
# all(), bin(), bool(), dict(), sum(), str(), int(),sorted(),print(),issubclass(),issuperclass(),enumerate() etc.
# How to define and call a Function?
#


def sayHello():
	print "Hello world"

sayHello()

#Function with arguments and parameter:


def sayHello1(myname):
	print "Hello " + myname
sayHello1("Ganesh")



# Function with default argument or parameters

def sayHello2(myname="Dear customer "):
	print "Hello " + myname

sayHello2()

#using language defined identifier in function:

def sayhello4(myname="Dear Customer"):
"This is documentation example"
	print "Hello " + myname


print sayhello4.__doc__
# Retaining values: 

def sum_parameters(arg1,arg2):
	result = arg1 - arg2
	return result

summation = sum_parameters(2,5)
print summation



































































































