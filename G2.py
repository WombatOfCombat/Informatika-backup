import tkinter,random
from tkinter import *
root=Tk()
v=0
t=60
x1=0
y1=0
x2=10
y2=10
W=500
H=500
xo1=0
xo2=0
yo1=0
yo2=0
points=0
xos=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500]
AC=False
c = Canvas(root,width=W, height=H, bg='black')
c.pack(pady=20)
c.create_rectangle(x1,y1,x2,y2,fill='blue',tags=('sprite','object'))
c.create_text(W/2,H/2,text='press any key to start',fill='white',tags='smsg')
def controls1(event):
    global x1,y1,x2,y2,AC,points,xo1,xo2,yo1,yo2,t
    if AC==True:
        if event.char=='a':
                if x1==x2+10:
                    if x1>10:
                        x1-=20
                else:
                    if x1>=10:
                        x1-=10
                c.delete('sprite')
                c.create_rectangle(x1,y1,x2,y2,fill='blue',tags=('sprite','object'))
        elif event.char=='d':
                if x1==x2-10:
                    if x1<490:
                        x1+=20
                else:
                    if x1<=490:
                        x1+=10
                c.delete('sprite')
                c.create_rectangle(x1,y1,x2,y2,fill='blue',tags=('sprite','object'))
        elif event.char=='w':
                if y1==y2+10:
                    if y1>10:
                        y1-=20
                else:
                    if y1>=10:
                        y1-=10
                c.delete('sprite')
                c.create_rectangle(x1,y1,x2,y2,fill='blue',tags=('sprite','object'))
        elif event.char=='s':
                if y1==y2-10:
                    if y1<490:
                        y1+=20
                else:
                    if y1<=490:
                        y1+=10
                c.delete('sprite')
                c.create_rectangle(x1,y1,x2,y2,fill='blue',tags=('sprite','object'))
        elif event.keysym=='Left':
                if x2==x1+10:
                    if x2>10:
                        x2-=20
                else:
                    if x2>=10:
                        x2-=10
                c.delete('sprite')
                c.create_rectangle(x1,y1,x2,y2,fill='blue',tags=('sprite','object'))
        elif event.keysym=='Right':
                if x2==x1-10:
                    if x2<490:
                        x2+=20
                else:
                    if x2<=490:
                        x2+=10
                c.delete('sprite')
                c.create_rectangle(x1,y1,x2,y2,fill='blue',tags=('sprite','object'))
        elif event.keysym=='Up':
                if y2==y1+10:
                    if y2>10:
                        y2-=20
                else:
                    if y2>=10:
                        y2-=10
                c.delete('sprite')
                c.create_rectangle(x1,y1,x2,y2,fill='blue',tags=('sprite','object'))
        elif event.keysym=='Down':
                if y2==y1-10:
                    if y2<490:
                        y2+=20
                else:
                    if y2<=490:
                        y2+=10
                c.delete('sprite')
                c.create_rectangle(x1,y1,x2,y2,fill='blue',tags=('sprite','object'))
        elif event.char=='r':
            AC=False
            t=60
            c.create_text(W/2,H/2,text='press any key to restart',fill='white',tags='smsg')
    else:
        c.delete('smsg')
        AC=True
        c.after(0,objective)
        t=60
        c.after(0,timer)
        v=0
        x1=0
        y1=0
        x2=10
        y2=10
        xo1=0
        xo2=0
        yo1=0
        yo2=0
        points=0
        c.delete('points')
        c.create_text(W/2,H/25,text='points:{}'.format(points),fill='white',tags='points')
    if (((x1==xo1 and y1==yo1) and (x2==xo2 and y2==yo2)) or ((x1==xo2 and y1==yo2) and (x2==xo1 and y2==yo1))) or (((x1==xo1 and y1==yo2) and (x2==xo2 and y2==yo1)) or ((x1==xo2 and y1==yo1) and (x2==xo1 and y2==yo2))):
        t=t+5
        c.after(0,objective)
        points=points+1
        c.delete('points')
        c.create_text(W/2,H/25,text='points:{}'.format(points),fill='white',tags='points')

def objective():
    global xo1,xo2,yo1,yo2,t,v
    c.delete('objective')
    xo1=random.choice(xos)
    xo2=random.choice(xos)
    yo1=random.choice(xos)
    yo2=random.choice(xos)
    while (xo1>=xo2 or yo1>=yo2):
        xo1=random.choice(xos)
        xo2=random.choice(xos)
        yo1=random.choice(xos)
        yo2=random.choice(xos)
    c.create_rectangle(xo1,yo1,xo2,yo2,tags='objective',fill='green')
    c.create_rectangle(xo1+5,yo1+5,xo2-5,yo2-5,tags='objective',fill='black')
    c.after(0,timer)
    v=v+1
def timer():
    global t,AC
    c.delete('time')
    c.create_text(20,20,text='time:{}'.format(t),tags='time',fill='white')
    while t>=1 and AC==True:
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        c.after(16)
        c.update()
        t=t-1
        c.delete('time')
        c.create_text(20,20,text='time:{}'.format(t),tags='time',fill='white')
    if t==0:
        AC=False
        c.delete('objective')
        c.delete('sprite')
        c.create_text(W/2,H/2,text='press any key to restart',fill='white',tags='smsg')
        c.create_text(W/2,H/25,text='points:{}'.format(points),fill='white',tags='points')
root.bind("<Key>",controls1)
root.mainloop()