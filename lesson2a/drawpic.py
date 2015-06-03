__author__ = 'fhk'
import turtle


def draw_square(turtle_name):

    for i in range(4):
        turtle_name.forward(200)
        turtle_name.right(90)


def draw(turtle_name):

    for i in range(36):
        draw_square(turtle_name)
        # turtle_name.circle(150)
        turtle_name.right(10)


brad = turtle.Turtle()
brad.shape("turtle")
brad.color("red")
brad.speed(100)

window = turtle.Screen()
draw(brad)
window.exitonclick()