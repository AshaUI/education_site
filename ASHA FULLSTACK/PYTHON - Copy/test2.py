#add india
t1=('usa','uk','canada')
t2=list(t1)
t2.append('india')
print(t2)
t3=tuple(t2)
print(t3)

2# reverse string
s='Python Training at Levelup'
print(s[::-1])

#3concatinating two sets
set1={2,4,6}
set2={8,10,6,4,10}
print(set1.update(set2))
print(set1)

#4 write a python program to print odd numbers in list
lst=[1,2,3,4,5,6,7,8,9,11]
print(lst[0:9:2])

for i in lst:
    if i%2!=0:
        print(i)

#5  write a python program to find average of 3 numbers
'''x,y,z=[int(x) for x in input("enter 3 numbers:").split()]
print("average is:",(x+y+z)/3)'''



#6write python prgrm to represent 20 in different forms
dec=20
print("20 in binary format",bin(dec))
print("20 in hex format",hex(dec))
print("20 in oct format",oct(dec))


#7concatinate using formate and print below output
x=9
print("iam on cloud {}".format(x))

#8type casting below data types
#int to float
a=10
print(type(a))
b=float(a)
print(type(b))
#str to int
x='124'
print(type(x))
y=int(x)
print(type(y))


#tuple to set
t1=(1,2,"india",4,5)
print(type(t1))
t2=set(t1)
print(t2)
print(type(t2))





