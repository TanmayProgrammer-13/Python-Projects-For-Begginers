# Loops In Pyton
# While Loop

i = 1
while i < 7:
    print("Follow Mr Programmer")
    i += 1

# While Loop With Break Statement
x = 1
while i < 6:
  print(x)
  if x == 3:
    break
  x += 1

# While Loop With Continue

i = 1
while i < 8:
    i += 1
    if i == 5:
        continue
        print(i)

# While Loop With Else Statement
x = 1
while x < 10:
  print(x)
  x += 1
else:
  print("1 is no longer smaller than 10")

# For Loops 
# printing Hello Python For 10 Times Using For Loop 
i = 1
for i in range(11):
    print("Hello Python")

# For Loop With Break Statement

Strings = ["Python", "Programmer", "PC"]
for x in Strings:
  print(x)
  if x == "Programmer":
    break

# For Loop With Continue Statement
Strings = ["Python", "Programmer", "PC"]
for x in Strings:
  if x == "Programmer":
    continue
  print(x)

# Else Statement With For Loop
for x in range(8):
  if x == 4:
    break
  print(x)
else:
  print("Loop Has Ended Here")
