import turtle

screen = turtle.Screen()
screen.bgcolor("white")
turtle.speed(0)
turtle.penup()


def draw_rectangle(color, x, y, width, height):
    turtle.goto(x, y)
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()


draw_rectangle("blue", -300, 150, 600, 150)
draw_rectangle("yellow", -300, 0, 600, 150)

turtle.goto(-180, -180)
turtle.color("black")
turtle.write("Happy Independence Day, Ukraine!", font=("Arial", 16, "normal"))

turtle.hideturtle()
turtle.done()
