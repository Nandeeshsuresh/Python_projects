import turtle
from turtle import Turtle, Screen
import random


tury=Turtle()
angle=0
tury.speed(0)
turtle.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

def spirograph(size_of_gap):
      for iteration in range(int(360 / size_of_gap)):
         tury.color(random_color())
         tury.circle(100)
         tury.setheading(tury.heading()+size_of_gap)

spirograph(5)



screen=Screen()
screen.exitonclick()