#Python Program To Check Voter's Eligblity
age = int(input("Enter Your Age: "))

if age > 18:
    print("You Are Eligible To Vote Now")
elif age < 18:
     print("You Are Not Eligible To Vote Now")
else:
    print("Invalid Input, Try Again")
    