a = [3, 5, 1232, 55, 68, 44, 563]
# b = []
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)
## Shortcut to write the same:-
b = [i for i in a if i%2==0]
print(b)

t = [1, 5, 2, 56, 1, 5, 2]
s = {i for i in t}
print(s)