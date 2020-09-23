import turtle as t
from random import *

t.shape('turtle')
t.color('green', 'yellow')
t.speed(10)

while (True):
    t.forward(randint(5, 50))
    t.left(randint(0, 360))

t.exitonclick()
