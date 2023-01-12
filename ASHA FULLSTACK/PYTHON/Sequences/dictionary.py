#dictionary is collection which is ordered and un indexed
#it is key value pair
#written in{} as set
#dictionary is mutable
from re import L 
from statistics import quantiles


d1={}
print(d1)
print(type(d1))
#1,2,3 are key of elements
d2={1:'jhon',2:'bob',3:'bill'}
print(d2)

mydict={
'brand':'BMW',
'model':'3series',
'year':2018
}
print(mydict)

#access dictionary items here we are using key as index
print(mydict['brand'])
print(mydict['year'])
x=mydict['model']
print(x)

print(mydict.items()) #item() will return all elements in dictonary

#dictionary is mutable change year to 2018
mydict['year']=2019
print(mydict)
mydict['model']='5series'
print(mydict)

#length of dictiony
print(len(mydict))

#add item to dictionary  no perticular method just define  the element with key . it will automatically adds
mydict['color']='black'
print(mydict)
mydict['fuel']='petrol'
print(mydict)

#delete item
mydict.pop('fuel')
print(mydict)
#popitem() is deleting last element
mydict.popitem()  
print(mydict)
del mydict['model']
print(mydict)


 #copy dict
x=mydict.copy()
print(x)
y=dict(mydict)
print(y)

#emptying dictionary
mydict.clear()
print(mydict)

#practice quantiles
# #create a dict 
#add an item to dict
#change the item
#remove last elem from dic
#find length of dict
#copy dict by both copy() and dict() methods


#nested dictionary
mystuff={'key1':'123','key2':'value2','key3':{'inside':[1,2,'hello']}}
print(mystuff)

print(mystuff['key3'])
print(mystuff['key3']['inside'][2])
print(mystuff['key3']['inside'][2][1]) #it prints e from hello
print((mystuff['key3']['inside'][2][1].upper))


d1={1:'hi',2:[{'10':'python',20:'html'}]}#[2][0] for accessing 0 th element[2][0][20] for accessing html bcs  2 is key 0 is index of list and 20 is key
print(d1)
print(d1[2])
print(d1[2][0][20])

#dict constructor
d2=dict(make='ford',model='ikon', year=2018)
print(d2)


#concatinate dict
d1={1:10}
d2={2:20}

d1.update(d2)
print(d1)

#Nested dictionary
d1={1:'hi',2:{'10':'python',20:'html'}}#[2][0] for accessing 0 th element[2][0][20] for accessing html bcs  2 is key 0 is index of list and 20 is key
print(d1)
print(d1[2])
print(d1[2][20])
print()

#loop through key

mydict={
'brand':'BMW',
'model':'3series',
'year':2018
}
print(mydict)

k=mydict.keys()
for i in k:
     print(i)

for j in mydict.values():

    print(j)

for x,y in mydict.items():
        print(x,y)





































































