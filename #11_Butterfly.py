import turtle

turtle.shape('turtle')
turtle.color('green', 'yellow')
turtle.speed(2000000000)

def circle(R):
    for i in range(1,  361, 1):
        turtle.forward(R * 3.14159265 / 180)
        turtle.left(1)

def butterfly(n, R, dR):
    for i in range(1, n + 1, 1):
        circle(R)
        turtle.left(180)
        circle(R)
        R += dR

turtle.left(90)
butterfly(10, 50, 10)

turtle.exitonclick()

