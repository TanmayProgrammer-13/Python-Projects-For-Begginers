#Number Guessing Game Using Python
#Importing Modules
import random
num = random.randint(1,10)
guess = int(input("Enter the Number Between the Given Range: "))
while num < 5 != "guss":
 if guess < num:
     print("You Guessed Too Small")
 elif guess > num:
     print("You Guessed Too Large")
 break
else:
    print("Finally, You Guess It :)")


