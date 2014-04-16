from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty

class Peca(Widget):
    pass

class Tabuleiro(Widget):
    def __init__(self, **kwargs):
        super(Tabuleiro, self).__init__(**kwargs)
        self.layout = GridLayout(cols=2)
        self.layout.add_widget(Peca())
        self.table = ListProperty([[Peca(), Peca()],[Peca(), Peca()]])
    

class PongApp(App):
    def build(self):
        return Tabuleiro()

if __name__ == '__main__':
    PongApp().run()
