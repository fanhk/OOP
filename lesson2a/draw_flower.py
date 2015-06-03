__author__ = 'fhk'
import turtle


def draw_diamond(turtle_name):

    for i in range(2):
        turtle_name.forward(100)
        turtle_name.left(40)
        turtle_name.forward(100)
        turtle_name.left(140)


def draw_main():

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(100)

    window = turtle.Screen()
    for i in range(60):
        draw_diamond(brad)
        brad.right(6)
    # for i in range(100):
    #     draw_diamond(brad)
    #     brad.right(18)
    # draw_diamond(brad)
    brad.right(90)
    brad.forward(250)
    window.exitonclick()


draw_main()