"""
def ask_item():
	try:
		val = int(input("Please enter an integer:" ))
	except:
		print "Looks like you did not enter an integer"
	else:
		print "Finally, block executed"
		print val

ask_item()


while True:
	try:
		val = int(input("Please enter an integer: "))
	except:
		print "Looks like you didn't enter an integer."
		continue
	else:
		print "correct, that is an integer."
		break
	finally:
		print "Finally block executed"
print val

"""
while True:
	try:
		number = int(input("Enter a number: "))
		print number
		a_file = open('module.py')
		print a_file.readline()
	except NameError:
		print "Not a number, please re-enter."
		break
	except IOError:
		print "unable to open file"
		continue
print "Finished"






















	
