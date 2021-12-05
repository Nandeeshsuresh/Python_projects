# import colorgram
#
# colors = colorgram.extract('image.jpg',84)
#
# print(len(colors))
# print(type(colors))
#
# rgb_list=[]
#
# for color in range(35):
#     color_class = colors[color]
#     r = color_class.rgb.r
#     g = color_class.rgb.g
#     b = color_class.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_list.append(rgb_tuple)
#
# print(rgb_list)
import turtle
from turtle import Turtle,Screen
import random

color_list=[  (203, 165, 108), (239, 245, 240), (235, 238, 244), (154, 74, 47), (222, 201, 136), (51, 93, 124), (171, 153, 40), (138, 31, 20), (132, 162, 185), (199, 91, 71), (47, 122, 88), (14, 100, 73), (146, 178, 147), (94, 73, 75), (72, 48, 39), (234, 176, 164), (162, 143, 158), (55, 46, 50), (184, 205, 172), (19, 85, 88), (42, 62, 74), (147, 20, 23), (85, 145, 127), (183, 86, 88), (45, 66, 84), (107, 127, 152), (221, 172, 176), (14, 72, 67), (176, 191, 210), (175, 197, 204), (105, 137, 142), (68, 64, 58), (248, 195, 5)]
print(len(color_list))
tury=Turtle()
turtle.colormode(255)
tury_upward=-260
tury.speed(0)
tury.hideturtle()               

def tury_displacement():
     global tury_upward
     tury_upward+=50
     tury.hideturtle()
     tury.penup()
     tury.goto(-220,tury_upward)
     tury.pendown()


def tury_painting():
     for iteration in range(10):
         tury.dot(20,color_list[random.randint(0,32)])
         tury.penup()
         tury.forward(50)
         tury.pendown()

for iteration in range(10):
   tury_displacement()
   tury_painting()






screen=Screen()
screen.exitonclick()
