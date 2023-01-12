#transfer 
# statement RE USED TO TRANSFER from one place to aother place
#in program
#break,,, continue,,,pass

#break -breaks current enclosest loop after break nothing will be incremented and printed
#continue-goes to the top of current enclosest loop
#pass-does nothng at all

mystr='python'

for letter in mystr:
    if letter=='h':
        break
        print(letter)

x=0
while x<5:
    if x==3:
        break
    print(x)   
    x+=1

for i in 'python':
  if i=='o':
    break
  print(i)

  #continue
  mystr='django'
  for letter in mystr:
    if letter=="a":
        continue
    print(letter)

x=1
while x<=25:
    x=x+1
    if x%2==0:  #skips all even numbers
        continue
    print(x)

 #pass will do nothing it will send control to very next instruction

x=[1,2,3]
for i in x:
    pass
print('end of loop')

for i in range(1,25):
    if i%2!=0:
        pass
    else:
        print(i)
#write a python program to check if a num is prime or no




x=[10,11,12,15,20,25]
for i in x:
    if i%5==0:
        print(i)

x=[10,11,12,15,20,25]
for i in x:
    if i%5==0:
        print(i) 
        break

x=[11,12,13,14,16,18]

for i in x:
    if i%5==0:
       pass
    else:
        print("not found")
else:
    print("not found again")       

#prime number validation
num=4     
for i in range(1,num):
    count=0
    if num%i==0:
        count=count+1
if count!=0:
        print(" not prime") 
else:
        print("prime")
 




    


