import turtle as t

t.shape('turtle')
t.color('green', 'yellow')
t.screensize(300000, 200000)
t.speed(10)

inp = open('input')

t.pu()
t.bk(500)
t.pd()

Number = [[0,0] for n in range (11)]

for i in range(1, 11, 1):
    num = list(inp.readline().split())
    for j in range(len(num)):
        num[j] = num[j].split(',')
    for angle, step in num:
        angle, step = float(angle), float(step)
        t.lt(angle)
        t.fd(step)
    t.pu()
    t.fd(90)
    t.pd()

t.exitonclick()






