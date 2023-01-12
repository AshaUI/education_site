'''=int(input("enter a number:"))
if(n%2!=0):
    print("weird")
elif(n%2==0 and n in range(2,6)):
    print("Not Weird")
elif(n%2==2 and n in range(6,21)) :
    print("WEIRD")'''

l=list(map(int,input().split()))
print(l)
x,y=[int(x) for x in input("enter values:").split()]
for i in l:
    if i%x==0 and i%y!=0:
        print(i,end='')








    


