"""
class song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday_lyric = song(["happy bday to u","I don't want to get sound", "so, i will stop here"])

happy_bday_lyric.sing_me_a_song()

# accessing object variable

class MyClass:
	variable = "blah"
	def function(self):
		print "This is a message inside the class."

myObjectx = MyClass()
print myObjectx.variable

myObjecty = MyClass()
myObjecty.variable = "yourcity"
print myObjecty.variable

# accessing object functions

myobjectx = MyClass()
myobjectx.function()


class Student:
	scount = 0
	def __init__(self, name, subject):
		self.name = name
		self.subject = subject
		Student.scount +=1
	def saycount(self):
		print Student.scount
	def sayStudent(self):
		print "Name: ", self.name,  "\n"
		print "Subject: " , self.subject


std1 = Student("John", "Python")
std2 = Student ("Jack", "C")
std3 = Student ("Jill", "cpp")


std1.sayStudent()
std2.sayStudent()

print Student.scount

#Inheritance of classes.

class Parent:
	pa = 2
	def __init__(self):
		print "Parent constructor called"
	def pm(self):
		print "in parent method"
	def seta(self,a):
		Parent.seta = a
	def geta(self):
		print "attribute is: ", Parent.pa

class Child(Parent):
	def __init__(self):
		print "I am a child constructor"
	def cm(self):
		print "child method called"

John = Child()

print John.cm()
print John.pm()
print John.seta(5000)
print John.geta()
"""
#Data Hiding: How we can hid name of data so that no other members can access that data

class smsgs:

	__sms = 0
	def msgs(self):
		self.__sms+=1
		print self.__sms
hide = smsgs()
#now i am going to call function couple of times and i can increment number have to call hide msgs.

hide.msgs()
hide.msgs()
hide.msgs()
hide.msgs()
#print hide.__sms
#we get error while printing

hide._smsgs__sms

#R






























	


































#Data Hiding




























