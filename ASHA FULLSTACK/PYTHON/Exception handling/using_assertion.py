#assertion are statements  
'''num=int(input("enetr a number:"))
assert num%2==0,"you hav eentered invalid input or odd num"
print("after assertion")'''


#handling assertion error

try:
    num=int(input("enetr a number:"))
    assert num%2==0,"you hav eentered invalid input or odd num"
    print("after assertion")

except AssertionError as e:
  print(e)
  print("after assertion")


