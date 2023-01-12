#1.Write python program to find the largest of three numbers.
x=int(input("enter x num:"))
y=int(input("enter y num:"))
z=int(input("enter z num:"))
if(x==y and x==z) :
    print("x y z are equal")
elif(x==y and x>z)   :
    print("x &y are big")
elif(x==z and x>y)   :
    print("x &z are big")
elif(z==y and z>x)   :
    print("z &y are big")
elif (x>z and x>y)   :
  print(" x is big")
elif (y>z)  :
    print("y is big") 
else:
    print("z is big")    
#2.Write a python program to check whether a person can get a driving license (consider age to be 18 and above)
age=int(input("enter persons age:"))
if (age>=18):
    print("person can get driving license")
else:
    print("person cannot get license as age is less than 18")

#3.Write a program to check student result for below marks and display grade
'''90 or above is equivalent to an A grade
  80-89 is equivalent to a B grade
  70-79 is equivalent to a C grade
  65-69 is equivalent to a D grade
  64 or below is equivalent to an F grad'''
m=int(input("enter student marks:"))
if (m>=90):
    print("A grade")
elif(m>=80 and m<=89) :
    print("B grade")   
elif(m>=70 and m<=79) :   
  print("C grade")
elif(m>=65 and m<=69) :   
  print("D grade") 
elif(m<=64) :   
  print("F grade")    
