# Using walrus operator
if(n := len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n} elsements, expected <= 3)") # Output: List is too long (5 elements, expected <= 3)
