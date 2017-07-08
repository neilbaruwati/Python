def gencubes(n):
	out = []
	for num in range(n):
		out.append(n**3)
		return out
print gencubes(10)
#for x in gencubes(10):
	#print x 
"""
def gencubes(n):
	for num in range(n):
		yield num**3

for x in gencubes(10):
	print x
def genfibon(n):
	a = 1
	b = 1
	for i in range(n):
		yield a
		a = b
		b = a+b
for num in genfibon(10):
	print num


import random
random.randint(1,10)
def rand_num(low,high,n):
	for i in range(n):
		yield random.randint(low,high)

for num in rand_num(1,10,2):
	print num
"""
