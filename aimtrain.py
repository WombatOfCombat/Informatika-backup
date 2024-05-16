from tkinter import *
import os,random
os.chdir(os.path.dirname(os.path.abspath(__file__)))
root=Tk()
c=Canvas(root,height=300,width=300,bg='black')
c.pack()
pos=[0,0]
hit,miss,crit_hit=0,0,0
shot=False
first=True
def stvorec(side_lenght):
    global pos,miss,shot,first
    if not shot and not first:
        miss+=1
    shot=False
    first=False
    pos=[random.randint(0,260),random.randint(0,260)]
    c.delete('stvorec')
    c.create_rectangle(pos,[pos[i]+side_lenght for i in range(2)],fill='green',tags='stvorec')
    c.create_rectangle([p+10 for p in pos],[pos[i]+side_lenght-10 for i in range(2)],fill='red',tags='stvorec')
    c.update()
    c.after(1000,lambda:stvorec(40))
c.after(1000,lambda:stvorec(40))
def check(event):
    global pos,hit,miss,crit_hit,shot
    if pos[0]<event.x<pos[0]+40 and pos[1]<event.y<pos[1]+40:
        hit+=1
        if pos[0]+10<event.x<pos[0]+30 and pos[1]+10<event.y<pos[1]+30:
            crit_hit+=1
        shot=True
    else:
        miss+=1
    c.delete('score')
    c.create_text(150,10,fill='white',text=f'accuracy: {round(100/(hit+miss)*hit,2)}%',tags='score')
    c.create_text(150,30,fill='white',text=f'critical accuracy: {round(100/(hit+miss)*crit_hit,2)}%',tags='score')
root.bind("<Button-1>",check)
root.mainloop()