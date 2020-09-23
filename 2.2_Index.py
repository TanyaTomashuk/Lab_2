import turtle as t

t.shape('turtle')
t.color('green', 'yellow')
t.speed(10)

Zero = [(270, 100), (90, 50), (90, 100), (90, 50), (180, 50)]
One = [(45, 50 * 2**0.5), (225, 100), (180, 100), (270, 0)]
Four = [(270, 50), (90, 50), (270, 50), (180, 100), (270, 0)]
Seven = [(0, 50), (225, 50 * 2**0.5), (45, 50), (180, 50), (315, 50 * 2**0.5),           (315, 0)]

Index = [One, Four, One, Seven, Zero, Zero]

for i in Index:
    if (i == One):
        t.up()
        t.lt(270)
        t.fd(50)
        t.lt(90)
        t.down()
        for angle, step in i:
            t.lt(angle)
            t.fd(step)
        t.up()
        t.fd(30)
        t.down()
    else:
        for angle, step in i:
            t.lt(angle)
            t.fd(step)
    t.up()
    t.fd(30)
    t.down()

t.exitonclick()

