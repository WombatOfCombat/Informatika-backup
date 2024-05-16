import tkinter,random,math
from tkinter import *
root = Tk()
c = Canvas(root,bg = "black",height=1000, width=1700)
pointcoordsx=[0,700,1000]
pointcoordsy=[0,200,500,800]
pointcoordsx2=[0,350,650]
pointcoordsx3=[0,1050,1350]
def main(event):
    while True:
        c.after(150)
        c.update()
        c.delete('symbol')
        r=random.randint(1,15)
        rc=r
        for i in range(4):
            t=True
            if r==1:
                c.create_line(pointcoordsx[1],pointcoordsy[1],pointcoordsx[1],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==2:
                c.create_line(pointcoordsx[1],pointcoordsy[1],pointcoordsx[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==3:
                c.create_line(pointcoordsx[1],pointcoordsy[1],pointcoordsx[2],pointcoordsy[1],fill='white',width='2',tags='symbol')
            elif r==4:
                c.create_line(pointcoordsx[1],pointcoordsy[1],pointcoordsx[2],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==5:
                c.create_line(pointcoordsx[1],pointcoordsy[1],pointcoordsx[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==6:
                c.create_line(pointcoordsx[2],pointcoordsy[1],pointcoordsx[1],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==7:
                c.create_line(pointcoordsx[2],pointcoordsy[1],pointcoordsx[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==8:
                c.create_line(pointcoordsx[2],pointcoordsy[1],pointcoordsx[2],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==9:
                c.create_line(pointcoordsx[2],pointcoordsy[1],pointcoordsx[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==10:
                c.create_line(pointcoordsx[1],pointcoordsy[2],pointcoordsx[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==11:
                c.create_line(pointcoordsx[1],pointcoordsy[2],pointcoordsx[2],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==12:
                c.create_line(pointcoordsx[1],pointcoordsy[2],pointcoordsx[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==13:
                c.create_line(pointcoordsx[2],pointcoordsy[2],pointcoordsx[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==14:
                c.create_line(pointcoordsx[2],pointcoordsy[2],pointcoordsx[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==15:
                c.create_line(pointcoordsx[1],pointcoordsy[3],pointcoordsx[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            while t==True:
                r=random.randint(1,15)
                if r!=rc:
                    t=False
        for i in range(4):
            t=True
            if r==1:
                c.create_line(pointcoordsx2[1],pointcoordsy[1],pointcoordsx2[1],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==2:
                c.create_line(pointcoordsx2[1],pointcoordsy[1],pointcoordsx2[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==3:
                c.create_line(pointcoordsx2[1],pointcoordsy[1],pointcoordsx2[2],pointcoordsy[1],fill='white',width='2',tags='symbol')
            elif r==4:
                c.create_line(pointcoordsx2[1],pointcoordsy[1],pointcoordsx2[2],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==5:
                c.create_line(pointcoordsx2[1],pointcoordsy[1],pointcoordsx2[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==6:
                c.create_line(pointcoordsx2[2],pointcoordsy[1],pointcoordsx2[1],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==7:
                c.create_line(pointcoordsx2[2],pointcoordsy[1],pointcoordsx2[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==8:
                c.create_line(pointcoordsx2[2],pointcoordsy[1],pointcoordsx2[2],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==9:
                c.create_line(pointcoordsx2[2],pointcoordsy[1],pointcoordsx2[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==10:
                c.create_line(pointcoordsx2[1],pointcoordsy[2],pointcoordsx2[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==11:
                c.create_line(pointcoordsx2[1],pointcoordsy[2],pointcoordsx2[2],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==12:
                c.create_line(pointcoordsx2[1],pointcoordsy[2],pointcoordsx2[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==13:
                c.create_line(pointcoordsx2[2],pointcoordsy[2],pointcoordsx2[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==14:
                c.create_line(pointcoordsx2[2],pointcoordsy[2],pointcoordsx2[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==15:
                c.create_line(pointcoordsx2[1],pointcoordsy[3],pointcoordsx2[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            while t==True:
                r=random.randint(1,15)
                if r!=rc:
                    t=False
        for i in range(4):
            t=True
            if r==1:
                c.create_line(pointcoordsx3[1],pointcoordsy[1],pointcoordsx3[1],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==2:
                c.create_line(pointcoordsx3[1],pointcoordsy[1],pointcoordsx3[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==3:
                c.create_line(pointcoordsx3[1],pointcoordsy[1],pointcoordsx3[2],pointcoordsy[1],fill='white',width='2',tags='symbol')
            elif r==4:
                c.create_line(pointcoordsx3[1],pointcoordsy[1],pointcoordsx3[2],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==5:
                c.create_line(pointcoordsx3[1],pointcoordsy[1],pointcoordsx3[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==6:
                c.create_line(pointcoordsx3[2],pointcoordsy[1],pointcoordsx3[1],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==7:
                c.create_line(pointcoordsx3[2],pointcoordsy[1],pointcoordsx3[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==8:
                c.create_line(pointcoordsx3[2],pointcoordsy[1],pointcoordsx3[2],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==9:
                c.create_line(pointcoordsx3[2],pointcoordsy[1],pointcoordsx3[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==10:
                c.create_line(pointcoordsx3[1],pointcoordsy[2],pointcoordsx3[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==11:
                c.create_line(pointcoordsx3[1],pointcoordsy[2],pointcoordsx3[2],pointcoordsy[2],fill='white',width='2',tags='symbol')
            elif r==12:
                c.create_line(pointcoordsx3[1],pointcoordsy[2],pointcoordsx3[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==13:
                c.create_line(pointcoordsx3[2],pointcoordsy[2],pointcoordsx3[1],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==14:
                c.create_line(pointcoordsx3[2],pointcoordsy[2],pointcoordsx3[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            elif r==15:
                c.create_line(pointcoordsx3[1],pointcoordsy[3],pointcoordsx3[2],pointcoordsy[3],fill='white',width='2',tags='symbol')
            while t==True:
                r=random.randint(1,15)
                if r!=rc:
                    t=False
        

c.bind("<Button-1>", main)
c.pack()
root.mainloop()