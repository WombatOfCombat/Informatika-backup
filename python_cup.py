def min_energy_path_with_path(map_values):
    rows = len(map_values)
    cols = len(map_values[0])

import turtle,random

screen=turtle.Screen()
screen.title("christmas tree")
screen.bgcolor("white")

t=turtle.Turtle()
t.speed(2)
t.color("green")

def equilateral_triangle(side_lenght):
    for _ in range(3):
        t.forward(side_lenght)
        t.left(120)
for i in range(10):
    equilateral_triangle(100)
    t.penup()
    t_location=t.pos()
    t.goto(t_location[0]+random.randint(-5,5),t_location[1]+random.randint(-5,5))
    t.pendown()