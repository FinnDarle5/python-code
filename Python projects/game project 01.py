import random

def gameWin(comp , you):
    if comp == you:
        return None
    elif comp =='s':
        if you =='w':
            return False
        elif you =='g':
            return True
    elif comp == 'w':
        if you =='g':
            return False
        elif you== 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Comp Turn : Snake(s), Water(w) or Gun(g)")
RandomNo = random.randint(1 , 3)
# print(RandomNo)
if RandomNo == 1:
    comp ='s'
elif RandomNo == 2:
    comp ='w'
elif RandomNo == 3:
    comp ='g'

you = input(" Your's Turn : Snake(s), Water(w) or Gun(g)")
a = gameWin(comp , you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You Lose!")