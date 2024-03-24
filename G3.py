import tkinter
from tkinter import *
root=Tk()
ST=True
RW=0
GW=0
PT=1
W=700
H=700
V=[0]*9
GE=False
c = Canvas(root,width=W, height=H, bg='black')
c.pack(pady=20)
c.create_line(250,50,250,650,fill='white')
c.create_line(450,50,450,650,fill='white')
c.create_line(50,250,650,250,fill='white')
c.create_line(50,450,650,450,fill='white')
def restart():
    global PT,V,RW,GW,ST,GE
    ST=True
    PT=1
    V=[0]*9
    GE=False
    c.delete('all')
    c.create_line(250,50,250,650,fill='white')
    c.create_line(450,50,450,650,fill='white')
    c.create_line(50,250,650,250,fill='white')
    c.create_line(50,450,650,450,fill='white')
    c.create_text(25,350,text=RW,fill='red')
    c.create_text(675,350,text=GW,fill='green',font=('bold',10))
def controls(coords):
    global PT,V,RW,GW,ST,GE
    x=coords.x
    y=coords.y
    if GE==True:
        restart()
    else:
        if 250>=x>=50 and 250>=y>=50:
            if V[0]==0:
                if PT==1:
                    c.create_line(75,75,225,225,width=10,fill='red')
                    c.create_line(225,75,75,225,width=10,fill='red')
                    V[0]=1
                else:
                    c.create_oval(75,75,225,225,width=10,outline='green')
                    V[0]=2
            else:
                ST=False
        elif 250>=x>=50 and 450>=y>=250:
            if V[1]==0:
                if PT==1:
                    c.create_line(75,275,225,425,width=10,fill='red')
                    c.create_line(225,275,75,425,width=10,fill='red')
                    V[1]=1
                else:
                    c.create_oval(75,275,225,425,width=10,outline='green')
                    V[1]=2
            else:
                ST=False
        elif 250>=x>=50 and 650>=y>=450:
            if V[2]==0:
                if PT==1:
                    c.create_line(75,475,225,625,width=10,fill='red')
                    c.create_line(225,475,75,625,width=10,fill='red')
                    V[2]=1
                else:
                    c.create_oval(75,475,225,625,width=10,outline='green')
                    V[2]=2
            else:
                ST=False
        elif 450>=x>=250 and 250>=y>=50:
            if V[3]==0:
                if PT==1:
                    c.create_line(275,75,425,225,width=10,fill='red')
                    c.create_line(425,75,275,225,width=10,fill='red')
                    V[3]=1
                else:
                    c.create_oval(275,75,425,225,width=10,outline='green')
                    V[3]=2
            else:
                ST=False
        elif 450>=x>=250 and 450>=y>=250:
            if V[4]==0:
                if PT==1:
                    c.create_line(275,275,425,425,width=10,fill='red')
                    c.create_line(425,275,275,425,width=10,fill='red')
                    V[4]=1
                else:
                    c.create_oval(275,275,425,425,width=10,outline='green')
                    V[4]=2
            else:
                ST=False
        elif 450>=x>=250 and 650>=y>=450:
            if V[5]==0:
                if PT==1:
                    c.create_line(275,475,425,625,width=10,fill='red')
                    c.create_line(425,475,275,625,width=10,fill='red')
                    V[5]=1
                else:
                    c.create_oval(275,475,425,625,width=10,outline='green')
                    V[5]=2
            else:
                ST=False
        elif 650>=x>=450 and 250>=y>=50:
            if V[6]==0:
                if PT==1:
                    c.create_line(475,75,625,225,width=10,fill='red')
                    c.create_line(625,75,475,225,width=10,fill='red')
                    V[6]=1
                else:
                    c.create_oval(475,75,625,225,width=10,outline='green')
                    V[6]=2
            else:
                ST=False
        elif 650>=x>=450 and 450>=y>=250:
            if V[7]==0:
                if PT==1:
                    c.create_line(475,275,625,425,width=10,fill='red')
                    c.create_line(625,275,475,425,width=10,fill='red')
                    V[7]=1
                else:
                    c.create_oval(475,275,625,425,width=10,outline='green')
                    V[7]=2
            else:
                ST=False
        elif 650>=x>=450 and 650>=y>=450:
            if V[8]==0:
                if PT==1:
                    c.create_line(475,475,625,625,width=10,fill='red')
                    c.create_line(625,475,475,625,width=10,fill='red')
                    V[8]=1
                else:
                    c.create_oval(475,475,625,625,width=10,outline='green')
                    V[8]=2
            else:
                ST=False
        else:
            ST=False
        if V[0]==V[1]==V[2]==1 or V[3]==V[4]==V[5]==1 or V[6]==V[7]==V[8]==1 or V[0]==V[3]==V[6]==1 or V[1]==V[4]==V[7]==1 or V[2]==V[5]==V[8]==1 or V[0]==V[4]==V[8]==1 or V[2]==V[4]==V[6]==1:
            RW+=1
            GE=True
            c.delete('victorytext')
            c.create_text(350,350,text='RED WINS',fill='white',tags=('victorytext','all'),font=('bold',60))
        elif V[0]==V[1]==V[2]==2 or V[3]==V[4]==V[5]==2 or V[6]==V[7]==V[8]==2 or V[0]==V[3]==V[6]==2 or V[1]==V[4]==V[7]==2 or V[2]==V[5]==V[8]==2 or V[0]==V[4]==V[8]==2 or V[2]==V[4]==V[6]==2:
            GW+=1
            GE=True
            c.delete('victorytext')
            c.create_text(350,350,text='GREEN WINS',fill='white',tags=('victorytext','all'),font=('bold',60))
        elif V[0]!=0 and V[1]!=0 and V[2]!=0 and V[3]!=0 and V[4]!=0 and V[5]!=0 and V[6]!=0 and V[7]!=0 and V[8]!=0:
            GE=True
            c.delete('victorytext')
            c.create_text(350,350,text='DRAW',fill='white',tags=('victorytext','all'),font=('bold',60))
        if PT==1 and ST==True:
            PT=0
            c.delete('turn')
            c.create_text(350,675,text='green',fill='green',tags='turn',font=('bold',40))
        elif PT==0 and ST==True:
            PT=1
            c.delete('turn')
            c.create_text(350,675,text='red',fill='red',tags='turn',font=('bold',40) )
        ST=True
root.bind("<Button-1>",controls)
root.mainloop()
