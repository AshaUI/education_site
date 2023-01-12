#Built in modules are predefined , they are already available
#numpy,pandas,math,random,functools,datetime,re,urllib

import platform
z=platform.system()
print(z)  #gives palt form we use nothing but windows

#math module
import math
'''r=float(input('enter radius:'))
area=math.pi*r**2 # wen we r importing entire file we should call pi with math.pi
print("area is:",area)'''

print(math.pi)

from math import pi   #importing individua pi , so while accessing it we dont need to call it with math.
print(pi)

from math import *
print(pi) # as we are importing all (*)from math individually we dont need to call with math.

import math
print(dir(math))   #it will print all funtions available in "math" file
print(math.sqrt(25))
print(math.factorial(5))  #we cancall factorial and sqrt by its name itself as we hav already imported all individually by (*).

#random
import random  #to givr random ops in the given range
print(dir(random))  #it will print functions available in random
print(random.randint(0.6)) #it prints any no from range randomly
print(random.random()) #it prints any no btwn 0 and 1 randomly
print(random.random()*100)  #it prints any no btwn 0 and 1 randomly with 100 multiply



