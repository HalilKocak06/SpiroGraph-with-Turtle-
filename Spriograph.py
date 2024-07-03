from turtle import Turtle,Screen
import random

halo = Turtle()
halo.speed("fast")
colours = ["green","red","blue","purple","brown"]

def draw_spirograph(radius ,angle):
    for blank in range(int(360/angle)):
        halo.color(random.choice(colours))
        halo.circle(radius)
        halo.left(angle)

draw_spirograph(100,10)        


screen = Screen()
screen.exitonclick()

