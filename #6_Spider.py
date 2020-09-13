n = int(input())

import turtle

turtle.shape('turtle')
turtle.color('green', 'yellow')
turtle.speed(1)

for i in range(1, n + 1, 1):
    turtle.right(360 / n)
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)

turtle.exitonclick()


