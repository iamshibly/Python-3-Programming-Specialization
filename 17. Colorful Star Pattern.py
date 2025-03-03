import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Super-fast drawing
t.pensize(2)
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# Draw a colorful star pattern
for i in range(36):  # 36 repetitions to make a circular pattern
    t.color(colors[i % len(colors)])  # Cycle through colors
    for _ in range(5):  # Draw a star
        t.forward(100)
        t.right(144)  # Star angle
    t.right(10)  # Rotate for the next star

wn.exitonclick()
