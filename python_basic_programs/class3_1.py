x = True
print ("The initial state of x: ", x)
print("The type of x:", type(x))

x = not x
print("after not operation and assignment, the state x is",x)

x = 3
y = 4
print ("x=",x,"y=",y)
print("x==y returns", x==y)
print("x!=y returns",x!=y)
print("x>y returns", x>y)
print("x<y returns", x<y)
print ("x>=y returns",x>=y)
print("x<=y returns",x<=y)


number = 2
if (number ==1):
    print("one")
elif (number==10):
    print("ten")
elif number==20:
    print("twenty")
    
else:
    print("we are not looby for this value")
    
list_a = [1,2,3]
list_b = [1,2,3]
list_c = [4,5,6]
print (list_a == list_b)
print (list_a !=list_c)


name = "justin"
print(len(name))
print (len(name)==6)
print(50%2==0)

bag = [10,123,12443]
for item in bag:
    print item
    
for item in bag:
    if item==10:
        print("yeah!")
        
i=10
while i<11:
    print("yup")
    i=i+1
    
numerator=12
denominator=2
if denominator!=0:
    print(numerator/denominator)
else:
    print("division by zero not allowed")
    
grade = 44
if grade>=90:
    lettergrade="A"
elif grade >=80:
    lettergrade = "B"
elif grade >= 70:
    lettergrade = "C"
elif grade >=60:
    lettergrade = "D"
else:
    lettergrade = "F"
print lettergrade


for name in ("jane","john","matt"):
    print name
    
for i in [1,2,3,4,5,6,7,8,9,10]:
    print i
    
#TO PERFORM TASK REPEATEDLY
name = raw_input("please enter your name: ")
age = input("How old are you, {0}?".format(name))
print "okay, your age is {0}.".format(age)
if age>=18:
    print("you are old enough to vote")
    print ("please put an x in the box")
else:
    print("please come back in {0} years".format(18-age))

    
print ("please guess a number between 1 and 10!!")
guess = int(input())
if guess<5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("well done")
    else:
        print("you are not good")
elif guess>5:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("well done")
    else:
        print("sorry, you have not guessed correctly")
else:
    print ("you got it first time.")
    
x = False
if x:
    print ("x is true")




"""

print ('''False:{0}
None:{1}
0:{2}
0.0:{3}
empty_list[]:{4}
empty_tuple():{5}.format(False,bool(name),bool(0)))    

"""





for i in range(1,120):
    print ("i is now {0}".format(i))
    
for i in range(1,13):
    for j in range (1,13):
        print("{1} times {0} is {2}".format(i,j,i*j))

"""print ("==========================",end='\t') """


shopping_list = ["milk","pasta","eggs","spam","bread","rice"]
for item in shopping_list:
    print ("Buy " + item)
    
"""
if item == "spam":
    continue
    print ("Buy " + 2 + item)

    
"""

ip_address = "225.12.12.0"
x = ip_address.split(".")
print x
if int(x[0])<=255 and int(x[1])<=255 and int(x[2])<=255 and int(x[3])<=255:
	print "IP address is a valid one"




number = "9,223,372,036,854,775,007"
for i in range (0,len(number)):
    print number[i]


number = "9,223,372,036,854,775,007"
for i in range(0,len(number)):
    if number[i] in '0123456789':
        print number[i]



number = "9,223,372,036,854,775,807"
cleanednumber = ''
for char in number:
    if char in '0123456789':
        cleanednumber = cleanednumber + char
newnumber = int(cleanednumber)
print ("the number is {}".format(newnumber))
    




































































































    




























