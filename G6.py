import tkinter,math,random
from tkinter import *
root=Tk()
W=600
H=600
c = Canvas(root,width=W, height=H, bg='black')
c.pack(pady=20)
ec=[random.randint(1,W/40-1)*40,random.randint(1,H/40-1)*40]
completed=[]
def controls(coordinates):
    global ec,completed
    c.delete('pointers')
    cf=0
    vector=[ec[0]-coordinates.x,ec[1]-coordinates.y]
    dp=distance([ec[0],ec[1]],[coordinates.x,coordinates.y])+1
    for x in range(40,W-40+1,40):
        for y in range(40,H-40+1,40):
            dc=distance([x,y],[coordinates.x,coordinates.y])+1
            cf=dc/25
            color="#{:02x}{:02x}{:02x}".format(int((1 + math.sin(0.3*cf)) * 127),int((1 + math.sin(0.3*cf + 2)) * 127),int((1 + math.sin(0.3*cf+4)) * 127))
            if [x,y] not in completed:
                c.create_line(x-vector[0]/(dp/7),y-vector[1]/(dp/7),x+vector[0]/(dp/7),y+vector[1]/(dp/7),fill=color,tags='pointers',width=1)
            else:
                c.create_oval(x-5,y-5,x+5,y+5,fill=color,tags='pointers',width=1)
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def find(coordinates):
    global ec,completed
    if distance([ec[0],ec[1]],[coordinates.x,coordinates.y])<=5:
        completed.append(ec)
        if len(completed)==int((W/40-1)*(H/40-1)):
            c.create_text(W/2,H/2,text='congratulations now get a life',fill='white',tags='endtxt')
        else:
            ec=[random.randint(1,W/40-1)*40,random.randint(1,H/40-1)*40]
            while ec in completed:
                ec=[random.randint(1,W/40-1)*40,random.randint(1,H/40-1)*40]
    else:
        completed=[]
        c.delete('endtxt')
root.bind("<Motion>",controls)
root.bind("<Button-1>",find)
root.mainloop()