#for loop are to make iteration 
#syntax of for loop
#my_seq=[1,2,3]
#for i in my_seq:
   #print(i)
mylist=[1,2,3,4,5,6,7,8,9,10]
#for printing all elemnts in list
for i in mylist:
    print(i,end='')
print()
#for printing even and odd
for i in mylist:
    if i%2==0 :
        print(i)
    else:
        print(i,"is odd")
#printing only odd

for i in mylist:
    if i%2!=0 :
        print(i,end=(''))
        print()
#printin addtn of all

x=0                  # fr addtn var val shd b 0            
for i in mylist:
    x=x+i
    print(x)         #it gives result of evry iteration
print(x)             #it gives overall iteration


#multiplication of all  

list=[1,2,3,4,5]
y=1            #fr mulplctn we should take var val 1
for i in list:
    y=y*i
    print(y)
print(y)    

#iteration ovr strings
mystring='hello world'
for letter in mystring:
    print(mystring)

for letter in mystring:
    print(letter,"python") 

s1='java'
s2='python'
for i in s1,s2:
    print(i)


#practice qtns
#1.iterate over the string'levelup'
str='levelup'
for i in str:
    print(i,end=' ')    
#2.in the list print multiples of 3
list=[1,2,3,6,9,12,14,15]
for i in list:
    if i%3==0:
        print(i,"multpl by 3")

#3.add elements of list
list=[1,2,3,6,9,12,14,15]
sum=0
for i in list:
    sum=sum+i
    print(i)
    print()
print(i) 
#print 3& 5 multiples in list

lst=[1,2,3,6,9,12,14,15,45]

for i in list:
    if i%3==0 and i%5==0:
        print(i,"multpl by 3 &5")

#iterate over tuple
tpl=(1,2,3)
for i in tpl:
    print(i)        

#create list of tupe
t1=[(1,2),(3,4),(5,6)]










#dictinary  iteration

d1={'key1':10,'key2':20,'key3':30}
for i in d1:
    print(i)
    print(d1[i])
print(d1)
print(len(d1))

for i in d1.keys():
    print(i)
for i in d1.values():
    print(i)   
for x,y in d1.items():
    print(x,y)    

#iteration over set
s={1,2,3,4,5,5,'set1'}  #it excludes repetation
for i in s:
    print(i)



