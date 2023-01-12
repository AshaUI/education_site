from re import X


name='sam'
Name='same'
NAME='saam'

print(name)
print(Name)
print(NAME)
#EVEN PI is non changable python takes modified val
pi=3.142
print(pi)
pi=2.143
print(pi)
#if two var are holding same val ,both varibles address will be same
x=10
y=x
print(x)
print(y)
print(id(x))
print(id(y))
#val of x is changed so address also changed
x=9
print(id(x))
'''comments for multiple line '''
"""commentsfor multiple line"""
'''17-10-22'''
a=b=c=3
print(a,b,c)
a=10
b=20
c=30
print(a,b,c)
x,y,z=1,2,3
print(x,y,z)
x,y,z=1,2,3
print(x,y,z)
"value and type"
a=10.5
print(a)
print(type(a))
a="asha"
print(type(a))