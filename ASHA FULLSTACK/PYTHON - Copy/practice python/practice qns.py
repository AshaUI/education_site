# create list and  remove elements from index position
l1=[11,22,33,44,55,-11,-22]
del l1[4]
print(l1)
l1.pop(2)
print(l1)
#find max and min elements 
print(max(l1))
print(min(l1))
#sort the list in desending order
l1=[11,22,33,44,55,-11,-22]
l1.sort(reverse=True)
print(l1)

#join 2 lisrs
l2=[66,77,88,]
print(l1+l2)
#nested list
l3=['a','s',[99,100],'aisha']
print(l3[0])
print(l3[3])
print(l3[2][1])
print(l3[3][1])

#create a list using list constructor
print(list(('x','y','z')))

#copy one list to another list
l4=l3.copy()
print(l4)
l5=l1.copy()
print(l5)

