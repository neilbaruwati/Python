"""

#Advanced function
# Map is an advanced function which needs your function,seq as an attribute to define


def fahrenheit(t):
	return 9.0/5*t +32
t = [0,22.5,6,72,50]
print map(fahrenheit,t)

temp = [0,22.5,6,72,50]
print map(lambda t:9.0/5*t+32, temp)

a = [1,2,3]
b = [3,4,5]
c = [5,6,7]
print map(lambda x,y:x+y,a,b)
print map(lambda x,y,z:x+y+z,a,b,c)
print map(lambda num:num*-1,a)

# Reduce: it continuously apply function to the seq.

list = [47,11,42,73]
print reduce(lambda x,y:x+y,list)

max_find = lambda a,b:a if a>b else b

print reduce(max_find,list)

def even_check(num):
	if num%2==0:
		return True
	else:
		return False

print even_check(35)

list = range(10)

print filter(even_check,list)
items = ["mic","phone",323.3, 2,4,"Justin"]
def parse_lists(abc):
	str_list_items = []
	num_list_items = []
	for i in abc:
		if isinstance(i,float) or isinstance(i,int):
			num_list_items.append(i)
		elif isinstance(i,str):
			str_list_items.append(i)
		else:
			pass
	return str_list_items,num_list_items
print parse_lists(items)

def my_sum(my_num_list):
	total = 0
	for i in my_num_list:
		if isinstance(i,float) or isinstance(i,int):
			total +=i
	return total

print my_sum(items)

def main():
	f = open("guru.txt","w+")
	for i in range(10):
		f.write("This is line %d \n"%(i+1))
	f.close()

main()

def main():
	f = open("guru.txt","a+")
	for i in range(10):
		f.write("This is line %d appended \n"%(i+1))
	f.close()

main()

def main():
	f = open("guru.txt","r")
	if f.mode =='r':
		contents = f.read()
	print contents

main()
"""
def main():
	f = open("guru.txt","r")
	f1 = f.readline()
	for x in f1:
		print x

main()

































