import time
from turtle import *
import keyboard

fidget = []
screen = Screen()
screen.title("Fidget Spinner")
screen.tracer(0)
velocity = 0


def create_fidget():
    for angle, colour in zip([0, 120, 240], ["red", "blue", "green"]):
        body = Turtle()
        body.hideturtle()
        body.penup()
        body.speed("fastest")
        body.seth(angle)
        body.fd(60)
        body.shape("circle")
        body.color(colour)
        body.shapesize(stretch_len=4, stretch_wid=4)
        body.showturtle()
        body.seth(angle - 90)
        fidget.append(body)


create_fidget()
screen.update()


def spin(extent):
    for body in fidget:
        body.circle(radius=-60, extent=extent)


def vel_increase():
    global velocity
    if velocity < 180:
        velocity += 0.5


screen.onkeypress(vel_increase, "space")
screen.listen()
while True:
    time.sleep(0.01)
    if velocity > 0:
        spin(velocity)
    if not keyboard.is_pressed('space'):
        if velocity > 0:
            velocity -= 0.15
    screen.update()
