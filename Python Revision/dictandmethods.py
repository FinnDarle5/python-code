# a = {} #It is an empty dictionary
# print(type(a))
#
# b = set() #It is an empty set
# print(type(b))

dict1 = {'Good boy' : 'A boy who listens to his parents' ,
         'Fetch' : 'To bring',
         '1' : 'The number 1'}
# print(dict1['Good boy'])

marks = {'Harshit' : 99.4586,
         'Ayush'   : 70,
         'Adarsh'  : 82.6,
         'Kishan'  : 70}
print(marks['Ayush'])

marks["niloyyy"] = 22
print(marks['niloyyy'])
print(marks)

marks.pop('niloyyy')
print(marks.copy())
# marks.clear()
print(marks.keys())

print(marks)