for _ in range(3):
    print("Hello")
    print("tayson")
print("Done")
import turtle
wn = turtle.Screen()
wn.bgcolor("red")
Jhon = turtle.Turtle()
Jhon.pensize(10)
Jhon.color("white")
distance=50
angle =90
for _ in range(20):
    Jhon.forward(distance)
    Jhon.right(angle)
    distance = distance+10
    angle = angle - 2

wn.exitonclick()
