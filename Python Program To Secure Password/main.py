#Python Program To Secure Your Password 
#Suggest a Good Password For Your Account

Secure = (('s','$'),('and','&'),
         ('a','@'),('o','0'),('i','1'),
         ('i','#'))

#Creating a Python Funtion
def SecurePass(password):
    for a,b in Secure:
        password = password.replace(a,b)
        return password

if __name__ == "__main__":
    password = input("Enter the Password: ")
    password = SecurePass(password)
    print("Your Password Is: {password}")
