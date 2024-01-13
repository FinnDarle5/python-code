'''
Write a python program which will keep adding a stream of numbers
inputed by the user
'''
sum = 0
while(True):
    number = input('Enter the price : ')
    if(number != 'q'):
        sum = sum + float(number)
        print(f'your order total so far {sum}')

    else:
        print(f'Your bill total is : {sum}')
        print('Thanks for shopping with us')
        break