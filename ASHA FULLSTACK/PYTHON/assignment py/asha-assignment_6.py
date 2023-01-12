#1.use a set to find the unique values of list :
 #mylist = [2,2,2,2,2,2,6,6,6,6,6,3,3,3,3,3,3]
mylist= [2,2,2,2,2,2,6,6,6,6,6,3,3,3,3,3,3]
s1=set(mylist)
print(s1)


'''2.Given a set,demostrate the use of copy().
   s={"fb","insta","twitter","whatsapp"}''' 
   
s={"fb","insta","twitter","whatsapp"}
t=s.copy()
print(t)

#3.create set and demonstrate the use of difference(),subset(),superset(),intersection.
st1={11,22,33,'python','css'}
st2={22,44,'css','JS'}
print(st1.difference(st2))
print(st2.difference(st1))
st1={11,22,33,44,'python','css','JS'}
st2={22,44,'css','JS'}
print(st1.intersection(st2))

print(st2.issubset(st1))
print(st2.issuperset(st1))
#4.create a set and convert it into frozenset
st1={11,22,33,44,'python','css','JS'}
st3=frozenset(st1)
print(st3)

#5.show how two sets can be joined with an example.
st1={11,22,33,'python','css'}
st2={22,44,'css','JS'}
st1.update(st2)
print(st1)
st3=st2.union(st1)
print(st3)

