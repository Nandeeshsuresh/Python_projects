from turtle import Turtle, Screen
import random

colors=["light steel blue","salmon","forest green","beige","cornflower blue","brown","dark cyan","black","hot pink","indigo"]

tury=Turtle()
screen=Screen()

tury.color(random.choice(colors))
for time in range(3):
   tury.forward(100)
   tury.right(120)                                          #Triangle=120

tury.color(random.choice(colors))
for time in range(4):
   tury.forward(100)                                     #square=90
   tury.right(90)

tury.color(random.choice(colors))
for time in range(5):
   tury.forward(100)                                    #pentagon=72
   tury.right(72)

tury.color(random.choice(colors))
for time in range(6):
   tury.forward(100)                                    #hexagon= 60
   tury.right(60)

tury.color(random.choice(colors))
for time in range(7):
   tury.forward(100)                                                                # heptagon=51.428
   tury.right(51.428)

tury.color(random.choice(colors))
for time in range(8):
   tury.forward(100)                                                                # octagon=45
   tury.right(45)

tury.color(random.choice(colors))
for time in range(9):
   tury.forward(100)                                                               # nonagon=40
   tury.right(40)

tury.color(random.choice(colors))
for time in range(10):
   tury.forward(100)                                                               # decagon=36
   tury.right(36)

screen.exitonclick()