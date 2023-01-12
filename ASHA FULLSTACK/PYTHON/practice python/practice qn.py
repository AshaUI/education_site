#practice qtns
#creat a list
lst2=[1,2,'python2',4,]
print(lst2)

# append()   add an element to list
lst2.append(5)
print(lst2)
 # insert() 
lst2.insert(3,6)
print(lst2)
lst2.insert(5,'python33')
print(lst2)

#extend()
lst2.extend([10,11,12])
print(lst2)
#length of list
print(len(lst2))
#indexing & slicing

print(lst2[7])

print(lst2[2:8])
print(lst2[::-1])




'''
add multiple elements to list
add an element to index position 3
find lenght of list
indexing and slicing on list'''

#sets practise qns
#practice qns
#join two sets
j={11,22,44,'asha'}
k={55,66,44,'lvlup'}
m=j.union(k)
print(m)
j.update(k)
print(j)
#find commom element

s1={1,2,3,4,2,'3',3}
s2={3,4,5,6,5,6}
print(s1.intersection(s2))
#conv set to frozenset
s3=frozenset(s1)
print(s3)


#find length of set
print(len(s1))
#add multiple elements set
s2.update([10,20,30])
print(s2)
#remove random elem from set
s2.remove(30)
print(s2)
s2 .pop()
print(s2)
