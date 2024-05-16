import tkinter,random,math
import numpy as np
root=tkinter.Tk()
root.title("gravity sim")
H,W=600,600
canvas=tkinter.Canvas(root,bg="black",height=H,width=W)
canvas.create_oval(W/2+20,H/2+20,W/2-20,H/2-20,fill='white')
terminate=False
def generate(event):
    global terminate
    obj=[event.x,event.y]
    mass=random.randint(5,10)
    while True:
        canvas.update()
        canvas.delete('obj')
        if terminate==True or (not 600>=obj[0]>=0) or (not 600>=obj[1]>=0):
            break
        obj=move_diagonally(obj,15)
        obj=gravitational_force(obj,mass)
        canvas.create_oval(obj[0]+mass,obj[1]+mass,obj[0]-mass,obj[1]-mass,fill='white',tags='obj')
        canvas.after(100)

def gravitational_force(point1,distance,point2=[W/2,H/2]):
    global terminate
    x1,y1=point1
    x2,y2=point2
    current_distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    if current_distance<=20:
        terminate=True
        return point1
    ratio=distance/current_distance
    new_x=x1+(x2-x1)*ratio
    new_y=y1+(y2-y1)*ratio
    return (new_x, new_y)

def move_diagonally(point1, distance,point2=[W/2,H/2]):
    p1 = np.array(point1)
    p2 = np.array(point2)
    vector = p2 - p1
    rotated_vector = np.array([vector[1], -vector[0]])
    normalized_vector = rotated_vector / np.linalg.norm(rotated_vector)
    moved_point = p1 + distance * normalized_vector
    moved_point = np.round(moved_point).astype(int)
    return tuple(moved_point)

print(move_diagonally([0,0],[0,1],3))
canvas.bind("<Button-1>", generate)
canvas.pack()
root.mainloop() 