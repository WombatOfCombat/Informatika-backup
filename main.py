import tkinter as tk
import numpy as geek
import time,math

# Create a Tkinter window
root = tk.Tk()
root.title("Color Rotation")
c = tk.Canvas(root, width=600, height=600)
c.pack()

colrot1 = 0
colrot2 = 0
def rgb_rotation(steps):
    colors = []
    for i in range(steps):
        red = int((1 + math.sin(i/255)) * 127)
        green = int((1 + math.sin(i/255 + 2)) * 127)
        blue = int((1 + math.sin(i/255 + 4)) * 127)
        color_hex = "#{:02x}{:02x}{:02x}".format(red, green, blue)
        c.after(1,c.delete('color'))  # Clear previous rectangle
        c.create_rectangle(0, 0, 600, 600, fill=color_hex, tags='color')
        c.update()
c.after(0,rgb_rotation(100000))
