import tkinter,random
from tkinter import *
DU=0
MUT=0
TV=0
TP=0
UDP=1
EXT=[0]*64
EYT=[0]*64
INITIATION=False
root=Tk()
W=640
H=640
REPT=0
REP=False
points = 0
cost=10
GW=0
EN=0
ERNG = 0
for i in range(64):
    EXT[i]=0
    EYT[i]=0
EN=0
GW=GW+1
REX=[W/16,W/16+W/8,W/16+(W/8)*2,W/16+(W/8)*3,W/16+(W/8)*4,W/16+(W/8)*5,W/16+(W/8)*6,W/16+(W/8)*7]
REY=[H/16,H/16+H/8,H/16+(H/8)*2,H/16+(H/8)*3,H/16+(H/8)*4,H/16+(H/8)*5,H/16+(H/8)*6,H/16+(H/8)*7]
SX = W/16
SY = H/16
L=0
U=0
D=0
R=0
c = Canvas(root,width=W, height=H, bg='black')
c.create_rectangle(SX-W/17,SY-H/17,SX+W/17,SY+H/17,fill='white',tags='sprite')
c.pack(pady=20)
c.create_text(W/2,20,text='press Q to start',tags='init',fill='red',font=('Normal','15','normal'))
c.delete('enemy')
def controls(event):
    if INITIATION==True:
        if (event.char=="a"):
            c.after(0, B1(event))
        elif(event.char=="d"):
            c.after(0,B4(event))
        elif(event.char=="w"):
            c.after(0,B2(event))
        elif(event.char=="s"):
            c.after(0,B3(event))
        elif(event.char=="x"):
            c.after(0,B5())
        elif(event.char=="e"):
            c.after(0,B6(event))
        elif(event.char=="f"):
            c.after(0,B7(event))
        else:
            pass
    else:
        if (event.char=="q"):
            c.after(0, INIT())
        if (event.char=="1"):
            c.after(0, UT())
        if (event.char=="2"):
            c.after(0, UD())
def UD():
    global UDP,TP,DU
    if TP>=500 and DU<5:
        TP=TP-500
        UDP=UDP-0.1
        DU=DU+1
        c.delete('DU')
        c.create_text(W/2,60,text=('press 2 to upgrade delete {}/5'.format(DU)+' cost: 500'),tags='DU',fill='red',font=('Normal','15','normal'))
        c.delete('TPoints')
        c.create_text(80,20,text='total points:{}'.format(TP),tags='TPoints',fill='red',font=('Normal','15','normal'))
def UT():
    global MUT,TP,TV
    if TP>=250 and MUT<5:
        TP=TP-250
        MUT=MUT+1
        TV=TV+1
        c.delete('TP')
        c.create_text(W/2,40,text=('press 1 to upgrade teleport {}/5'.format(TV)+' cost: 250'),tags='TP',fill='red',font=('Normal','15','normal'))
        c.delete('TPoints')
        c.create_text(80,20,text='total points:{}'.format(TP),tags='TPoints',fill='red',font=('Normal','15','normal'))
def INIT():
    global INITIATION,REPT,REP,points,cost,GW,EN,ERNG,EXT,EYT,SX,SY,L,U,D,R,H,W
    INITIATION=True
    c.delete('init')
    REPT=0
    REP=False
    points = 0
    cost=10
    GW=0
    EN=0
    ERNG = 0
    for i in range(64):
        EXT[i]=0
        EYT[i]=0
    c.delete('enemy')
    SX = W/16
    SY = H/16
    L=0
    U=0
    D=0
    R=0
    c.delete('TP')
    c.delete('EndMessage')
    c.delete('sprite')
    c.delete('points')
    c.delete('TPoints')
    c.delete('DU')
    c.create_rectangle(SX-W/17,SY-H/17,SX+W/17,SY+H/17,fill='white',tags='sprite')
def enemy():
    global GW,EN,ERNG,EXT,EYT
    if EN == 62:
        c.delete('enemy')
        EXT=[0]*64
        EYT=[0]*64
        EN=0
        GW+=1
    EC =0
    EXT[EN]=random.choice(REX)
    EYT[EN]=random.choice(REY)
    EX=EXT[EN]
    EY=EYT[EN]
    for i in range (64):
            if i==EN:
                pass
            else:
                if EX==EXT[i] and EY==EYT[i]:
                    EC=1
                else:
                    pass
    while (EX==SX and EY==SY) or EC==1:
        EC=0
        EXT[EN]=random.choice(REX)
        EYT[EN]=random.choice(REY)
        EX=EXT[EN]
        EY=EYT[EN]
        for i in range (64):
            if i==EN:
                pass
            elif EX==EXT[i] and EY==EYT[i]:
                EC=1
    c.create_rectangle(EX-W/16,EY-H/16,EX+W/16,EY+H/16,fill='grey',tags=('enemy','enemy{}'.format(EN)))
    c.create_rectangle(EX-W/32,EY-H/32,EX+W/32,EY+H/32,fill='black',tags=('enemy','enemy{}'.format(EN)))
    c.create_rectangle(EX-W/64,EY-H/64,EX+W/64,EY+H/64,fill='grey',tags=('enemy','enemy{}'.format(EN)))
    EN = EN+1
    ERNG = 0
def B1(event):
    global REPT,REP,i,SY,SX,ERNG,points,L,U,D,R
    SDV1=0
    i=0
    for i in range (64):
        if SX-W/8==EXT[i] and SY==EYT[i]:
            SDV1=1
    if SDV1==1:
        pass
    else:
        if SX == W/16:
            pass
        else:
            if REP==True:
                points=points-5
                REP=False
                REPT=0
            SX=SX-W/8
            c.delete('sprite')
            c.create_rectangle(SX-W/17,SY-H/17,SX+W/17,SY+H/17,fill='white',tags='sprite')
            if L==1:
                points = points+1
            c.delete('points')
            c.create_text(SX,SY,text=str(points),tags='points',fill='black',font=('Normal','15','normal'))
            ERNG=ERNG+0.5
            if ERNG==1:
                c.after(0, enemy)
            L=1
            U=0
            D=0
            R=0
def B2(event):
    global REPT,REP,i,SY,SX,ERNG,points,L,U,D,R
    i=0
    SDV2=0
    for i in range (64):
        if SY-H/8==EYT[i] and SX==EXT[i]:
            SDV2=1
    if SDV2==1:
        print('triggered')
    else:
        if SY == H/16:
            pass
        else:
            if REP==True:
                points=points-5
                REP=False
                REPT=0
            SY=SY-H/8
            c.delete('sprite')
            c.create_rectangle(SX-W/17,SY-H/17,SX+W/17,SY+H/17,fill='white',tags='sprite')
            if U==1:
                points = points+1
            c.delete('points')
            c.create_text(SX,SY,text=str(points),tags='points',fill='black',font=('Normal','15','normal'))
            ERNG=ERNG+0.5
            if ERNG==1:
                c.after(0, enemy)
            L=0
            U=1
            D=0
            R=0
def B3(event):
    global REPT,REP,i,SY,SX,ERNG,points,L,U,D,R
    i=0
    SDV3=0
    for i in range (64):
        if SY+H/8==EYT[i] and SX==EXT[i]:
            SDV3=1
    if SDV3==1:
        pass
        print('triggered')
    else:
        if SY == H - H/16:
            pass
        else:
            if REP==True:
                points=points-5
                REP=False
                REPT=0
            SY=SY+H/8
            c.delete('sprite')
            c.create_rectangle(SX-W/17,SY-H/17,SX+W/17,SY+H/17,fill='white',tags='sprite')
            if D==1:
                points = points+1
            c.delete('points')
            c.create_text(SX,SY,text=str(points),tags='points',fill='black',font=('Normal','15','normal'))
            ERNG=ERNG+0.5
            if ERNG==1:
                c.after(0, enemy)
            L=0
            U=0
            D=1
            R=0
def B4(event):
    global REPT,REP,i,SY,SX,ERNG,points,L,U,D,R
    SDV4=0
    i=0
    for i in range (64):
        if SX+W/8==EXT[i] and SY==EYT[i]:
            SDV4=1
    if SDV4==1:
        pass
    else:
        if SX == W - W/16:
            pass
        else:
            if REP==True:
                points=points-5
                REP=False
                REPT=0
            SX=SX+W/8
            c.delete('sprite')
            c.create_rectangle(SX-W/17,SY-H/17,SX+W/17,SY+H/17,fill='white',tags='sprite')
            if R==1:
                points = points+1
            c.delete('points')
            c.create_text(SX,SY,text=str(points),tags='points',fill='black',font=('Normal','15','normal'))
            ERNG=ERNG+0.5
            if ERNG==1:
                c.after(0, enemy)
            L=0
            U=0
            D=0
            R=1
def B5():
    global INITIATION,points,GW,TP,DU
    for N1 in range (64):
        if EXT[N1]==0:
            points=points+0.5
    points = points + 5*GW
    c.delete('points')
    TP=TP+points
    c.create_text(W/2,H/2,text=str(points),tags='EndMessage',fill='red',font=('Normal','30','normal'))
    c.create_text(W/2,H/2-100,text='GAME OVER',tags='EndMessage',fill='red',font=('Normal','30','normal'))
    c.create_text(W/2,H/2+100,text='WINS:{}'.format(GW),tags='EndMessage',fill='red',font=('Normal','30','normal'))
    c.create_text(W/2,20,text='press Q to start',tags='init',fill='red',font=('Normal','15','normal'))
    c.create_text(W/2,40,text=('press 1 to upgrade teleport {}/5'.format(TV)+' cost: 250'),tags='TP',fill='red',font=('Normal','15','normal'))
    c.create_text(W/2,60,text=('press 2 to upgrade delete {}/5'.format(DU)+' cost: 500'),tags='DU',fill='red',font=('Normal','15','normal'))
    c.create_text(80,20,text='total points:{}'.format(TP),tags='TPoints',fill='red',font=('Normal','15','normal'))
    INITIATION = False
def B6(event):
    global cost,points,EN,SX,SY,UDP
    if points>cost:
        points=points-cost
        EN=EN-1
        c.delete('enemy{}'.format(EN))
        EXT[EN]=0
        EYT[EN]=0
        c.delete('points')
        c.create_text(SX,SY,text=str(points),tags='points',fill='black',font=('Normal','15','normal'))
        cost=cost+UDP
    else:
        pass
def B7(event):
    global REPT,REP,points,SX,SY,REX,REY,TV
    if points>=5:
        CV1= True
        CV2= False
        REP= True
        if REP==True:
            REPT=REPT+1
            if REPT>TV:
                points=points-1
            else:
                pass
        SX=REX[random.randint(0,7)]
        SY=REY[random.randint(0,7)]
        while CV1==True or CV2==True:
            CV1= False
            CV2= False
            for N2 in range(64):
                if SX==EXT[N2] and SY==EYT[N2]:
                    CV2=True
                    SX=REX[random.randint(0,7)]
                    SY=REY[random.randint(0,7)]
        c.delete('sprite')
        c.create_rectangle(SX-W/17,SY-H/17,SX+W/17,SY+H/17,fill='white',tags='sprite')
        c.delete('points')
        c.create_text(SX,SY,text=str(points),tags='points',fill='black',font=('Normal','15','normal'))
root.bind("<Key>",controls)
root.mainloop()
