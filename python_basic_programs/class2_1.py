# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:12:31 2017

@author: chiranjib
"""

age = 24
print ("my age is "+ str(age) + " years")

print ("my age is {0} years".format(age))

print ("There are {0} days in {1},{2},{3},{4},{5},{6},{7}".format(31,"January","March","May","July","August","october","December"))

print (""" 
January:{2}
February:{0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}
 """.format(28,30,31))
 
print ("My age is %d years" %age)
 
print ("My age is %d %s, %d %s" %(age,"years",6,"months"))

for i in range(1,12):
    print ("No. of %2d squared is %4d and cubed is %6d" %(i,i**2,i**3))
    
print ("pi is approximately %12.50f" %(22/7))

for i in range(1,12):
    print("No. of {0:2} squared is {1:4} and cubed is {2:4}".format(i,i**2,i**3))
    
    
    