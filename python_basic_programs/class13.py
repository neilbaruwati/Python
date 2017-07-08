#Exception and error handling: It is said to be abnormal condition in a program resulting to the disruption.
# in the flow of the program. Whenever an exception occurs, the program haults the execution.
#Exception in the code can be handled when there are some hierarchy in the exception zeroDivisionError, nameError, indentation error, IO error,
#EOF error.
"""
try:
	number = float(input("Enter a non-zero number as divisor: "))
	result = 100/number
	print "Result: ", result
except:
	print "Unexpected output, zero as divisor not accepted"

try:
	2 + 's'
except TypeError:
	print "There was a type error."
finally:
	print "finally this was printed"

try:
	f = open('chiranjib.txt','r')
	f.write("Text written here")
except:
	print "Error in writing the file"
else:
	print "File written successful"
try:
	f = open('chiranjib.txt','w')
	f.write("Text written here")
except:
	print "Error in writing the file"
else:
	print "File written successful"
"""
	



































