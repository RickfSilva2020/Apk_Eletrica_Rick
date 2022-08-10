from turtle import title
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty
from kivy.uix import popup


# CLASSE PARA GERENCIAR AS TELAS
class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    def confirmacao(self, *args):
        box = BoxLayout(orientation='vertical')
        pop = popup(title = 'Deseja mesmo sair?', content = box)
        
#class Widget1(BoxLayout): # EM CASO DE UMA TELA
class Widget1(Screen): # NO CASO DE MAIS DE UMA TELA
    def __init__(self, widget1=[], **kwargs):
        super().__init__(**kwargs)
        for palavra in widget1:
            self.ids.princBox.add_widget(Rempalavra(text=palavra))
            
    # Vincular eventos de teclado um pouco antes de entrar na tela
    def on_pre_enter(self):
        Window.bind(on_keyboard= self.voltar)
        
    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current= 'menu'           
            return True
    
    def on_pre_leave(self):
        Window.unbind(on_keyboard= self.voltar)        
    
    def addWidget(self):
        input_testo = self.ids.nova_palavra.text
        self.ids.princBox.add_widget(Rempalavra(text = input_testo ))
        self.ids.nova_palavra.text = ''
        
# Personalização dos botões
class BotaoPers(ButtonBehavior, Label):
    cor = ListProperty([0.3 ,0.5, 0.4, 1])
    cor2 = ListProperty([0.1, 0.1, 0.1, 1])
    def __init__(self, **kwargs):
        super(BotaoPers, self).__init__(**kwargs)
        self.atualizarbotao()
        
    def on_pos(self, *args):
        self.atualizarbotao()
        
    def on_size(self, *args):
        self.atualizarbotao()
    
    def on_press(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor
    
    def on_release(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor
        
    def on_cor(self, *args):
        self.atualizarbotao()
    
    def atualizarbotao(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(size=(self.height*2, self.height), 
                    pos=(self.pos))
            Ellipse(size=(self.height * 2, self.height),
                    pos=(self.x + self.width - self.height*2, self.y))
            Rectangle(size=(self.width - self.height*2, self.height),
                    pos=(self.x + self.height , self.y))

class Rempalavra(GridLayout):

    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.removepalavra.text = text


class MeuApp(App):
    def build(self):
        return Gerenciador()


MeuApp().run()
