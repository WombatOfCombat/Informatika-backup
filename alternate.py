import tkinter,math
from tkinter import *
root=Tk()
W=1900
H=1000
c = Canvas(root,width=W, height=H, bg='black')
c.pack(pady=20)
run1=True
def controls(coordinates):
    global run1
    c.delete('pointers')
    cf=0
    for x in range(0,W+1,10):
        for y in range(0,H+1,10):
            dp=distance([x,y],[round(coordinates.x),round(coordinates.y)])+1
            cf=dp/50
            color="#{:02x}{:02x}{:02x}".format(int((1 + math.sin(0.3*cf)) * 127),int((1 + math.sin(0.3*cf + 2)) * 127),int((1 + math.sin(0.3*cf+4)) * 127))
            c.create_rectangle(x,y,x+10,y+10,fill=color,outline=color,tags='pointers')
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
root.bind("<Motion>",controls)
root.mainloop()