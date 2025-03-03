import turtle
wn = turtle.Screen()
wn.bgcolor("green")
pet = turtle.Turtle()
pet.pensize(10)
pet.color("black")
distance = 100
angle = 72
for _ in range(5):
    pet.forward(distance)
    pet.right(angle)
wn.exitonclick()