#while loop evaluates untill condition is true
# syntax of while loop
#while bool_condition
   #code
x=0
while x<5:
    print(x)
    x=x+1 

#printing 1 to 20
x=1                            #initialisation
while x<=20:                   #condition
   print(x,end=' ')             #code
   x+=1                        #increment


print()

x=1   #prints "hi" 10 times
while x<=10:
    print("hi")
    x+=1

x=5
while x>=1:
    print(x,end='')
    x-=1
    print()

i=1
while i<=20:
    if i%2==0:
      print(i) 
      i+=1

