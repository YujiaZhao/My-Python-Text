import turtle as t
import random
t.setup(650,500,200,200)
t.bgcolor('#00008B')

def star():
    t.pencolor('yellow')
    t.pensize(3)
    t.speed(100)
    a = 0
    while a<50:
        a=a+1
        t.up()
        t.goto(random.randint(-300,300),random.randint(-300,300))
        t.down()
        i = 0
        while i < 5:
            t.fd(15)  # fd 边长
            t.left(144)  # left 角度
            i = i+1
def moon():
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
def doctor():
    t.pencolor('black')
    t.fillcolor('black')
    t.begin_fill()         
    t.fd(120)
    t.lt(90)
    t.fd(100)
    t.circle(60,180)
    t.fd(100)
    t.end_fill()


    t.lt(90)
    t.fd(30)
    t.pencolor('white')
    t.fillcolor('white')
    t.begin_fill()
    t.rt(110)
    t.fd(100)
    t.lt(110)
    t.fd(130)
    t.lt(110)
    t.fd(100)
    t.end_fill()
    t.lt(70)
    t.penup()
    t.fd(30)
    t.pendown()

    t.pencolor('blue')
    t.pensize('10')
    t.lt(90)
    t.fd(90)
    t.bk(60)
    t.lt(90)
    t.fd(35)
    t.bk(70)
    t.pencolor('white')
    t.pensize('20')

    t.rt(150)
    t.fd(60)
    t.bk(60)
    t.penup()
    t.lt(150)
    t.fd(70)
    t.rt(30)
    t.pendown()
    t.fd(60)
    t.bk(60)

    t.rt(60)
    t.penup()
    t.fd(60)

    t.rt(90)
    t.fd(15)
    t.lt(90)
    t.pendown()
    t.fd(50)
    t.dot(20,'brown')

    t.penup()
    t.bk(50)
    t.rt(90)
    t.fd(40)
    t.lt(90)
    t.pendown()
    t.fd(50)
    t.dot(20,'brown')

    t.penup()
    t.pensize(1)
    t.bk(280)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.lt(90)
    t.fd(40)
    t.lt(60)
    t.fd(40)
    t.lt(90)
    t.circle(80,60)
    t.lt(90)
    t.fd(40)
    t.end_fill()

    t.penup()
    t.lt(60)
    t.fd(20)
    t.lt(90)
    t.fd(10)
    t.pensize(10)
    t.pencolor('red')
    t.pendown()
    t.fd(25)
    t.bk(12.5)
    t.rt(90)
    t.fd(12.5)
    t.bk(25)


moon()
star()
t.penup()
t.home()
t.pendown()
doctor()

