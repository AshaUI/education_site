# 5.Write a python program to print even numbers in a list using while loop,for loop,lambda functions

'''for i in lst:
    if i%2==0:
        print(i)'''
lst=[1,12,34,45,47,56,67,78,89,23,35,46,14]

i = 0
while i < len(lst):
    element = lst[i]
    if element%2==0:
        print(element)     
    i+=1
