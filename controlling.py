import turtle as t
tu = t.Turtle()
s = t.Screen()

def mf():
    tu.setheading(0)
    tu.forward(50)
def mb():
    tu.setheading(180)
    tu.forward(50)
def mc():
    tu.setheading(270)
    tu.forward(50)
def mcc():
    tu.setheading(90)
    tu.forward(50)
def mo():
    # tu.setheading(90)
    tu.circle(50)
def cl():
    # tu.setheading(90)
    tu.penup()
    tu.home()
    tu.clear()
    tu.pendown()
def cvl():
    nh1 = tu.heading() + 10
    tu.setheading(nh1)
def cvr():
    nh2 = tu.heading() - 10
    tu.setheading(nh2)
def fd():
    tu.forward(50)
def bd():
    tu.backward(50)


s.listen()
s.onkey(key="d", fun=mf)
s.onkey(key="a", fun=mb)
s.onkey(key="s", fun=mc)
s.onkey(key="w", fun=mcc)
s.onkey(key="o", fun=mo)
s.onkey(key="c", fun=cl)
s.onkey(key="l", fun=cvl)
s.onkey(key="r", fun=cvr)
s.onkey(key="f", fun=fd)
s.onkey(key="b", fun=bd)
s.exitonclick()