import turtle

turtle.shape('turtle')
turtle.color('green', 'yellow')
turtle.speed(1000000000000)

def circle(R):
    for i in range(1, 181, 1):
        turtle.forward(R * 2 * 3.14159265 / 180)
        turtle.left(2)

circle(30)

turtle.exitonclick()
