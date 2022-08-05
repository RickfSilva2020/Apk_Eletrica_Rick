from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


# CLASSE PARA GERENCIAR AS TELAS
class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass
        
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


class Rempalavra(GridLayout):

    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.removepalavra.text = text


class MeuApp(App):
    def build(self):
        return Gerenciador()


MeuApp().run()
