import turtle

turtle.shape('turtle')
turtle.color('black', 'green')
turtle.speed(10)

def star(n, r):
    phi = 90 - 90 * (n - 2) / n
    for i in range(1, n + 1, 1):
        turtle.forward(r)
        turtle.left(180 - phi)

star(5, 100)

turtle.penup()
turtle.forward(200)
turtle.pendown()

star(11, 150)

turtle.exitonclick()
