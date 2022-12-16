import turtle
sc=turtle.Screen()
t=turtle.Turtle()


def rec(col,rad):
    t.fillcolor(col)
    t.begin_fill()
    for i in range(2):
        t.forward(450)
        t.left(90)
        t.forward(320)
        t.left(90)
    t.end_fill()


t.goto(-50,-50)
rec('gray',1)

t.penup()
t.goto(-10,180)
t.pendown()
t.pensize(20)
t.pencolor("black")
t.right(90)
t.forward(150)

t.penup()
t.goto(40,150)
t.pendown()
t.pensize(15)
t.pencolor("black")
t.circle(30,360)

t.penup()
t.goto(99,150)
t.pendown()
t.pensize(15)
t.pencolor("black")
t.forward(80)

t.penup()
t.goto(100,70)
t.pendown()
t.circle(-30,180)


t.penup()
t.goto(130,180)
t.pendown()
t.right(90)
t.forward(30)

t.penup()
t.goto(160,180)
t.pendown()
t.circle(-30,120)
t.forward(100)
t.left(90)
t.circle(30,30)
t.forward(50)

t.penup()
t.goto(240,180)
t.pendown()
# t.right(90)
t.forward(30)

t.penup()
t.goto(270,180)
t.pendown()
t.circle(-20,120)
t.forward(120)


t.right(240)
t.penup()
t.goto(330,180)
t.pendown()
t.pensize(15)
t.pencolor("black")
t.forward(65)
t.backward(65)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.backward(50)
t.right(90)
t.forward(80)


turtle.exitonclick()

