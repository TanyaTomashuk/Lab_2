import turtle

turtle.shape('turtle')
turtle.color('green', 'yellow')
turtle.speed(2000000000)

def circle(R):
    for i in range(1,  361, 1):
        turtle.forward(R * 3.14159265 / 180)
        turtle.left(1)

def flower(n, r):
    for i in range(1, n + 1, 1):
        circle(r)
        turtle.right(360 / n)

flower (7, 100)

turtle.exitonclick()
