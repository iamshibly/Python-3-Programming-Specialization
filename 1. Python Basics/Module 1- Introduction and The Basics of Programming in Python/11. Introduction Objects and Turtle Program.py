#Turtle and Screen are class
import turtle #module named turtle, turtle is a library
wn = turtle.Screen()
wn.bgcolor("green")
Alex = turtle.Turtle()#alex is an object, shibly and wn are objects
Alex.pensize(10)#penszie, color, forward, bfcolors are method
Alex.color("gold")
Alex.forward(200)
Alex.left(90)
Alex.forward(200)
Alex.left(90)
Alex.forward(200)
Alex.salary = 50000#instance variables
print(Alex.salary)
#all these are methos of object Alex
#instance. we can have as many as turtle we want
shibly = turtle.Turtle()
shibly.pensize(10)
shibly.color("pink")
shibly.left(180)
shibly.forward(200)
shibly.right(90)
shibly.forward(200)
shibly.right(90)
shibly.forward(200)
wn.exitonclick()
