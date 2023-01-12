#list is a collection /sequence which is ordered and indexed
#written using[]
#it stores elements dynamically
#lists are mutable

lst=[]
print(lst)
print(type(lst))

lst1=[10,20,'python',-10,30.5]
print(lst1)

#length of list
print(len(lst1))

#indexing
print(lst1[0])
print(lst1[4])
#print(lst1[5])
print(lst1[-3])

#slicing
print(lst1[0:3])
print(lst1[2:4])
print(lst1[-4:-1])
#reversing list with slicing techniq we reverse the string and lists
print(lst1[::-1])
# ADDING ELEMENTS TO LIST  append() -- adds elem at last of list, insert()--inserts at index ,  extend()--adds mul elem at last ,

#append() -- adds elem at last of list
lst1.append(55)
print(lst1)
lst1.append(66)
print(lst1)

#insert()---at some index
lst1.insert(2,77)
print(lst1)
lst1.insert(2,'python3')
print(lst1)

#extends()--adds mul ele at last
lst1.extend([88])
print(lst1)
lst1.extend([99,100])
print(lst1)
print(len(lst1))
# remove list elements  removes actual element
lst1.remove('python3')
print(lst1)
del lst1[1] # deletes index elements
print(lst1)
lst1.pop(1) # removes last element

 #sort() accending order
lst=[19,20,-10,30.5,40,1,2]
lst.sort()



# max() min()
lst1=[2,3,4,5,6]
print(max(lst1))

print(min(lst1))

#copy list---copy()  list()    copies the list elements
l1=[1,2,3]
l2=l1.copy()
l2=list(l1)
print(l2)
#nested list---list inside list
lst=['hello',[1,2,3],['a']]
print(lst)

print(lst[0])
print(lst[2])
print(lst[0])
print(lst[0][1])
print(lst[1][1])


#list concatination
l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)
l3=l1+l2
print(l3)
print(l1+[4,5,6])
print([1,2,3]+[4,5,6])


#list constructor--list(()) it constructs  elements we given in list form
mylist=list(('hi','hello','bye'))
print(mylist)

#list membership operators--'in' and 'not in'
lst=[1,'1','hi',2,3]
print(1 not in lst)
print("1" in lst) #it checks wether 1 is in the list or not
print('hi' not in lst)
print("Hi"  in lst)
print("2 in lst")  # it prints as it is

#lists are mutable---changeable

lst1=['usa','uk','india']
lst1[1]='canada'
print(lst1)
lst1.append('germany') #'append' will add single element 'extend' will add multiple elements
print(lst1)

lst1.pop(1)#pop method on  lst1
print(lst1)
lst1.remove('usa')
print(lst1)

l2=[1,2,3,4,5,6,6,1,2]
del (l2[1:4])
print(l2)

#index
print(l2.index(5))
#count
print(l2.count(6)) #counting no of 6 in list

#clear
l2.clear() #deleting elements from list
print(l2)

 #sort() accending order
lst=[19,20,-10,30.5,40,1,2]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)
#list METHODS
#append(),insert(),extend(),remove(),pop(),sort(),max(),min(),list(),index(),count(),clear(),del()
 #sort() accending order
lst=[19,20,-10,30.5,40,1,2]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

 #sort() accending order
lst=[19,20,-10,30.5,40,1,2]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)