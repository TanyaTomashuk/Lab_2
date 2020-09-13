import turtle

turtle.shape('turtle')
turtle.color('green', 'yellow')
turtle.speed(2000000000)

def arc(R):
    for i in range(1,  181, 1):
        turtle.forward(R * 3.14159265 / 180)
        turtle.right(1)

def spring(n, R, r):
    for i in range(1, n + 1, 1):
        arc(R)
        arc(r)
    arc(R)

turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.left(90)

spring(4, 100, 20)

turtle.exitonclick()
