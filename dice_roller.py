from tkinter import Tk, Canvas, Button

root = Tk()
W, H = 1000, 100
c = Canvas(root, width=W, height=H, bg='black')
c.pack(pady=20)

conditions = []

class Par_handler:
    def __init__(self):
        self.buttons = []

    def remove_parameter(self, parameter_index):
        global conditions
        conditions.pop(parameter_index)
        self.update_buttons()

    def add_parameter(self, probability, should_fall):
        global conditions
        conditions.append([probability, should_fall])
        self.update_buttons()

    def update_buttons(self):
        for button in self.buttons:
            button.destroy()
        self.buttons = []
        for i, parameter in enumerate(conditions):
            #c.create_rectangle(51*i,50,51*(i+1),100,fill='white')
            c.create_text(25.5*(i+1),50,text=parameter)
            button = Button(root, text='remove', command=lambda i=i: self.remove_parameter(i))
            button.pack(side='left')
            self.buttons.append(button)

Parameters=Par_handler()

for _ in range(19):
    Parameters.add_parameter(1, True)

root.mainloop()