import turtle

turtle.shape('turtle')
turtle.color('green', 'yellow')
turtle.speed(10000)

def spiral(k, dphi, phi):
    for i in range(1, 1000000, 1):
        dl = k * dphi * (1 + phi**2)**0.5
        turtle.forward(dl)
        turtle.left(dphi * 180 / 3.14159265)
        phi += dphi

spiral(2, 0.1, 0)



