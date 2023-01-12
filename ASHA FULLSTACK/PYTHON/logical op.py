#logical operators are used to combine conditional statements
#and,,or..not
# x and y----true if both are true
# x or y ---true any one is true
# not x ----true wen x is false
x=20
y=30
print(x==20 and y==30)  #1st and 2nd conditions are true,o/p is true
print(x==20 and y==31)  #1st cond is true but 2nd is flase so o/p is false
print(x==20 or y==31)   #1st conditn is true so o/p is true bcs in 'or' if any one condtion is true o/p will be true
print(x<=21 or y==31)   #1st is true so o/p is true
print(x>=21 or y==31)  #x is not greater than 21 and not equal so 1st is false,and 2nd is false so o/p is false
print(not(x==21 or y==31)) #1st is false and 2nd also false so condition is side () is false, and not(flase)is true so o/p is true