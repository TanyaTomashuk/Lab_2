import turtle

turtle.shape('turtle')
turtle.color('green', 'yellow')
turtle.speed(10)

def square(length):
    for i in range(1, 5, 1):
        turtle.forward(length)
        turtle.left(90)

square(50)

turtle.exitonclick()


