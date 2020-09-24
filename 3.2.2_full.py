import turtle as t

t.shape('turtle')
t.color('green', 'yellow')
t.screensize(3000, 2000)
t.speed(10)

inp = open('input')

Number = [[0,0] for i in range(12)]

for i in range(1, 11, 1):
    num = list(inp.readline().split())
    for j in range(len(num)):
        num[j] = num[j].split(',')
    Number[i] = num
Number[0] = Number[10]

index = [1, 4, 1, 7, 0, 7]
for i in index:
    if (i == 1):
        t.up()
        t.lt(270)
        t.fd(50)
        t.lt(90)
        t.down()
        for angle, step in Number[i]:
            angle, step = float(angle), float(step)
            t.lt(angle)
            t.fd(step)
    else:
        for angle, step in Number[i]:
            angle, step = float(angle), float(step)
            t.lt(angle)
            t.fd(step)
    t.pu()
    t.fd(90)
    t.pd()
    
t.exitonclick()


