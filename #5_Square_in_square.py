import turtle

turtle.shape('turtle')
turtle.color('green', 'yellow')
turtle.speed(10)

def square(i):
    for k in range(1, 5, 1):
        turtle.forward(i)
        turtle.left(90)
    turtle.forward(i)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(180)
    turtle.pendown()

for i in range(10, 110, 10):
    square(i)

turtle.exitonclick()




