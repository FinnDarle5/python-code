import random
randNumber = random.randint(1, 100)
# print("The guessed number is: " , randNumber) #--> It Prints the guessed Number
userGuess = None  #Needed to define otherwise throws an error
guesses = 0
while (userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    if(userGuess==randNumber):
        print('You guessed it right')
    else:      #Gets Executed if the number entered is wrong
        if(userGuess>randNumber):
            print("You guessed it wrong! , Enter a smaller number")
        else:
            print("You guessed it wrong! , Enter a larger number")
    guesses +=1

print(f'You have guessed the number in {guesses} guesses')

with open('hiscore.txt') as f:
    hiscore = int(f.read())


if(guesses<hiscore):
    print('You have just broken the high score!!!')
    with open('hiscore.txt', 'w') as f:
        f.write(str(guesses))