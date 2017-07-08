import sys
ip_address = sys.argv[1]
x = ip_address.split(".")
print x
if 0<=int(x[0])<=255 and 0<=int(x[1])<=255 and 0<=int(x[2])<=255 and 0<=int(x[3])<=255:
	print "This IP address is a valid one"
else:
	print "This is not a valid IP address"

