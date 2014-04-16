from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.graphics import *
from kivy.vector import Vector
from kivy.metrics import dp

class Peca(Widget):
    def __init__(self, x, y, table, locx, locy,  **kwargs):
        super(Peca, self).__init__(**kwargs)
        self.table = table
        self.locx = locx
        self.locy = locy
        self.pos = x, y
        self.size = 70, 70
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()    
        
    def update_canvas(self, *args):
        raise Exception("Peca nao pode ser instanciada")
    
     
                    
    def move_right(self):
        print self.locx, self.locy
        self.table.table[self.locx][self.locy], self.table.table[self.locx + 1][self.locy] = self.table.table[self.locx+1][self.locy], self.table.table[self.locx][self.locy]
        self.table.update_canvas()

    def move_left(self):
        print self.locx, self.locy
        self.table.table[self.locx][self.locy], self.table.table[self.locx - 1][self.locy] = self.table.table[self.locx-1][self.locy], self.table.table[self.locx][self.locy]
        self.table.update_canvas()
    def move_up(self):
        print self.locx, self.locy
        self.table.table[self.locx][self.locy], self.table.table[self.locx ][self.locy+1] = self.table.table[self.locx][self.locy+1], self.table.table[self.locx][self.locy]
        self.table.update_canvas()

    def move_down(self):
        print self.locx, self.locy
        self.table.table[self.locx][self.locy], self.table.table[self.locx ][self.locy -1] = self.table.table[self.locx][self.locy -1], self.table.table[self.locx][self.locy]
        self.table.update_canvas()    
    
class Tri(Peca):
    def __init__(self, x, y,  table, locx, locy,**kwargs):
        super(Tri, self).__init__(x, y, table, locx, locy,**kwargs)    
    
    def update_canvas(self, *args):
        self.canvas.clear()
        Triangle(points=[self.pos[0], self.pos[1], self.pos[0]+ self.size[0]/2, self.pos[1]+self.size[0]/2, self.pos[0] + self.size[0], self.pos[1]])
        
    def __str__(self):
        return "Tri"
    def __repr__(self):
                return "Tri"    

class Bola(Peca):
    def __init__(self, x, y,  table, locx, locy,**kwargs):
        super(Bola, self).__init__(x, y, table, locx, locy,**kwargs)    
    
    def update_canvas(self, *args):
        self.canvas.clear()
        Ellipse(pos = self.pos, size = [2*self.size[0]/3, 2*self.size[1]/3])
    def __str__(self):
        return "Bola"   
    def __repr__(self):
            return "Bola"    
        
                     
        
class Tabuleiro(Widget):
    def __init__(self, **kwargs):
        super(Tabuleiro, self).__init__(**kwargs)
        self.table = [[[None] for i in range(8)] for j in range(8)]
        with self.canvas:
                            for i in range(len(self.table)):
                                for j in range(len(self.table[0])):
                                    if i%2==0:
                                        self.table[i][j] = Tri(50+ i*70,50+ j*70, self, i, j)  
                                    else:
                                        self.table[i][j] = Bola(50+ i*70,50+ j*70, self, i, j)  
                                    self.add_widget(self.table[i][j])         
        #self.update_canvas()
        
    def update_canvas(self):
        print self.table
        self.canvas.clear()
        self.clear_widgets()
        with self.canvas:
                    for i in range(len(self.table)):
                        for j in range(len(self.table[0])):
                            self.table[i][j].pos = 50+ i*70,50+ j*70
                            self.table[i][j].update_canvas()
                            self.add_widget(self.table[i][j])        
    

class JogoApp(App):
    def build(self):
        return Tabuleiro()

if __name__ == '__main__':
    JogoApp().run()
