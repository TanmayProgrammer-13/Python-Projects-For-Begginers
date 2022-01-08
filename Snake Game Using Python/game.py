# Snake Game With Score Counter 
# Importing Required Modules
from turtle import *
from random import randrange
import turtle
from freegames import square, vector


#Game Programming Starts Here
#Setting Background Color
bgcolor('black')
#Defining Screen Resolution
turtle.screensize('800 X 600')
#Setting Game Title
turtle.title("Snake Game")

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    aim.x = x
    aim.y = y
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190
def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'Lime')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'Lime')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()


