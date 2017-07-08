#More about Functions
"""
def my_first(x,y):
	print "hello " + str(x)
	print "hello " + str(y)


my_first("python","java")
my_first(3,4)
my_first(10,5.2)

def my_first1(num):
	sum = num**2
	return sum
print my_first1(5)

def my_first2(x,y,z):
	sum = (x+y)*z
	return sum **2

print my_first2(3,4,5)
square = lambda num:num**2
print square(10)

summation = lambda arg1,arg2:arg1+arg2
print summation(10,10)

# Lambda expression allows us to create annonymous function. This basically means we can create adhoc functions without
# needing to properly define a function using def. Lambda body is a single statement and not a block of statements.
#Lambda body is similar to what we would put in a def body. Def body return statement. Lambda function is used to limit program nesting.
#def handles larger task whereas lambda is designed for coding simple.

even = lambda num:num%2==0
print even(40)


first = lambda s:s[0]
print first('hello')

first = lambda s:s[::-1]
print first('hello')

len_check = lambda item:len(item)
print len_check ("How many character does this string have?")


#Nesting statements and scope:

x = 25 #Global variable
def pointer():
	x = 50 #local variable
	return x
print x
print pointer()

# this is where scope comes in. python deals with variable name you assigned. when you create a variable in python, the name is stored in a
# namespace. The variable name is also have a scope. The scope determines the visibility to other parts of the code.
#naming assignments: Naming assignments will create or change local names by default. Name references 4 scopes: local, enclosing function,
# global, builtin.
# local is nothing but the names assigned in any way within a function are not declared global in the function.
#enclosing function locals: the name in the local scope of any and all enclosing function from inner to outer.
#Global: name assigned to the top level of your module file or declared global in def within a function.
#Builtin variable: name preassigned builtin name modules such as open,range.

f = lambda x:x+2
print f(5)

name = "This is a global name"
def greet():
	name = "sunny"
	def hello():
		print "hello " +name
	hello()
greet()
print name
x = 50
def func():
	global x
	print "This is now using the global x!"
	print 'because of global x, ',x

	x = 2
	print "Random() changed global x to ",x
func()
print 'value of x continue of func() is: ',x


s = "Hello, how are you"
t = "My name is tom"

def up_low(s):
	d = {"upper":0,"lower":0}

	for c in s:
		if c.isupper():
			d["upper"]+=1
		elif c.islower():
			d["lower"]+=1
		else:
			pass
	print "The original string is: ",s
	print "The number of uppercase character are ",d["upper"]
	print "The number of lowercase character are ",d["lower"]

up_low(t)

def unique_list(l):
	x =[]
	for a in l:
		if a not in x:
			x.append(a)
	return x

print unique_list([1,3,4,4,5,6,6,5])

"""


def convertTemp(temp,scale):
	if scale =="c":
		return (temp-32.0)*(5.0/9.0)
	elif scale == "f":
		return temp*(9.0/5.0)+32

temp = int(input("Enter the temperature: "))
scale = raw_input("Enter the scale to convert to: ")
converted = convertTemp(temp,scale)
print "The converted temp is" + str(converted)













































































































































