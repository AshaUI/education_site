#1.using list comprehension write a program to find the product of elements in two lists:
prod=1
a=[1,2,3,4,5]
b=[6,7,8,9,10]
for i in a:
    prod=prod*i
print("product of list a:",prod)      
prod=1
for i in b:
    prod=prod*i
print("product of list a:",prod) 

#2.using list comprehension find common elements in two lists.
lst1=[22,33,44,56,78,89,90]
lst2=[23,34,45,67,89,44,78]
s1=set(lst1)
s2=set(lst2)
s3=s1.intersection(s2)
print(s3)
s4=list(s3)
print(type(s4))
'''3.create an ouput dictionary which contains only the even numbers that are present in the input list as
   keys and their squares as values.'''

lst=[2,3,4,5,6,7,8,34,45,56,67,78]
dict={ }
for i in lst:
    if i%2==0:
     dict.keys=i
     dict.values=i**2

print(dict)     
