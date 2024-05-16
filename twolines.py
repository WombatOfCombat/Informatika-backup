import tkinter,random,math
from tkinter import *
root = Tk()
H=600
W=600
xb=list()
yb=list()
vectoru=list()
c = Canvas(root,bg = "black",height=H, width=W)
def twolines():
    while True:
        c.after(100)
        c.update()
        global xb,yb,vectoru
        xb=list()
        yb=list()
        vectoru=list()
        c.delete('lines')
        for i in range(4):
            wall=random.choice(['u','d','l','r'])
            if wall=='u':
                xb.append(random.randint(0,600))
                yb.append(0)
            elif wall=='d':
                xb.append(random.randint(0,600))
                yb.append(600)
            elif wall=='l':
                xb.append(0)
                yb.append(random.randint(0,600))
            elif wall=='r':
                xb.append(600)
                yb.append(random.randint(0,600))
        for j in range(0,4,2):
            c.create_line(xb[j],yb[j],xb[j+1],yb[j+1],fill='white',tags='lines')
            vectoru.append([xb[j]-xb[j+1],yb[j]-yb[j+1]])
        solveequation()
def solveequation():
    from sympy import symbols, Eq, solve
    t, s = symbols('t s')
    eq1 = Eq(xb[0]+t*vectoru[0][0],xb[2]+s*vectoru[1][0])
    eq2 = Eq(yb[0]+t*vectoru[0][1],yb[2]+s*vectoru[1][1])
    solve((eq1,eq2), (t, s))
    sol_dict = solve((eq1,eq2), (t, s))
    print(sol_dict)
    x=xb[0]+sol_dict[t]*vectoru[0][0]
    y=yb[0]+sol_dict[t]*vectoru[0][1]
    #c.create_oval(int(x)-5,int(y)-5,int(x)+5,int(y)+5,fill='',outline='white')
button_frame = tkinter.Frame(root)
button_frame.pack(side='bottom')
b1 = tkinter.Button(button_frame, text='1', command=twolines)
b1.pack(side='left')
c.pack()
root.mainloop()