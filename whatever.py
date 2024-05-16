import tkinter,random,math
from tkinter import *
root = Tk()
c = Canvas(root,bg = "black",height=700, width=400)
pointcoordsx=[50,350]
pointcoordsy=[50,350,650]
rc=list()
def main(event):
    while True:
        global r1,r2,r3,r4,rc
        c.after(200)
        c.update()
        c.delete('a')
        r1=r2=r3=r4=0
        k=True
        for i in range(4):
            while k==True:
                r1=random.randint(0,1)
                r2=random.randint(0,1)
                r3=random.randint(0,2)
                r4=random.randint(0,2)
                print(rc,r1,r3,r2,r4)
                if ([r1,r3,r2,r4] not in rc) and ([r1,r3]!=[r2,r4]) and ([r2,r4,r1,r3] not in rc):
                    rc.append([r1,r3,r2,r4])
                    k=False
            c.create_line(pointcoordsx[r1],pointcoordsy[r3],pointcoordsx[r2],pointcoordsy[r4],fill='red',tags='a')
            k=True
        rc=list()
c.bind("<Button-1>", main)
c.pack()
root.mainloop()
