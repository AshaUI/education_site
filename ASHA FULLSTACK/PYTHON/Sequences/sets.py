#a set is a collection is un ordered and un indexed
#written using {}
#it will not take duplicate elements same ele in set
#sets are mutable
from queue import Empty


s={}
print(s)
print(type(s))#--dict
#-----------
s=set()
print(s)
print(type(s))

s={10,20,30,'xyz',10,20}
print(s)
print(len(s))# length is 4 because it will not count repeated elements


#accessing set items by indexing is not possible
#set doesnt support indexing,slising,

#adding items to set --adding one itenm
s.add(40)
print(s)

#update
s.update([50,60,50,60])#it adds only one set of 50,60--adding
print(s)
#length of the set it will not take repeated elemnts
print(len(s))

#set constructor--set(())
myset=set(('india','usa','uk'))
print(myset)

#remove itemd--remove(),discard(),pop()
s1={1,2,3,4}
s1.remove(2)
print(s1)

s1.discard(4)
print(s1)

s1.discard(5)# we are tryng to rem elm wich is not in set still no error
print(s1)

 #s1.remove(5)
#print(s1)

#pop()
s2={'abc','pqr','xyz'}
s2.pop()  # generally pop removes last elemnt but here it can remove any element from list
print(s2)


#practice qtns
#create a set ,add elemnt to set
#remove elem frm set,find length of set
#show the poped element from set

#copy set
s1={1,2,3}
s2=s1.copy()
print(s2)
s2=set(s1)  #for copying we can use both copy() and set()
print(s2)
# concatinating sets union(),update()
set1={1,2,3}
set2={4,5,6,4,5}
#print(set1+set2)  cant join

set3=set1.union(set2)
print(set3)
set1.update(set2) #no need to  take another var, it updates to existed set
print(set1) 

s1={'i','am','asha'}
s2={'i','am','sw'}
s2.update(s1)
print(s2)
#difference of set
x={'apple','fd','microsft'}
y={'amazon','google','apple'}
z=x.difference(y) #excluding y elem from x and print remaing of x
print(z)

z=y.difference(x)#excluding x elem from x and print remaing of y
print(z)
#subset
x={'a','b','c'}
y={'d','f','e','b','a',}
z=x.issubset(y)
print(z)
print(x.issubset(y))

#super set

y={'a','b','c'}
x={'d','f','e','b','a','c'} # x has all y elements so x is super y is 
print(x.issuperset(y))
print(y.issubset(x))
a={1,2,3,4,5,6,7}
b={2,3,4,5,8,9}
print(b.issubset(a))
print(a.issuperset(b))

#intersection of sets -- will return commom elements

s1={1,2,3,4,2,'3',3}
s2={3,4,5,6,5,6}
print(s1.intersection(s2))

#frozen set it is fixed,cannot be change
#wen a set con in to frozen ser update(), remove()clear() cannot be perform
s={1,2,3}
print(type(s))
f=frozenset(s)
print(f)
print(type(f))
#f.update([4,5])
print(f)

#f.remove(2)
print(f)
#f.clear()
print(f)

#delete frozenset
'''del f
print(f)'''
s1={'11','22','33'}
s1.clear()
print(s1)

s1.add('44')
print(s1)

#practice qns
#join two sets
j={11,22,44,'asha'}
k={55,66,'lvlup'}
m=j.union(k)
print(m)
#find commom element
#conv set to frozenset
#find length of set
#add multiple elements set
#remove random elem from set
















