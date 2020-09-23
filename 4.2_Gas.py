from random import randint
import turtle as t
import math

t.shape('circle')
t.shapesize(0.5)

number_of_turtles = 5
steps_of_time_number = 10000

t.penup()
t.goto(200, -200)
t.pendown()
for i in range (1, 5, 1):
    t.lt(90)
    t.fd(400)
t.penup()
t.home()

pool = [t.Turtle(shape = 'circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.shapesize(0.5)
    unit.penup()
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.speed(randint(1, 3))
    unit.right(randint(0, 360))

t.hideturtle()
for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(unit.speed())
        x = abs(unit.xcor())
        y = abs(unit.ycor())
        if (y >= 200):
            unit.seth(-unit.heading())
        else:
            if (x >= 200):
                unit.seth(180 - unit.heading())

t.exitonclick()




