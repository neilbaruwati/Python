parrot = "Norweigin Blue"
letter = raw_input("Enter a character: ")
if letter in parrot:
	print "Letter {0} is present,".format(letter)
else:
	print "Letter {0} is not present.".format(letter)



number = "908,237,565,965,$_?"

clearedNumber = " "
for i in range(0,len(number)):
	if number[i] in '0123456789':
		print number[i]

		clearedNumber = clearedNumber + number[i]

intNumber1 = int(clearedNumber)

print "The number is {0}".format(intNumber1)

number = "908,237,565,965,$_?"
clearedNumber = ""
for char in number:
	if char in '0123456789':
		clearedNumber = clearedNumber + char
newNumber = int(clearedNumber)
print "The number is {0}".format(newNumber)



for i in range(1,11):
	for j in range(1,11):
		print "{0}*{1} = {2}".format(i,j,i*j)
	print "="*40




a = 3
b = "3"

if a is b:
	print "a and b have same ID"
else:
	print " does not have same ID"

a = 3
b = [1,2,3,4,5,6,7]
c = ["chiranjib",1,2,4.5,7]

if a not in b:
	print "not found"
else:
	print "found"

if a in c:
	print "found in c"
else:
	print "not found in c"


shopping_list = ["bread","milk","cheese","spam","Burger"]
for item in shopping_list:
	if item =="spam":
		print"I don't want to buy this item."
		break
	print "BuY" + item


shopping_list = ["bread","milk","cheese","spam","Burger"]
for item in shopping_list:
	if item =="spam":
		print"I don't want to buy this item."
		continue
	print "BuY" +" "+ item

rating = input("Enter the rating: ")
if rating != 0:
	print "Thanks for the rating."
	if rating <=2:
		print "Please explain about low rating."

	elif rating == 5:
		print "Thanks for the great feedback!"

else:
	print "Please give my rating greater than zero."


for number in range(10):
	if number == 7:
		break
	print number
 

list1 = [4,5,6]
list2 = [10,20,30]

for i in list1:
	for j in list2:
		if j == 20:
			break
		print i*j

list1 = [4,5,6]
list2 = [10,20,30]
for i in list1:
	for j in list2:
		if j == 20:
			continue
		print i*j



































