from random import randrange
from turtle import *
import random

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

crand =random.randint(1,5)
if crand == 1:
    color = 'blue'
elif crand == 2:
    color = 'yellow'
elif crand == 3:
    color ='green'
elif crand == 4:
    color = 'purple'
elif crand == 5:
    color = 'orange'

ccrand = random.randint(1,5)
if ccrand == 1:
    color2 = 'yellow'
elif ccrand == 2:
    color2 = 'blue'
elif ccrand == 3:
    color2 ='purple'
elif ccrand == 4:
    color2 = 'green'
elif ccrand == 5:
    color2 = 'orange'

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, color)
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        #Se mueve en un rango aleatorio entre -1 y 1 en los ejes "x" y "y"
        food.x = randrange(-1, 1) * 10
        food.y = randrange(-1, 1) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color)

    square(food.x, food.y, 9, color2)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
