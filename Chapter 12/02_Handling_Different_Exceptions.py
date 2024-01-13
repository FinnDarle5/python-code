try:
    a = int(input("Enter a numbeer\n"))
    c = 1/a
    print(c)
except ValueError as e:
    print("Please enter a valid value.")
    print(e)

except ZeroDivisionError as e:
    print("Make sure you not dividing it by zero.0")
    print(e)

print("Thanks for using this code!")