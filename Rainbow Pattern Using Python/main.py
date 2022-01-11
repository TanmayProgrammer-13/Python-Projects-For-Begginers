# Importing Required Modules
import turtle
 
# Turtle Object
sc = turtle.Screen()
 
# Creating an Object(pen)
pen = turtle.Turtle()
 

def semi_circle(col, rad, val):
 
    # Filling the Semicolor
    pen.color(col)
 
    # Drawing a Circle
    pen.circle(rad, -180)
 
    # Move the turtle to air
    pen.up()
 
    
    pen.setpos(val, 0)
 
    # Move the Turtle
    pen.down()
 
    pen.right(180)
 
 
# Assigning Colors to the Rainbow 
col = ['violet', 'indigo', 'blue',
       'green', 'yellow', 'orange', 'red']
 
# Setup Screen Features For Turtle
sc.setup(600, 600)
 
# Setting Background Color to Black
sc.bgcolor('black')
 
# Adding Turtle Features
pen.right(90)
pen.width(10)
pen.speed(7)
 
# Running Loop For 7 Times
for i in range(7):
    semi_circle(col[i], 10*(
      i + 8), -10*(i + 1))
 
# Hide the turtle
pen.hideturtle()