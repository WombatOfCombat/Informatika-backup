import tkinter,math
from tkinter import *
root=Tk()
W=1920
H=1080
c = Canvas(root,width=W, height=H, bg='black')
c.pack(pady=20)
def controls(coordinates):
    global run1
    c.delete('pointers')
    cf=0
    for x in range(0,W+1,40):
        for y in range(0,H+1,40):
            vector=[x-coordinates.x,y-coordinates.y]
            dp=distance([x,y],[coordinates.x,coordinates.y])+1
            cf=dp/100
            color="#{:02x}{:02x}{:02x}".format(int((1 + math.sin(0.3*cf)) * 127),int((1 + math.sin(0.3*cf + 2)) * 127),int((1 + math.sin(0.3*cf+4)) * 127))
            c.create_line(x-vector[0]/(dp/7),y-vector[1]/(dp/7),x+vector[0]/(dp/7),y+vector[1]/(dp/7),fill=color,tags='pointers',width=1)
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
root.bind("<Motion>",controls)
root.mainloop()