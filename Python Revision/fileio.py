s = "Hello world"

#writing to a file
# with open("test.txt", "w") as f:
#     f.write(s)

# fp = open("test.txt", "w")
# fp.write(s)
# fp.close()

# #Reading a file
# with open("test.txt", "r") as f:
#     s = f.read()
#     print(s)

a = open("test.txt", "r")
s = a.read()
a.close()
print(s)


