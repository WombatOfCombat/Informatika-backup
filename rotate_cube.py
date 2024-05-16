import math,tkinter,random
from sympy import symbols, solve

root=tkinter.Tk()
root.title("cube")

H,W=900,900
canvas=tkinter.Canvas(root, bg="black", height=H, width=W)
cubes=[[[375,375,675],[525,375,675],[525,525,675],[375,525,675],[375,375,525],[525,375,525],[525,525,525],[375,525,525]],[[412.5, 412.5, 562.5], [487.5, 412.5, 562.5], [487.5, 487.5, 562.5], [412.5, 487.5, 562.5], [412.5, 412.5, 487.5], [487.5, 412.5, 487.5], [487.5, 487.5, 487.5], [412.5, 487.5, 487.5]]]
camera=[450,450,900]
cube_side_centers=[[[[375,450,600],[525,450,600]],[[450,375,600],[450,525,600]],[[450,450,675],[450,450,675]]],[[[412.5, 450.0, 525.0], [487.5, 450.0, 525.0]], [[450.0, 412.5, 525.0], [450.0, 487.5, 525.0]], [[450.0, 450.0, 562.5], [450.0, 450.0, 562.5]]]]
rotation_speeds_all=[[0,0,math.pi/64],[-math.pi/64,0,0]]
x=0
def main():
    global cubes,cube,x
    canvas.delete('cube')
    projection=[]
    for k,cube in enumerate(cubes):
        for i,point3D in enumerate(cube):
            for j,CSC in enumerate(cube_side_centers[k]):
                if x//128%2==0:
                    rotation_speeds=rotation_speeds_all[k]
                else:
                    rotation_speeds=rotation_speeds_all[k-1]
                if x%128==0:
                    cubes=[[[375,375,675],[525,375,675],[525,525,675],[375,525,675],[375,375,525],[525,375,525],[525,525,525],[375,525,525]],[[412.5, 412.5, 562.5], [487.5, 412.5, 562.5], [487.5, 487.5, 562.5], [412.5, 487.5, 562.5], [412.5, 412.5, 487.5], [487.5, 412.5, 487.5], [487.5, 487.5, 487.5], [412.5, 487.5, 487.5]]]
                if j==1:
                    if i<=3:
                        point3D=[(point3D[0]-CSC[0][0])*math.cos(rotation_speeds[j])-(point3D[2]-CSC[0][2])*math.sin(rotation_speeds[j])+CSC[0][0],point3D[1],(point3D[0]-CSC[0][0])*math.sin(rotation_speeds[j])+(point3D[2]-CSC[0][2])*math.cos(rotation_speeds[j])+CSC[0][2]]
                    else:
                        point3D=[(point3D[0]-CSC[1][0])*math.cos(rotation_speeds[j])-(point3D[2]-CSC[1][2])*math.sin(rotation_speeds[j])+CSC[1][0],point3D[1],(point3D[0]-CSC[1][0])*math.sin(rotation_speeds[j])+(point3D[2]-CSC[1][2])*math.cos(rotation_speeds[j])+CSC[1][2]]
                elif j==0:
                    if i in [0,3,4,8]:
                        point3D=[point3D[0],(point3D[1]-CSC[0][1])*math.cos(rotation_speeds[j])-(point3D[2]-CSC[0][2])*math.sin(rotation_speeds[j])+CSC[0][1],(point3D[1]-CSC[0][1])*math.sin(rotation_speeds[j])+(point3D[2]-CSC[0][2])*math.cos(rotation_speeds[j])+CSC[0][2]]
                    else:
                        point3D=[point3D[0],(point3D[1]-CSC[1][1])*math.cos(rotation_speeds[j])-(point3D[2]-CSC[1][2])*math.sin(rotation_speeds[j])+CSC[1][1],(point3D[1]-CSC[1][1])*math.sin(rotation_speeds[j])+(point3D[2]-CSC[1][2])*math.cos(rotation_speeds[j])+CSC[1][2]]
                else:
                    if i in [0,1,4,5]:
                        point3D=[(point3D[0]-CSC[0][0])*math.cos(rotation_speeds[j])-(point3D[1]-CSC[0][1])*math.sin(rotation_speeds[j])+CSC[0][0],(point3D[0]-CSC[0][0])*math.sin(rotation_speeds[j])+(point3D[1]-CSC[0][1])*math.cos(rotation_speeds[j])+CSC[0][1],point3D[2]]
                    else:
                        point3D=[(point3D[0]-CSC[1][0])*math.cos(rotation_speeds[j])-(point3D[1]-CSC[1][1])*math.sin(rotation_speeds[j])+CSC[1][0],(point3D[0]-CSC[1][0])*math.sin(rotation_speeds[j])+(point3D[1]-CSC[1][1])*math.cos(rotation_speeds[j])+CSC[1][1],point3D[2]]
            point3D=[round(point3D[i])for i in range(3)]
            cube[i]=point3D
            vector=[point3D[i]-camera[i] for i in range(len(point3D))]
            t=symbols('t')
            t=solve(point3D[2]+vector[2]*t)[0]
            projection.append([eval(str(point3D[i]+vector[i]*t)) for i in range(2)])
    for j,proj in enumerate([projection[:8],projection[8:16]]):
        for i,point2D in enumerate(proj):
            if i<=3:
                canvas.create_line(point2D,proj[(i+1)%4],fill='blue',tags='cube')
                canvas.create_line(point2D,proj[i+4],fill='green',tags='cube')
            else:
                canvas.create_line(point2D,proj[((i-3)%4)+4],fill='red',tags='cube')
    x+=1
    for i in range(8):
        canvas.create_line(projection[:8][i],projection[8:][i],fill='purple',tags='cube')
    #for i in range(4):
        #if i%2==0:
            #color='blue'
        #else:
            #color='red'
        #canvas.create_polygon(projection[i*4],projection[i*4+1],projection[i*4+2],projection[i*4+3],fill=color,tags='cube')
    canvas.update()
    canvas.after(20,main)
canvas.pack()
canvas.after(100,main)
root.mainloop()