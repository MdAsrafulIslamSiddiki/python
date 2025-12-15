import turtle
from turtle import *
wn = Screen()
wn.bgcolor("black")
t=turtle.Turtle()
t.pencolor('white')
def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)
def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

heart()
t.ht()

def write( message,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    # style=('Stencil Std',18,'italic')
    t.write(message,font=('Stencil Std',18,'italic'))

write('I', (-68,95))
write('L', (-55,95))
write('o', (-42,95))
write('v', (-30,95))
write('e', (-14,95))
write('y', (10,95))
write('o', (26,95))
write('u', (45,95))

write('A', (-32,55))
write('F', (-14,55))
write('S', (4,55))
write('U', (22,55))
wn.mainloop()