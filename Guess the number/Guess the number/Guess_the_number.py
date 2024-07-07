import random

a = random.randint(0,20)

print("I have a random number between 0-20. You have 4 attempts. If you guess right, you'll have 3 wishes!")

b=int(input("What is the number? "))

att=3

while att>0:
    if b==a:
        print("WOW! You guessed it right on the first attempt!")
    else:
        att-=1
        b=int(input("Ok. No worries. Guess again. "))
        if b==a:
            print(f"Yesss. The number was {a}")
            break
    if att==0:
        print(f"You lose! The number was {a}")
    
