import numpy
from tkinter import *
root=Tk()
c=Canvas(root,height=800,width=800,bg='black')
c.pack(pady=20)
code=['{:08}'.format(int(numpy.base_repr(number,2))) for number in [123,65,4,98,54,186,201,166]]
colors=['white','black']
for y,number in enumerate(code):
    for x,digit in enumerate(number):
        c.create_rectangle(x*100,y*100,x*100+100,y*100+100,fill=colors[int(digit)])
root.mainloop()