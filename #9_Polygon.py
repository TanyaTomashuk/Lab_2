import turtle
import math

turtle.shape('turtle')
turtle.color('green', 'yellow')
turtle.speed(10)

def polygon(R, n, dR):
    turtle.left(180 - (n - 2) * 90/n)
    for i in range(1, n + 1, 1):
        turtle.forward(2 * math.cos(3.14159265 * (n - 2) / (2 * n)) * R)
        turtle.left(180 - (n - 2) * 180 / n)
    turtle.right(180 - (n - 2) * 90 / n)
    turtle.penup()
    turtle.forward(dR)
    turtle.pendown()

R = 10
for k in range(1, 11, 1):
    polygon(R, k + 2, 10)
    R += 10

turtle.exitonclick()







