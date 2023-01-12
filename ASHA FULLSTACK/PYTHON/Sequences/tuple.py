
#tuple are sequence /collection which is ordered and indexed
#tuples are immutable 
#written using()



tp1=()
print(tp1)
print(type(tp1))

tp1=(40)
print(tp1)
print(type(tp1))
tp1=(40,)
print(tp1)
print(type(tp1))
tp1=(40,50,40,'abc')
print(tp1)

#indexing
print(tp1[0])

print(tp1[2])

#slicing for printing multiple elements
print(tp1[2:3])
print(tp1[1:4]) #it will print 1 indexd element to till 3indexd elemnts

#length oe tuple
print(tp1[3:8])
print(len(tp1))

#e cannot use methods such as append,insert,extend(),remove(),clear()

#change tuple values we cannot directly change values we should first convrt to list thn change  elemnts
x=('python','html','js')

y=list(x)                # conv tuple to list
print(type(y))
print(y)
y[1]='css'  #changing html as css
print(y)  
z=tuple(y)   # conv list to tuple back
print(z)

tpl1=('rose','lotus','sunflower')
tpl2=list(tpl1)
tpl2[2]='jasmine'
tpl3=tuple(tpl2)
print(tpl3)

#tuple concatination-joining ,combining,adding
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)
t3=t1+t2
print(t3)
t1=(1,2)
t2=('abc','xyz')
print(t1+t2)

#tuple membership test- 'in' and 'not in'

tpl=(1,"1",2,3,'hii')
print("1" in tpl)
print("'1' not in tpl")
print(1 and 2 in tpl)
print(1 and 4 in tpl)

#add
t1=('india','canada','usa')
t2=list(t1)
t2.append('spain')
print(t2)
t3=tuple(t2)
print(t3)

#pactise questions
#craete tupe and do indexing and slicing 
#find length of tuple
#change 'hi' to 'hey' in following tuple t1=("hii",'bye','hi')
#repeat tuple 3 times

t1=("hii",'bye','hi')
t2=list(t1)
t2[2]='hey'
t1=tuple(t2)
print(t1)

'''tpl=(1,2,1,1,2,3,4)
print(tpl)
#tupple method
print(tpl.index(4))
#count()
print(tpl.count(1))
#tuple constructor-tuple(())
t1=tuple((1,2,3))
print(t1)'''

          