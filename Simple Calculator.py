#Calculator With Options

a = int(input("Enter a Number: "))
b = int(input("Enter another Number: "))

op = input("Press The Desired Number Given: ")

#Adding Options For Performing Actions
print("Press 1 To Add")
print("Press 2 To Subtract")
print("Press 3 To Multiply")
print("Press 4 To Divide")
if op == "1":
    print("Result Of a+b Is: ",a+b)
elif op == "2":
    print("Result Of a-b Is: ",a-b)
elif op == "3":
    print("Result Of a*b Is: ",a*b)
elif op == "4":
    print("Result Of a/b Is: ",a/b)
else:
    print("Wrong Input Try Again...")