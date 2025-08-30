from functools import reduce

# Map Example
l = [1,2,3,4,5]
square = lambda x: x*x
sqList = map(square, 1)
print(list(sqList))

# Filter Example
def even(n):
    if(n%2 == 0):
        return True
    return False
onlyEven = filter(even, 1)
print(list(onlyEven))

# Reduce Example
def sum(a, b):
    return a+b
mul = lambda x,y:x*y
print(reduce(sum,l))
print(reduce(sum,l))
