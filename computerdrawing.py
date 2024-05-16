import random
from tkinter import *
root=Tk()
W=600
H=600
c = Canvas(root,width=W, height=H, bg='black')
c.pack(pady=20)
def draw(coords):
    global pen_down,cp
    cc=[coords.x,coords.y]
    if pen_down:
        c.create_line(cc,cp,fill='white',tags='line')
    pen_down=True
    cp=cc
    with open('suradnice.txt','a') as file:
        file.write(str(cp[0])+','+str(cp[1])+',')
def redraw_from_memory(coords):
    config_coords=[coords.x,coords.y]
    with open('suradnice.txt','r') as file:
        redraw_data=file.readline().split(',')
    redraw_data.remove('')
    redraw_data=[int(coordinate) for coordinate in redraw_data]
    c.create_line(redraw_data,fill=random.choice(['red','green','blue','purple','orange']),tags='line')
    c.create_line(redraw_data[::-1],fill=random.choice(['red','green','blue','purple','orange']),tags='line')
def delete_specific(key_pressed):
    global pen_down
    if key_pressed.char=='a':
        c.delete('line')
        pen_down=False
    elif key_pressed.char=='d':
        with open('suradnice.txt','w') as _:
            pass
cp=[0]*2
pen_down=False
#root.bind("<Motion>",controls)
root.bind("<B1-Motion>",draw)
root.bind("<Button-2>",redraw_from_memory)
root.bind('<Key>',delete_specific)
root.mainloop()