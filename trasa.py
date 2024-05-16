import tkinter
root=tkinter.Tk()
root.title("trasa vyletu")
H,W=600,600
canvas=tkinter.Canvas(root,bg="black",height=H,width=W)
nv=[15, 15, 16, 17, 19, 17, 16, 15, 14, 14, 13, 12, 12, 13, 12]
#nv=[]
#for i in range(15):
   #nv+=[int(input('nadmorska vyska:'))]
x=0
for i in range(len(nv)-1):
   if abs(nv[i]-nv[i+1])>1:
      canvas.create_line(W/30+W/15*i,600-nv[i]*15,W/30+W/15*(i+1),600-nv[i+1]*15,fill='red')
   else:
      x+=1
      canvas.create_line(W/30+W/15*i,600-nv[i]*15,W/30+W/15*(i+1),600-nv[i+1]*15,fill='green')
if x==14:
   print('trasa je prispôsobilá pre starú mamu')
else:
   print('trasa je nespôsobilá pre starú mamu')
canvas.pack()
root.mainloop() 
