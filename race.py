import random
import turtle as t


s = t.Screen()
s.setup(width=500,height=400)
bet = s.textinput(title="Make your bet", prompt="wh will win the race? Enter a color?: ")
# print(bet)

c = ["green","blue","red","purple","orange","black"]
ya = [10, 50, 90, 130, -30, -70]
all = []
for i in range(0,6):
    tu = t.Turtle(shape="turtle")
    tu.color(c[i])
    tu.penup()
    tu.goto(x=-200,y=ya[i])
    all.append(tu)

end = False
while not end:
    for j in all:
        j.forward(random.randint(0, 10))
        if j.xcor() > 220:
            w = j.pencolor()
            end = True
            if w == bet:
                print(f"You've won! the {w} turtle is the winner")
            else:
                print(f"You've lost! the {w} turtle is the winner")



s.exitonclick()