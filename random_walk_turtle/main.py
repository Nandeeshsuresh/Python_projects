import turtle
from turtle import Turtle, Screen
import random

tury=Turtle()
screen=Screen()


tury.width(6)
tury.speed(0)
right_or_left = [0,90,180,270]
turtle.colormode(255)

def random_colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

for iteration in range(1000):
   random_color=random_colors()
   right_left=random.choice(right_or_left)
   if right_left == 0:
       tury.right(90)
   elif right_left ==90 :
       tury.left(90)
   elif right_left == 180:
      tury.left(180)
   elif right_or_left == 270:
      tury.right(180)
   tury.color(random_color)
   tury.forward(30)



screen.exitonclick()

