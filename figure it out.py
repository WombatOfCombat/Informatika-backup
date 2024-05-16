import math,tkinter,random
from tkinter import font
import numpy as geek
root=tkinter.Tk()
root.title("figure it out")

H,W=1000,1800
canvas=tkinter.Canvas(root, bg="black", height=H, width=W)
cubes=[[[375,375,675],[525,375,675],[525,525,675],[375,525,675],[375,375,525],[525,375,525],[525,525,525],[375,525,525]]]
camera=[400,500,1100]
cube_side_centers=[[[[375,450,600],[525,450,600]],[[450,375,600],[450,525,600]],[[450,450,675],[450,450,475]]]]
detail=512
axes_of_rotation=[1,1,1]
rotation_speeds_all=[[math.pi/detail*r*i for r in axes_of_rotation] for i in [0.05 if j == 0 else -0.1 if j==1 else 0.1 for j in range(3)]]
render=[]
x=0
no=True
colrot1=0
colrot2=0
center=[450,450,600]
def resize_cube(vertices,size_modifier):
    global center
    half_side_length=min([abs(coord-center[i])for i,coord in enumerate(vertices[0])])/size_modifier
    new_vertices=[[center[i]+(coord-center[i])/size_modifier for i,coord in enumerate(vertex)] for vertex in vertices]
    return new_vertices


cubes.append(resize_cube(cubes[-1],8/6))
cubes.append([100*crd+center[i] +(-0.5 if i==0 else math.sqrt(6)/12 if i==1 else math.sqrt(3)/6 if i==2 else '')*100 for i,crd in enumerate(point)] for point in [[0,0,0],[1,0,0],[0.5,0,-math.sqrt(3)/2],[0.5,-math.sqrt(6)/3,-math.sqrt(3)/6]])
cubes=[[[dim-40 if i==0 else dim+50 if i==1 else dim for i,dim in enumerate(point)] for point in cube] for cube in cubes]
cube_side_centers=[[[[dim-40 if i==0 else dim+50 if i==1 else dim for i,dim in enumerate(point)] for point in dim_centers] for dim_centers in n_cubes_side_centers] for n_cubes_side_centers in cube_side_centers]

def draw(projection):
    global x,cubes,no,colrot1,colrot2,color
    colrot1+=1
    red = int((1 + math.sin(colrot1/255)) * 127)
    green = int((1 + math.sin(colrot1/255 + 2)) * 127)
    blue = int((1 + math.sin(colrot1/255 + 4)) * 127)
    color = ["#{:02x}{:02x}{:02x}".format(red, green, blue),"#{:02x}{:02x}{:02x}".format(red,blue,green),"#{:02x}{:02x}{:02x}".format(green,red,blue),"#{:02x}{:02x}{:02x}".format(green,blue,red),"#{:02x}{:02x}{:02x}".format(blue,green,red),"#{:02x}{:02x}{:02x}".format(blue,red,green)]
    for i in range((len(projection)-4)//8):
        canvas.create_text(1000+160*(i%4),570+i//4*140,text=[["{:.2f}".format(j ) for j in k] for k in projection[i*8:(i+1)*8]],fill='grey',tags='cube',width=100,font=font.Font(size=10))
    for i,cube in enumerate(cubes):
        canvas.create_text(1000+160*(i%4),290+i//4*140,text=[["{:.2f}".format(j ) for j in k] for k in cube],fill='grey',tags='cube',width=150,font=font.Font(size=10))
    for j,proj in enumerate([projection[i*8:(i+1)*8] for i in range((len(projection)-4)//8)]):
        for i,point2D in reversed(list(enumerate(proj))):
            if i<=3:
                canvas.create_line(point2D,proj[(i+1)%4],fill=color[j%len(color)],tags='cube')
                canvas.create_line(point2D,proj[i+4],fill=color[j%len(color)],tags='cube')
            else:
                canvas.create_line(point2D,proj[((i-3)%4)+4],fill=color[j%len(color)],tags='cube')
    for j,proj in enumerate(projection[-3:]):
        canvas.create_line(projection[-4],proj,fill=color[2],tags='cube')
        if j!=0:
            canvas.create_line(projection[-3],proj,fill=color[2],tags='cube')
        if j==2:
            canvas.create_line(projection[-2],proj,fill=color[2],tags='cube')


def rotate_point(point3D,CSC,rotation_speeds,i,j):
    if j==0:
        CSC_index=0 if i in [0,3,4,8] else 1
        point3D=[point3D[0],
                 (point3D[1]-CSC[CSC_index][1])*math.cos(rotation_speeds[j])-(point3D[2]-CSC[CSC_index][2])*math.sin(rotation_speeds[j])+CSC[CSC_index][1],
                 (point3D[1]-CSC[CSC_index][1])*math.sin(rotation_speeds[j])+(point3D[2]-CSC[CSC_index][2])*math.cos(rotation_speeds[j])+CSC[CSC_index][2]]
    elif j==1:
        CSC_index=0 if i<=3 else 1
        point3D=[(point3D[0]-CSC[CSC_index][0])*math.cos(rotation_speeds[j])-(point3D[2]-CSC[CSC_index][2])*math.sin(rotation_speeds[j])+CSC[CSC_index][0],
                 point3D[1],
                 (point3D[0]-CSC[CSC_index][0])*math.sin(rotation_speeds[j])+(point3D[2]-CSC[CSC_index][2])*math.cos(rotation_speeds[j])+CSC[CSC_index][2]]
    else:
        CSC_index=0 if i in [0,1,4,5] else 1
        point3D=[(point3D[0]-CSC[CSC_index][0])*math.cos(rotation_speeds[j])-(point3D[1]-CSC[CSC_index][1])*math.sin(rotation_speeds[j])+CSC[CSC_index][0],
                 (point3D[0]-CSC[CSC_index][0])*math.sin(rotation_speeds[j])+(point3D[1]-CSC[CSC_index][1])*math.cos(rotation_speeds[j])+CSC[CSC_index][1],
                 point3D[2]]
    return point3D

def main():
    global cubes,cube,x
    canvas.delete('cube')
    projection=[]
    for k,cube in enumerate(cubes):
        for i,point3D in enumerate(cube):
            for j,CSC in enumerate(cube_side_centers[-1]):
                rotation_speeds=rotation_speeds_all[k]
                point3D=rotate_point(point3D,CSC,rotation_speeds,i,j)
            cube[i]=point3D
            vector=[point3D[i]-camera[i] for i in range(len(point3D))]
            projection.append([point3D[i]+vector[i]*(-point3D[2]/vector[2]) for i in range(2)])
    render.append(projection)
    draw(projection)
    x+=1
    canvas.update()
    canvas.after(0,main)
canvas.pack()
canvas.after(100,main)
root.mainloop()