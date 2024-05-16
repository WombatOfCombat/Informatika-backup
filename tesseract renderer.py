import math,tkinter,random
from tkinter import font
import numpy as geek
root=tkinter.Tk()
root.title("3D_tesseract_render")

H,W=1000,1800
canvas=tkinter.Canvas(root, bg="black", height=H, width=W)
#canvas.create_line(0,500,2100,500,fill='white')
cubes=[[[375,375,675],[525,375,675],[525,525,675],[375,525,675],[375,375,525],[525,375,525],[525,525,525],[375,525,525]]]
camera=[400,500,1100]
cube_side_centers=[[[[375,450,600],[525,450,600]],[[450,375,600],[450,525,600]],[[450,450,675],[450,450,475]]]]
detail=512
axes_of_rotation=[1,0,1]
rotation_speeds_all=[[math.pi/detail*axes_of_rotation[j]*i for j in range(3)] for i in [1 if i % 2 == 0 else -1 for i in range(10)]]
render=[]
x=0
no=True
colrot1=0
colrot2=0
def half_size_cube(vertices):
    center=[450,450,600]
    half_side_length=min([abs(coord-center[i])for i,coord in enumerate(vertices[0])])/3*2
    new_vertices=[[center[i]+(coord-center[i])/3*2 for i,coord in enumerate(vertex)] for vertex in vertices]
    return new_vertices

for i in range(7):
    cubes.append(half_size_cube(cubes[-1]))
    cube_side_centers.append(half_size_cube([subsublist for sublist in cube_side_centers[-1] for subsublist in sublist]))
    cube_side_centers[-1]=[[cube_side_centers[-1][2*i+j]for j in range(2)]for i in range(3)]
cubes=[[[dim-40 if i==0 else dim+50 if i==1 else dim for i,dim in enumerate(point)] for point in cube] for cube in cubes]
cube_side_centers=[[[[dim-40 if i==0 else dim+50 if i==1 else dim for i,dim in enumerate(point)] for point in dim_centers] for dim_centers in n_cubes_side_centers] for n_cubes_side_centers in cube_side_centers]

def draw(projection):
    global x,cubes,no,colrot1,colrot2,color
    colrot1+=1
    red = int((1 + math.sin(colrot1/255)) * 127)
    green = int((1 + math.sin(colrot1/255 + 2)) * 127)
    blue = int((1 + math.sin(colrot1/255 + 4)) * 127)
    color = ["#{:02x}{:02x}{:02x}".format(red, green, blue),"#{:02x}{:02x}{:02x}".format(red,blue,green),"#{:02x}{:02x}{:02x}".format(green,red,blue),"#{:02x}{:02x}{:02x}".format(green,blue,red),"#{:02x}{:02x}{:02x}".format(blue,green,red),"#{:02x}{:02x}{:02x}".format(blue,red,green)]
    for i in range(len(projection)//8-1):
        for j in range(8):
            canvas.create_line(projection[i*8:(i+1)*8][j],projection[(i+1)*8:(i+2)*8][j],fill='grey',tags='cube')
    for i in range(len(projection)//8):
        canvas.create_text(1000+160*(i%4),570+i//4*140,text=[["{:.2f}".format(j ) for j in k] for k in projection[i*8:(i+1)*8]],fill='grey',tags='cube',width=100,font=font.Font(size=10))
    for i,cube in enumerate(cubes):
        canvas.create_text(1000+160*(i%4),290+i//4*140,text=[["{:.2f}".format(j ) for j in k] for k in cube],fill='grey',tags='cube',width=150,font=font.Font(size=10))
    for j,proj in enumerate([projection[i*8:(i+1)*8] for i in range(len(projection)//8)]):
        for i,point2D in reversed(list(enumerate(proj))):
            if i<=3:
                canvas.create_line(point2D,proj[(i+1)%4],fill=color[j%len(color)],tags='cube',width=1)
                canvas.create_line(point2D,proj[i+4],fill=color[j%len(color)],tags='cube',width=1)
            else:
                canvas.create_line(point2D,proj[((i-3)%4)+4],fill=color[j%len(color)],tags='cube',width=1)

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
            for j,CSC in enumerate(cube_side_centers[k]):
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
