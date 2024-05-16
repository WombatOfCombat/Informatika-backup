from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Line,Color,Ellipse
import math,random

coordinates = [0, 0]
completed=[]
ec=[random.choice(range(40, 600 - 40 + 1, 40)) for _ in range(2)]
labeled=False

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        Window.size = (600, 600)  # Set the window size explicitly
        rectangle = TouchInput()
        layout.add_widget(rectangle)
        return layout


class TouchInput(Widget):
    def __init__(self, **kwargs):
        super(TouchInput, self).__init__(**kwargs)
        self.bind(size=self.draw)
        self.bind(pos=self.draw)

    def draw(self, *args):
        global labeled
        self.canvas.clear()
        W = int(self.width)
        H = int(self.height)
        vector = [ec[0] - coordinates[0], ec[1] - coordinates[1]]
        de=distance(ec,coordinates)+1
        with self.canvas:
            for x in range(40, W - 40 + 1, 40):
                for y in range(40, H - 40 + 1, 40):
                    dc = distance([x, y], coordinates) + 1
                    dcg=dc/25
                    rgba=Color(
                            ((1 + math.sin(0.3 * dcg)) * 127)/255,
                            ((1 + math.sin(0.3 * dcg + 2)) * 127)/255,
                            ((1 + math.sin(0.3 * dcg + 4)) * 127)/255,
                        )
                    if [x,y] not in completed:
                        Line(
                            points=[
                                x - vector[0] / (de / 7),
                                y - vector[1] / (de / 7),
                                x + vector[0] / (de / 7),
                                y + vector[1] / (de / 7),
                            ],
                            color=rgba
                        )
                    else:
                        Ellipse(pos=(x-5,y-5),size=(10,10),color=rgba)
        if len(completed) >= 14 ** 2 and not labeled:
            label = Label(text='congratulations', color=(1, 1, 1))
            self.parent.add_widget(label)
            labeled=True


    def on_touch_down(self, touch):
        global coordinates,ec
        coordinates = [touch.x, touch.y]
        if len(completed)<14**2:
            ec=[random.choice(range(40, 600 - 40 + 1, 40)) for _ in range(2)]
            while ec in completed:
                ec=[random.choice(range(40, 600 - 40 + 1, 40)) for _ in range(2)]
        self.draw()  # Update drawing

    def on_touch_move(self, touch):
        global coordinates
        coordinates = [touch.x, touch.y]
        self.draw()  # Update drawing

    def on_touch_up(self, touch):
        global coordinates,completed
        coordinates = [touch.x, touch.y]
        if distance(coordinates,ec)<=30:
            completed.append(ec)
        else:
            completed=[]
        print(len(completed))
        self.draw()  # Update drawing


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


if __name__ == "__main__":
    MyApp().run()
