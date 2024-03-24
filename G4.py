import tkinter,random
from tkinter import *
root = Tk()
H=600
W=600
c = Canvas(root,bg = "black",height=H, width=W)
c.pack(pady=20)
SX=0
SY=0
EX=0
EY=0
EXT=[0]*64
EYT=[0]*64
GXY=[W/16,W/16+W/8,W/16+(W/8)*2,W/16+(W/8)*3,W/16+(W/8)*4,W/16+(W/8)*5,W/16+(W/8)*6,W/16+(W/8)*7]
def controls(event):
    global SX,SY
    if (event.char=="a"):
        SX-=1
    elif(event.char=="d"):
        SX+=1
    elif(event.char=="w"):
        SY-=1
    elif(event.char=="s"):
        SY+=1
    c.delete('sprite')
    c.create_rectangle(GXY[SX%8]+W/16,GXY[SY%8]+W/16,GXY[SX%8]-W/16,GXY[SY%8]-W/16,fill='green',tags='sprite')
root.bind("<Key>",controls)
root.mainloop()
