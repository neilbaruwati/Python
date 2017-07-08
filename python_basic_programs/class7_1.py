"""
vendors = ["cisco","hp","lenovo","LG","Jupiter"]
for index,element in enumerate(vendors):
	print "index is %d" %(index+1)
	print "element is %s" %element


life = 0
while life<30:
	print "your life is ", life
	life = life +1

print "you are dead you have used {} life".format(life)


x = 1
while x<=10:
	print x
	x+=1

x =1
while x <=10:
	z = 5
	x = x+1
	while z<=10:
		print z
		z = z+1

def is_even():
	num = input("Please enter a number: ")
	i =2
	if i<=num:
		if num%i ==0:
			print "is even"
		else:
			print "is odd"
			i=i+1

is_even()

#Data structure: LIST

list = ["riku",0,9,2,3,"piku"]
print list


data1 = [1,2,3,4,5]
data2 = ['x','y','z']
data3 = [12.5,11.6]
list1 = [0,'rahul',"2"]
print ("elements in the list are: ",list1)

list1.append(10)
print ("after appending the list",list1)

list1.pop(-1)

print list1

list2 = ["ganesh","riku"]
list1.extend(list2)
print list1
list1.insert(2,"hello")
print list1

list1.remove("ganesh")
print list1
"""

list5 = [6,3,7,8,1]
print list5

list5.sort()
print list5






























