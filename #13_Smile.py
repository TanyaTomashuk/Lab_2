import turtle

turtle.shape('classic')
turtle.color('black', 'yellow')
turtle.speed(2000000000)

def circle(R):
    for i in range(1,  361, 1):
        turtle.forward(R * 3.14159265 / 180)
        turtle.left(1)

def arc(R):
    for i in range(1,  181, 1):
        turtle.forward(R * 3.14159265 / 180)
        turtle.right(1)

turtle.begin_fill()
circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(-45, 120)
turtle.pendown()
turtle.color('black', 'blue')
turtle.begin_fill()
circle(15)
turtle.end_fill()

turtle.penup()
turtle.goto(45,  120)
turtle.pendown()
turtle.begin_fill()
circle(15)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 115)
turtle.pendown()
turtle.width(6)
turtle.goto(0, 80)

turtle.width(8)
turtle.color('red', 'red')
turtle.penup()
turtle.goto(45, 70)
turtle.pendown()
turtle.right(90)
arc(45)

turtle.exitonclick()



