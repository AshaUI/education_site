#1.using suitable control statement ,print item i as long as i is less than 8.
x=1                            #initialisation
while x<8:                   #condition
   print(x,end=' ')             #code
   x+=1 
   print()
#2.Write a Python  program to find the product of numbers in a list.
lst=[2,3,4,5,6]
prod=1
for i in lst:
   prod=prod*i
   print(prod)
print(prod)   


#3.Display numbers from 1 to 30 using looping statements.
x=1                            #initialisation
while x<=30:                   #condition
   print(x,end=' ')             #code
   x+=1 
   print()
#4.Write a Python program to count the number of even and odd numbers from a series of numbers.
s1={2,3,4,7,8,9,12,14,15,23,24,57,13}
evencount=0
oddcount=0
for i in s1:
   if i%2==0:
      evencount+=1
   else:
      oddcount+=1
print("no of even numbers in series",evencount)
print("no of even numbers in series",oddcount)     
'''5.Write a Python program which iterates the integers from 1 to 50. 
For multiples of three print "Foo" instead of the number and for the multiples of five print "Bar".
For numbers which are multiples of both three and five print "FooBar".'''
for i in range(1,51):
   if i%3==0 and i%5==0:
      print("foobar")
   elif i%3==0:
      print("foo")  
   elif i%5==0:
      print("bar")    
