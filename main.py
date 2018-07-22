from kivy.app import App
#kivy.require("1.10.0")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

#Interface Layout
from kivy.lang import Builder
#presentation = Builder.load_file("main.kv")

# Window cofiguration
from kivy.config import Config
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")

from datetime import datetime as dtime


class WinClock(GridLayout):

    def __init__(self, **kwargs):
        GridLayout.__init__(self)
        self.cols=1  #important features-- represent no. of cols in screen
        #self.rows=2 #use with care
        self.wid =Label(font_size = 25 )
        self.add_widget(self.wid)
        Clock.schedule_interval(self.my_callback, 1)

    def my_callback(self,dt):
        res = dtime.now()
        info =[res.hour%12,res.minute,res.second]
        self.wid.text = ":".join(map(str, info))

class MyApp(App):
    
    def build(self):
        self.title = "Clock"
        return WinClock()


if __name__ == "__main__":
    MyApp().run()
