#Password Cracker Using Python
from random import *
user_Password = input("Enter Your Password: ")
password = ('a','b','c''d','e','f','g','h''i','j','k','l','m','n','o','p','q','r','s','t','u''v','w','x','y','z')
guess = ""

while(guess!=user_Password):
    guess=""
    for alphabet in range(len(user_Password)):
        guess_alphabet = password[randint(0,25)]
        guess = str(guess_alphabet)+str(guess)
        print(guess)
print('Your Password Is',guess)