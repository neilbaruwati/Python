import math

#f(x) = x*2 -5x + 6

#f'(x) = 2x - 5

x0 = input("put an intial value : ")

x0 = float(x0)


def func(x):
   
   #f(x) = x*2 -5x + 6
   #r=  x*x - 5.3*x + 6
   
   #f(x)  = x - 2sin x


   r=  x - 2 *math.sin(x)


   return r


def funcd(x):
   #f'(x) = 2x - 5
   #r=  2*x - 5.3

   #f'(x)  = 1 - 2cos x
   r=  1 - 2*math.cos(x)
   return r

print "computing newton raphson with initial value %f" %(x0)

N = 10
i =0
x1 = x0


while abs(func(x1)) > 1e-65:
   x1 = x0 - func(x0)/funcd(x0)
   x0 = x1
   N = N - 1
   i = i + 1

   print "iter = %d  x = %.15f  func(x1) =  %.15f" %(i, x1, func(x1))

