import turtle
wn = turtle.Screen()
se = turtle.Turtle()
se.pencolor("pink")
se.right(170)
colors=["yellow","red","pink","blue","red","pink","yellow","pink","blue","red"]
for color in colors:
    if se.pencolor()=="red":
        se.forward(50)
        se.left(30)
    elif se.pencolor()=="blue":
        se.backward(80)
        se.right(90)
    elif se.pencolor()=="pink":
        se.forward(40)
        se.left(70)
    elif se.pencolor()=="yellow":
        se.backward(120)
        se.right(60)
    se.pencolor(color)