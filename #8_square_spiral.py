import turtle

turtle.shape('turtle')
turtle.color('green', 'yellow')
turtle.speed(10)

def sp_square(step, number):
    for i in range(1, step * number + 1, step):
        turtle.forward(i)
        turtle.left(90)

sp_square(2, 1000)

