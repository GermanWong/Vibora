from turtle import *
from random import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['black','purple','blue','yellow','brown']
colorS = choice(colors)
colorF = choice(colors)
while True:
    if colorS == colorF:
        colorS=choice(colors)
    else:
        break
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -210 < head.x < 190 and -210 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
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
        square(body.x, body.y, 9, colorS)

    square(food.x, food.y, 9, colorF)
    update()
    ontimer(move, 100)

def movefood():
    food.x += randrange(-10,11,10)
    food.y += randrange(-10,11,10)

    if food.x >= 190:
        food.x += randrange(-10,0,10)
        food.y += randrange(-10,11,10)

    if food.x <= -200:
        food.x += randrange(0,11,10)
        food.y += randrange(-10,11,10)
    
    if food.y >= 190:
        food.x += randrange(10,11,10)
        food.y += randrange(-10,0,10)

    if food.y <= -200:
        food.x += randrange(10,11,10)
        food.y += randrange(0,11,10)


        


    ontimer(movefood,500)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
movefood()
done()
