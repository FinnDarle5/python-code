a1 = {3, 4, 99, 6, 6, 6, 6}
a2 = {9, 66, 33, 22, 41568, 0, 6}
print(a1)
print(a2)

# print(a1.pop()) #Removes a random element from the set
# print(a1.copy()) #Creates a copy of the set
# a1.a  dd(52000) #Adds 52000 to the set
print(a1.union(a2)) #Adds all the elemants that are not present in a1 but are present in a2
#a1.union(a2) #doesnot make changes to the existing set BUT it makes a new set

print(a1.intersection(a2))#Returns the common elements present in both a1 and a2
#It also doesnot make changes to the existing sets, and makes a new set.

print(a1)
print(a2)