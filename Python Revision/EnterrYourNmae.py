name = input("Enter your name: \n")

with open('All_The_Names_entered' , 'a') as a:
    a.write(name + "\n")