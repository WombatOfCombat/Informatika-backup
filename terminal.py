from tkinter import *

root=Tk()
c=Canvas(root,width=1200,height=900,bg='#000000')
c.pack(pady=20)

c_history=[]
c_input='>'
t_messages=[]

def t_message(message):
    global t_messages
    t_messages.append(message)
    c.delete('terminal')
    for i,message in enumerate(t_messages[::-1]):
        c.create_text(1100,900-(i+1)*100,text=message,width=200,fill='green',tags='terminal',font='Courier 10')

def c_line(key):
    global c_input,c_history
    if key.char=='\r':
        c_history.append(c_input[1:])
        c.delete('command_history')
        c.delete('command')
        for i,past_input in enumerate(c_history[::-1]):
            c.create_text(20+len(past_input)*4,880-(i+1)*10,text=past_input,fill='green',tags='command_history',font='Courier 10')
        #t_message(c_input[1:])
        c_input='>'
    elif key.char=='\x08':
        c_input=c_input[:-1]
        c.delete('command')
        c.create_text(20+len(c_input)*4,880,text=c_input,fill='green',tags='command',font='Courier 10')
    else:
        print(key)
        c_input+=key.char
        c.delete('command')
        c.create_text(20+len(c_input)*4,880,text=c_input,fill='green',tags='command',font='Courier 10')

root.bind('<Key>',c_line)
root.mainloop()