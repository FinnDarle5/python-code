num = float(input("Enter your number\n"))

table = [num*i for i in range(1, 11)]
print(table)

with open("Tables.txt", 'a') as f:
    f.write(str(table))
    f.write('\n')