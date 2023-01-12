#logical operators are used to combine conditional statements
#and,,or..not
# x and y----true if both are true
# x or y ---true any one is true
# not x ----true wen x is false
x=20
y=30
print(x==20 and y==30)
print(x==20 and y==31)
print(x==20 or y==31)
print(x<=21 or y==31)
print(x>=21 or y==31)
print(not(x==21 or y==31))