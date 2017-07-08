ip_address = raw_input("enter your IP address")
print ip_address.count(".")

parrot_list = ["pinin","nomo","askti","berft"]
parrot_list.append("new_breed")
for state in parrot_list:
	print "This is " + state
even = [2,4,6,8]
odd = [3,5,7,9]
num = even + odd

num.sort()
print num

print sorted(num)

number_in_order = sorted(num)

if number_in_order ==num:
	print "The list are equal"
else:
	print "The list are not equal"

#Tuples: mixture of list and dictionary.

tup1 = ()

tup2 = ("abc","abc")
tup3 = (("another","another"),("more","more"))
tup3[0][1]
tup2 +=("yet_another",123)

tup2

imelda = "riku","piku",2011,((1,"psycho"),(2,"jodu"),(3,"modhu"))

print imelda

title,artist,year,tracks = imelda
print title
print artist
print year
print tracks


title,artist,year,(track1,track2,track3) = imelda

print title
print artist
print year
print tracks

for song in tracks:
	print "\t", song

for song in tracks:
	track,title = song
	print "track number {0} and title {1}".format(track,title)


imelda = "riku","piku",2011,[(1,"psycho"),(2,"jodu"),(3,"modhu")]

print imelda


imelda[3].append((5,"all for you"))

title,artist,year,tracks = imelda
print imelda

tracks.append((6,"eternity"))

print title
print artist
print year
print tracks
for song in tracks:
	track,title = song
	print "track number {0} and title {1}".format(track,title)


#Dictionary : dictionaries are unordered set/collections. Dictionary elements are made with key and value pairs.
#Each key in a dictionary should be unique and must be immutable type.This means you can have strings,numbers and tuples.
#values need not have to be unique.

d1 = {1:"first_element",2:"second_element"}
fruit = {"orange":"a sweet, colored, citrous fruit",
	"apple":"a fruit for making cider",
	"lemon":"a sour yellow citrous fruit.",
	"grapes":"a small bunch of juicy fruit"}

print fruit["lemon"]
fruit["peer"] = " an odd shaped apple"
print fruit["peer"]
fruit["apple"] = "a great with taqila"

print fruit

fruit["peer"] = " an odd shaped apple with a different taste"
print fruit["peer"]

del(fruit["lemon"])

print fruit

#fruit.clear()
print fruit

while True:
	dict_key = raw_input("Enter a fruit name: ")
	if dict_key == 'quit':
		break
	if dict_key in fruit:
		description = fruit.get(dict_key)
		print description
	else:
		print "we don't have " + dict_key

for i in range(5):
	for snake in fruit:
		print snake + " is " + fruit[snake]
	print "="*50


ordered_list = list(fruit.keys())
ordered_list.sort()
for f in ordered_list:
	print f + " is " + fruit[f]

for val in fruit.values():
	print val
	print "="*40

for key in fruit:
	print fruit[key]

print fruit.keys()

my_list = ['a','b','c','d']
new_string = " "

for c in my_list:
	#new_string += c +"1" + "2,"
	new_string = ','.join(my_list)
print new_string
my_list = ['a','b','c','d']
numbers = "0123456789"
new_string = " "
for c in my_list:
	new_string = "missisipi".join(numbers)
	print new_string












































