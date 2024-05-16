from tkinter import *
import os,random,math
os.chdir(os.path.dirname(os.path.abspath(__file__)))
root=Tk()
c=Canvas(root,height=300,width=300,bg='black')
c.pack()
lc=[0]*2
taniere=[[50+x*100,50+y*100] for x in range(3) for y in range(3)]
def setup():
    global lc,taniere
    lc=[random.randint(0,290) for _ in range(2)]
    while all([all([(lc[0]+10*i-t[0])**2+(lc[1]+10*i-t[1])**2>50**2 for t in taniere]) for i in range(2)]) and [all([(lc[0]+10-10*i-t[0])**2(lc[1]-10*i-t[1])**2>50**2 for t in taniere]) for i in range(2)]:
    while (all([all([(lc[0]+(10*i)-t[0])**2+(lc[1]+(10*i)-t[1])**2>50**2 for t in taniere]) for i in range(2)]) and all([all([(lc[0]-(10*i)+10-t[0])**2+(lc[1]-(10*i)-t[1])**2>50**2 for t in taniere]) for i in range(2)])):
        print('running')
        lc=[random.randint(0,290) for _ in range(2)]
    c.create_rectangle(lc,[l+10 for l in lc],fill='green')
for _ in range(20000):
    setup()
for t in taniere:
    pass
    #c.create_oval([ta-50 for ta in t],[tb+50 for tb in t],fill='blue')
root.mainloop()