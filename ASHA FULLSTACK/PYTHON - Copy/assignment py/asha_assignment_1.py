#practice qstns
#create a variable and cheack its data type


p=4+5j
print(p)
print(type(p))
#types of variable assignment
x=y=z=45
print(x,y,z)
x,y,z,=3,6,9  #if x,y,z=3,6,9,12 --gives error of too many values
print(x,y)    #if x,y,z,k=3,6,9 --gives error of not enough values to un pack
print(x,y,z,)
x=5
y=6
#find address of variable
print(id(x))
print(id(y))
print(id(z))

#numeric type int,float,complex'''
print('data types')

a=10
b=12.2
c=2+3j #2 is real part ,3 is imaginary part ,'j' is standard co-efficient
d='1234'
e=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Boolean type  True and False
e=False
print(e)
print(type(e))
#type conversion 
print('   ')
print('type conversion')
a=10
b=12.4
c='1234'
#INT TO FLOAT conversion
x=float(a)
print(x)
print(type(x))
#FLOAT TO INT conversion
y=int(b)
print(y)
print(type(y))
#STRING TO INT conversion
z=int(c)
print(z)
print(type(z))
#INT TO STR conversion
k=str(z)
print(k)
print(type(k))
'''l=int(p)
print(l)
print(type(l))'''
#BOOLEAN INT,FLOAT, STR conversion
print('BOOLEAN INT,FLOAT, STR conversion')
m=float(e)
print(m)
print(type(m))

a=6
b=complex(a)
print(b)
print(type(b))
#string to integer
x='1234'
y=int(x)
print(y)
print(type(y))
'''a='abcd'
b=int(a)
print(b)
print(type(b))'''
