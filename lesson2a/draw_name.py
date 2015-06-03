__author__ = 'fhk'
import turtle


def draw_name():

    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")

    brad.penup()
    brad.goto(-200, 200)
    brad.pendown()
    brad.forward(100)

    brad.penup()
    brad.goto(-200, 150)
    brad.pendown()
    brad.forward(100)

    brad.penup()
    brad.goto(-200, 200)
    brad.pendown()
    brad.right(90)
    brad.forward(150)

    brad.penup()
    brad.goto(0, 200)
    brad.pendown()
    brad.right(20)
    brad.forward(160)

    brad.penup()
    brad.goto(0, 200)
    brad.pendown()
    brad.left(40)
    brad.forward(160)

    brad.penup()
    brad.goto(-35, 100)
    brad.pendown()
    brad.left(70)
    brad.forward(73)

    brad.penup()
    brad.goto(150, 200)
    brad.pendown()
    brad.right(90)
    brad.forward(150)

    brad.penup()
    brad.goto(150, 200)
    brad.pendown()
    brad.left(30)
    brad.forward(165)
    brad.left(150)
    brad.forward(150)
    window.exitonclick()


draw_name()