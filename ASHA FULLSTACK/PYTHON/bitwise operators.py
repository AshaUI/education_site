#bit wise operators are used to compare bits ,bits are nothing but 1 and 0 
# and--&  if both are 1 then op will be one  
# or--|   if any one bit is 1 op will be 1
# ex-or  ^   if both are different op will be true
# not ~ it will giv inverted op 
# <<       left shift ,shifting given num of bits to left side
# >>        right shift,shifting given num of bits to right side

     
#converting a decimal number to binary                                 
# we have a series of (2)^n  that is from righthand side  -----------
#   
#                          --------     (2)^6  (2)^5  (2)^4  (2)^3   (2)^2  (2)^1  (2)^0
#                                         64     32     16     8       4       2      1 
#a=60 is  11 1100 or 0011 1100  i.e        0      1      1     1       1       0      0  (32++16+8+4)=60
#x=55 is  11 0111 or 0011 0111             0      1      1     0       1       1      1  (32+16+4+2+1)=55
#we need to place 1's at the positions where we will get 60 by adding all posion values
#by adding  all corresponding num wher we placed 1 we will get 60(32+16+8+4=60)
# and  (& ) table   |       |   OR(|)  table       |   ex-or table         |      not table  |(appies to single bit)
# any one bit 0 o/p wll b 0||any one bit is 1 o/p 1||if both are diff o/p 1 ||  if bit is 1 o/p 0  ||         
#   
#    a & b   o/p  |           a | b   o/p          |    a ^ b   o/p           |   ~a    o/p
#    0   0   0    |           0   0   0            |    0   0   0             |    0    1
#    0   1   0    |           0   1   1            |    0   1   1             |    1    0
#    1   0   0    |           1   0   1            |    1   0   1       
#    1   1   1    |           1   1   1            |    1   1   0

          # & is simlply like  multiplctn (0*0=0,0*1=0,1*0=0,1*1=1)
x=55      # 0 0 1 1 1 1 0 0  =60
a=60      # & & & & & & & & 
b=13      # 0 0 0 0 1 1 0 1  =13 
c=a&b     # 0 0 0 0 1 1 0 0  =(8+4)=12
print(c)
          # | is simlply lik  addtion (0+0=0,0+1=1,1+0=1,1+1=1)
d=a|b     # 0 0 1 1 1 1 0 0  =60
          # | | | | | | | |
          # 0 0 0 0 1 1 0 1  =13
          # 0 0 1 1 1 1 0 1=(32+16+8+4+1)=61
 
print(d) 

e=a^b     # 0 0 1 1 1 1 0 0  =60
          # ^ ^ ^ ^ ^ ^ ^ ^
          # 0 0 0 0 1 1 0 1  =13
          # 0 0 1 1 0 0 0 1 =(32+16+1)=49
print(e)


f=~a     # 0 0 1 1 1 1 0 0  =60
         # ~ ~ ~ ~ ~ ~ ~ ~
print(f) # 1 1 0 0 0 0 1 1=(as first bit is sign 1 means -ve  so -61)

g=~b    # 0 0 0 0 1 1 0 1  =13
print(g)# ~ ~ ~ ~ ~ ~ ~ ~
h=~x    # 1 1 1 1 0 0 1 0  =(as first bit is sign 1 means -ve  so -14)
print(h)

print(10>>3 )  #                                ^ ^ ^
#in binary                      10 is 0 0 0 0 1 0 1 0  =(8+2)
#3 bit right side means         _ _ _ 0 0 0 0 1 = 1       last 3 bits will be discarded and        
#  tat is                       0 0 0 0 0 0 0 1           #remainig bits will move to rght most side and empty spases filled with 0's 
#                                         =o/p =1   
#simple formula is num>>n bits the o/p= num/(2)^n 
#wen a number shifts right side num value will be reduced as bits are moving to lower value side so division in formula is happening

print(10<<3)                   # 0 0 0 0 1 0 1 0  =(8+2) left side 3 bits discarde and 
#                                0 1 0 1 0 _ _ _       #move remaing bits to left most and fill 0's at empty places
#                                0 1 0 1 0 0 0 0   =(64+16)
#                                   o/p=80
#10 <<3 is 80 (val increasing)  and  10>>3 is 1 (val decreasing)

#simple formula is num<<n bits the o/p= num*(2)^n
#wen a number shifts left side num value will be increased as bits are moving to higher value side so multiplication in formula is happening

#not much needed
##left shift  formula num<<n=num*2^n
#right   formla num>>n=num/(2^n )
#bitwise ones compl formla  ~n=-(n+1)
#~4=~0000 0100=1111 1011----->will be -ve val --(remove last 1)--->1111 1010==do cmplmnt -->0000 0101-->5,,neg -->-5
#
