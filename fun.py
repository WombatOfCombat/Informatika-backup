import tkinter,random,math
from tkinter import *
root = Tk()
H=1000
W=1500
c = Canvas(root,bg = "black",height=H, width=W)
c.pack(pady=20)
colrot=0
def motion(event):
    global colrot
    colrot+=H//40
    colrot_memory=colrot
    c.delete('lines')
    xm,ym=event.x,event.y
    for x in range(0,W+1,40):
        for y in range(0,H+1,40):
            dist=distance([x,y],[xm,ym])/7+1
            colrot+=1
            vector=[x-xm,y-ym]
            r = int((1 + math.sin(colrot/255)) * 127)
            g = int((1 + math.sin(colrot/255 + 2)) * 127)
            b = int((1 + math.sin(colrot/255 + 4)) * 127)
            color="#{:02x}{:02x}{:02x}".format(r,g,b)
            c.create_line(x+vector[0]/dist,y+vector[1]/dist,x-vector[0]/dist,y-vector[1]/dist,fill=color,tags='lines',width=1)#+dist%50*2)
    colrot=colrot_memory
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def check():
    pass
root.bind('<Motion>', motion)
root.bind("<Button-1>",check)
root.mainloop()