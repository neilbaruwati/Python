s = 'hello'
for letter in s:
	print letter

s_iter = iter(s)
print next(s_iter)
print next(s_iter)
print next(s_iter)
print next(s_iter)



# Generator comprehension

my_list = [1,2,3,4,5]
gencomp = (item for item in my_list if item > 2)

for item in gencomp:
	print item
# List comprehension

list_comp =[item for item in my_list if len>3]
print list_comp


