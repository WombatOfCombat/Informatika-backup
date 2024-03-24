import tkinter,random,math
from tkinter import *
root = Tk()
H=1000
W=1500
c = Canvas(root,bg = "black",height=H, width=W)
c.pack(pady=20)
def draw():
    global luminousity,score
    c.delete('score_board')
    c.create_text(W/2,20,text=f'score:{score}',fill='white',tags='score_board')
    c.create_text(80,20,text='anomaly luminousity scale:',fill='white',tags='score_board')
    c.create_text(160,20,text=luminousity//50,fill="#{:02x}{:02x}{:02x}".format(luminousity-50,255-(luminousity-50),0),tags='score_board')
def motion(event):
    global target_point,score,xm,ym,luminousity
    c.delete('lines')
    xm,ym=event.x,event.y
    visibility=luminousity-distance([xm,ym],target_point)/2
    for x in range(0,W+1,20):
        for y in range(0,H+1,20):
            if distance([x,y],[xm,ym])<=visibility:
                vector=[x-xm,y-ym]
                col_index=int(255-(255/visibility)*distance([x,y],[xm,ym]))
                if score<=3:
                    color="#"+"{:02x}".format(int(col_index*(score/3)))*3
                else:
                    color="#"+"{:02x}".format(col_index)*3
                c.create_line(x,y,x+vector[0]/7,y+vector[1]/7,fill=color,tags='lines',width=1+score//5)
def check(event):
    global xm,ym,target_point,score,luminousity
    if distance([xm,ym],target_point)<=5:
        score=round(score+1+(luminousity//50-1)/10,1)
        luminousity=random.randint(50,200)
        target_point=[20*random.randint(0,W/20),20*random.randint(0,H/20-1)]
    else:
        score=round(score-0.1*(6-luminousity//50),1)
    if score<=0:
        startup()
    draw()
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def startup():
    global target_point,score,luminousity,xm,ym
    target_point=[20*random.randint(0,W/20),20*random.randint(0,H/20-1)]
    score=1
    xm,ym=0,0
    luminousity=random.randint(50,255)
    draw()
startup()
root.bind('<Motion>', motion)
root.bind("<Button-1>",check)
root.mainloop()