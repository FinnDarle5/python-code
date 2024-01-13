def GreetHello(name , ending):
    print("Hello World")
    print("hi " + name)
    print("how ya doing")
    print(ending)

def LetterGenerator(name, date):
    st = f"Hi mam this is {name} and I will not come to school on {date}"
    print(st)

def average(a,b):
    return(a+b)/2

print('Executing function.....')
GreetHello("Falcone", "Thank you")
GreetHello("James Gordon", "Thanks for your service")
# LetterGenerator(input("Enter your name: "),
#                 input("Enter the date: "))
LetterGenerator("Ayush", '2- june')
print(average(23, 57))
print("done executing!")



