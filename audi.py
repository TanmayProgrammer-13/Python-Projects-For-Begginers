# draw audi logo using python
import turtle
audi = turtle.Turtle()

audi.pensize(7)
turtle.Screen().bgcolor("black")
audi.pencolor("#D0CFCF")
audi.speed(10) 

#running for Loop 
for i in range(4):
  audi.penup()
  audi.goto(i*70, 0)
  audi.pendown()
  audi.circle(50)


audi.color("white")
audi.penup()
audi.goto(77, -40)
audi.pendown()

audi.write("Audi By Mr Programmer",font=("Arial", 16, "bold","italic"))
turtle.done()
