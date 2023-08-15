from turtle import Turtle, Screen, done

# Set up the turtle screen
screen = Screen()
screen.setup(width=415, height=695)
screen.bgcolor("white")
screen.screensize(1080, 1920)
screen._root.resizable(False, False)

flag = Turtle()

flag.speed(0)
flag.pensize(3)
flag.color("#000080")


def draw(x, y):
    flag.penup()
    flag.goto(x, y)
    flag.pendown()


for i in range(24):
    flag.forward(30)  # Adjusted width
    flag.backward(30)  # Adjusted width
    flag.left(15)

draw(0, -30)  # Adjusted width
flag.circle(30, 360)  # Adjusted width

draw(0, -40)  # Adjusted width

flag.color("#138808")

flag.begin_fill()
flag.forward(150)  # Adjusted length
flag.backward(300)  # Adjusted length
flag.right(90)
flag.forward(60)  # Adjusted width
flag.left(90)
flag.forward(300)  # Adjusted length
flag.left(90)
flag.forward(60)  # Adjusted width
flag.left(90)
flag.end_fill()

draw(-150, 40)  # Adjusted length

flag.color("#FF9933")

flag.begin_fill()
flag.right(90)
flag.forward(60)  # Adjusted width

flag.right(90)
flag.forward(300)  # Adjusted length
flag.right(90)
flag.forward(60)  # Adjusted width
flag.right(90)
flag.forward(300)  # Adjusted length

flag.end_fill()

flag.hideturtle()

done()
