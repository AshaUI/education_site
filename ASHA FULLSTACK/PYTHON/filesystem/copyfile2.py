f=open("ashaimg.jpg",'rb')
f1=open("copyimg2.jpg",'wb')
for i in f:
    f1.write(i)
