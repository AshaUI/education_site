'''result=lambda lst:lst.sort() 

lst1=[(1,2,3),(4,5,6),(7,8,9),(11,22,33)]
print(result(lst1))'''

'''def fun(lst):
    lst.sort()
    print(lst)



lst1=[(1,2,3),(4,5,6),(7,8,9),(11,22,33)]  
fun(lst1)'''

x,y=[int(i) for i in input("enter x and y:").split()]
a=x
x=y
y=a
print("x value is",x)
print("y value is",y)
