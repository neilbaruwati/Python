#object oriented programming
#techniques: class and object.

#a class creates a new type where objects are the instance of a class.
#an object can store data using variables.

#object that can use function that belong to class are called methods.

#oject that can use functions that belong to class are called methods.
#variables that belong to object or class is a fields.
#collectively, fields and methods are referred as attribute of the class.
#fields are of two types that belong to each object of the class are belong to class itself.

class person(object):
	def say_hi(self):
		print "Hello, how are you?"
p = person()
p.say_hi()


class myRouter(object):
	"""This is a class that describes a router."""
	def __init__(self,routername,model,slno,ios):
		self.model = model
		self.ios = ios
		self.slno = slno
		self.routername = routername
	def print_router(self,manf_date,dd):
		print "the router name is", self.routername
		print "the model name is ", self.model
		print "the serial number is ", self.slno
		print "the ios name is " , self.ios + dd
		print "The model and the data is " , self.model + manf_date

router1 = myRouter("R1","onida",1213,12.3)

print router1.model
print router1.ios
print router1.print_router("20/9/2017", 55)

#init is a method that runs as soon as the object of the class is instantiated. this method is used 
