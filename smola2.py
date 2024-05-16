import tkinter
import random
root = tkinter.Tk()
H = 100
W = 200
c = tkinter.Canvas(root, bg="black", height=H, width=W)
def uloha1():
    c.delete('all')
    cislo=int(entry.get())
    if cislo%7==0:
        txt_1='je delitelne cislom 7'
    else:
        txt_1='nie je delitelne cislom 7'
    if cislo%2==0:
        txt_2='je parne'
    else:
        txt_2='je neparne'
    c.create_text(W//2,H//2,text='cislo {} a {}'.format(txt_1,txt_2),fill='white')
def uloha2():
    c.delete('all')
    c1=eval(entry.get())
    c2=eval(entry1.get())
    c.create_text(W//2,H//2,text='{} je maximum, {} je minimum'.format(max(c1,c2),min(c1,c2)),fill='white')
def uloha3():
    c.delete('all')
    c.create_oval(1,1,W+2,H+2,fill='white')
def uloha4():
    c.delete('all')
    res=0
    c3=entry.get()
    for i in range(len(c3)):
        res+=int(c3[i])
    c.create_text(W//2,H//2,text='ciferny sucet je {}'.format(res),fill='white')
def uloha5():
    c.delete('all')
    for i in range(10000):
        x=random.randint(0,W)
        y=random.randint(0,H)
        if x<=W/2 and y<=H/2:
            color='green'
        elif x<=W/2 and y>H/2:
            color='red'
        elif x>=W/2 and y<=H/2:
            color='yellow'
        else:
            color='blue'
        c.create_oval(x-3,y-3,x+3,y+3,fill=color)
def uloha6():
    x=5
    y=20
    r=5
    pocet=0
    while x+r<W:
        pocet+=1
        if pocet%4==0:
            farba='yellow'
        elif pocet%4==1:
            farba='red'
        elif pocet%4==2:
            farba='green'
        elif pocet%4==3:
            farba='blue'
        if pocet%3==0:
            c.create_rectangle(x-r,y-2*r,x+r,y+2*r,fill=farba)
        elif pocet%3==1:
            c.create_oval(x-r,y-r,x+r,y+r,fill=farba)
        else:
            c.create_rectangle(x-r,y-r,x+r,y+r,fill=farba)
        x=x+r+r
button_frame = tkinter.Frame(root)
button_frame.pack(side='bottom')
b1 = tkinter.Button(button_frame, text='1', command=uloha1)
b1.pack(side='left')
b2 = tkinter.Button(button_frame, text='2', command=uloha2)
b2.pack(side='left')
b3 = tkinter.Button(button_frame, text='3', command=uloha3)
b3.pack(side='left')
b4 = tkinter.Button(button_frame, text='4', command=uloha4)
b4.pack(side='left')
b5 = tkinter.Button(button_frame, text='5', command=uloha5)
b5.pack(side='left')
b6 = tkinter.Button(button_frame, text='6', command=uloha6)
b6.pack(side='left')
entry = tkinter.Entry(button_frame)
entry.pack(side='left')
entry1 = tkinter.Entry(button_frame)
entry1.pack(side='left')
c.pack()
root.mainloop()
