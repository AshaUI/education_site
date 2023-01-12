#these are used to check if object are same memory locations
# 'is'  and 'is not'
x=[1,2,3]
y=[1,2,3]
print(x is y) # it gives flase bcs it just checks memory locations nt elements
z=x   # assigning memory locations of x to z as list is mutable
print(x is z)

#tuple
a=(1,2,3)
b=(1,2,3)
print(a is b) # tupls are immutable 
print(a is not b)



#membership operators
# "in"  "not in"
lst=['hi','helo',"bye",'bye']
print('hello' in lst)
print("'bye'" in lst)
print('bye' in lst)
print('hi in lst')
print('helo' not in lst)
