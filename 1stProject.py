import random
Target=random.randint(1,100)
while True:
    UserChoice=input("Guess the number or press (Q) for Quit: ")
    if(UserChoice=="Q"):
        break
    UserChoice=int(UserChoice)
    if(UserChoice==Target):
        print("Success:You guess the correct number: ")
        break
    elif(UserChoice<Target):
        print("Your number was too small.Take a bigger guess... ")
    else:
        print("Your number was too big.Take a smaller guess... ")
print("----GAME OVER----")
