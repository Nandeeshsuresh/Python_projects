# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle,Screen  #here turtle is a module(file)
# tommy = Turtle()                  #Turle and Screen is classses or also calles as classes
# print(tommy)
# tommy.shape("turtle")             #Here shape a method (metod in object oriented programming and function in procedural programming.
#                                   # Method is just a fancy word for Function)
# tommy.color("brown")
# tommy.forward(100)
#
# my_screen=Screen()
# print(my_screen.canvheight)       #canvheight is a attribute(attribute in object oriented programming and variable in procedural programming.
#                                   # Attribute is just a fancy word for Variable)
# my_screen.exitonclick()

from prettytable import PrettyTable  #Pretty table is a package. Package is a collection of modules
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="l"
print(table)
