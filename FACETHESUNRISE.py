import tkinter,random,math
from tkinter import *
root = Tk()
H=600
W=600
c = Canvas(root,bg = "black",height=H, width=W)
def one():
    for i in range(1000):
        lazy=random.randint(0,4)
        if lazy==0:
            c.create_line(random.randint(290,310),random.randint(290,310),0,random.randint(0,600),fill='white')
        elif lazy==1:
            c.create_line(random.randint(290,310),random.randint(290,310),600,random.randint(0,600),fill='white')
        elif lazy==2:
            c.create_line(random.randint(290,310),random.randint(290,310),random.randint(0,600),0,fill='white')
        elif lazy==3:
            c.create_line(random.randint(290,310),random.randint(290,310),random.randint(0,600),600,fill='white')
button_frame = tkinter.Frame(root)
button_frame.pack(side='bottom')
b1 = tkinter.Button(button_frame, text='1', command=one) 
b1.pack(side='left')
c.pack()
root.mainloop()
