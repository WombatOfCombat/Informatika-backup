import tkinter,random,winsound
from tkinter import *
root=Tk()
W=1500
H=900
names=['Laura','Simona','Samo','Liliana','Mima','Miro','Destiny','Ema','Tamara','Alex','Tatiana','Kaja','Natalia','Saša']
farba=['red','orange','yellow','green','blue','violet','pink']
finalmessage=['your time has come','we will see you in the next life','a worthy sacrifice','death seeks you','there is no escape now','may you rest in peace','tough luck']
c = Canvas(root,width=W, height=H, bg='black')
c.pack(pady=20)
c.create_text(W/2,H/2,text='Click to condemn.',tags='name',fill='white',font=('bold',60))
def main(coords):
    x=coords.x
    y=coords.y
    for i in range(34):
        c.delete('name')
        c.create_text(W/2,H/3,text=names[random.randint(0,13)],fill=farba[random.randint(0,6)],tags='name',font=('bold',60))
        c.update()
        winsound.Beep(800,100)
        c.after(100+i*i)
    c.create_text(W/2,H/3*2,text=finalmessage[random.randint(0,6)],fill='red',tags='name',font=('bold',60))
root.bind("<Button-1>",main)
root.mainloop()