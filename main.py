from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.graphics import *

class Peca(Widget):
    def __init__(self, x, y, **kwargs):
        super(Peca, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()    
        
    def update_canvas(self, *args):
        self.canvas.clear()
        Ellipse(pos = self.pos, size = self.size)

class Tabuleiro(Widget):
    def __init__(self, **kwargs):
        super(Tabuleiro, self).__init__(**kwargs)
        self.table = [[1, 1],[1, 1]]
        with self.canvas:
            for i in range(len(self.table)):
                for j in range(len(self.table[0])):
                    self.table[i][j] = Peca(i*100, j*100)  
    

class PongApp(App):
    def build(self):
        return Tabuleiro()

if __name__ == '__main__':
    PongApp().run()
