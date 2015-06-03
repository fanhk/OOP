__author__ = 'fhk'
import turtle


def draw_square():

    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("red")
    brad.speed(10)

    for i in range(4):
        brad.forward(200)
        brad.right(90)


def draw_circle():

    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("black")
    angie.speed(10)
    angie.circle(100)


def draw_triangle():

    steve = turtle.Turtle()
    steve.shape("square")
    steve.color("green")
    steve.speed(10)

    for i in range(3):
        steve.left(120)
        steve.forward(100)


window = turtle.Screen()
window.bgcolor("white")
draw_square()
draw_circle()
draw_triangle()
window.exitonclick()