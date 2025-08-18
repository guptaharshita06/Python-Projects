#List is mutable
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry")
print(friends)

l1 = [1,2,9,8,5,3]
l1.sort()
l1.reverse()
l1.insert(3,0)
l1.pop(3) #index likho
l1.remove(8) #value likho
print(l1)
