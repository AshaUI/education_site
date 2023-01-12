#1.Arrange the list in Ascending order
l1=[1,2,'cool',-1,0,-3,10]
del l1[2]
print(l1)
l1.sort()
print(l1)

#2.Write a python program to append a list to the second list
l1=[1,2,'cool',-1,0,-3,10]
l2=[5,6,'smart',-2,-10]
l1.append(l2)
print(l1)
#3.Write a python function to return Arithmetic operations
def arith(a,b):
    return a+b,a-b ,a/b,a*b
print(arith(5,10))   
#4.Write a pythom program to generate multiplication table of a given number
'''x=int(input("enter a number:"))
print(x,"table is")
for i in range(1,11):
    
    print(x,'*',i,'=',x*i)'''
# 5.Write a python program to print even numbers in a list using while loop,for loop,lambda functions
lst=[1,12,34,45,47,56,67,78,89,23,35,46,14]
'''for i in lst:
    if i%2==0:
        print(i)'''

i = 0
while i < len(lst):
    element = lst[i]
    if element%2==0:
        print(element)
i+= 1   


'''l=list(filter(lambda i:i%2==0,lst))
print(l)'''

# 6.Write a python program to find the largest  of the three numbers
'''x=int(input("enter x:"))
y=int(input("enter y:"))
z=int(input("enter z:"))
if x==y and x==z:
    print("all are equal")
elif x==y and x>z:
    print("x and y are big")    
elif x==z and x>y:
    print("x and z are big")  
elif y==z and y>x:
    print("y and z are big")
elif x>y and x>z:
    print("x is big") 
elif y>z:
    print("y is big")       
else  :
    print("z is big") 
# 7.Write  a python program to print all odd numbers in a range.
for i in range (1,32):
    if i%2!=0:
        print(i)'''
        
