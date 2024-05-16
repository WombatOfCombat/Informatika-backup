import tkinter,random,math
from tkinter import *
root = Tk()
colors=['orange','yellow','green','blue','purple']
H=1000
W=1700
c = Canvas(root,bg = "black",height=H, width=W)
def main(event):
    while True:
        c.after(150)
        c.update()
        c.delete('a')
        for j in range(5):
            for i in range(22):
                c.create_rectangle(25+75*i,H-25,75+75*i,H-random.randint(500-(100*j),H-25-(100*j))/(j+1),fill=colors[j],tags='a',outline=colors[j])
c.bind("<Button-1>", main)
c.pack()
root.mainloop()