from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.image import Image

from kivy.core.window import Window     # to get resolution

from kivymd.uix.button import MDFlatButton

from kivy.config import Config




class SayHello(App):
    def build(self):
        # self.theme_cls.primary_palette = "Red"


             
        Window.size = (350,700)       #proporcje telefonu mniej więcej
        window_size = Window.size  

        self.window = GridLayout()       
        self.window.cols = 2

        # add widgets to window

        # text widgetgit 
        

        self.left = Label(
                        text = f"text\n{window_size}"                     
                        ) 
        self.window.add_widget(self.left)


        # fretboard widget
        self.fretboard = GridLayout() 
        self.fretboard.cols = 4
        self.fretboard.size_hint = (0.6,1)
        self.window.add_widget(self.fretboard)

        f = 0.944
        frets = 24
        fret_color = (2.5,0.3,1,1)

        self.Estring = GridLayout()
        self.Estring.rows = frets

        self.Astring = GridLayout()
        self.Astring.rows = frets
        
        self.Dstring = GridLayout()
        self.Dstring.rows = frets
        
        self.Gstring = GridLayout()
        self.Gstring.rows = frets

        self.fretboard.add_widget(self.Estring)
        self.fretboard.add_widget(self.Astring)
        self.fretboard.add_widget(self.Dstring)
        self.fretboard.add_widget(self.Gstring)                



        for i in range(frets):
            num = i + 1
            symbol1 = ""
            symbol2 = ""
            if num in (3, 5, 7, 9, 15, 17, 21) :
                symbol1 = "*"
            elif num in (12, 24):
                symbol1 += "*"
                symbol2 ="*"

            self.Estring.add_widget(Button(
                # text = (f'Fret {num}, {f**i}{symbol}'), 
                text = (f'{symbol1}'), 
                background_color = (fret_color),
               # background_normal = '',
                border = (5,5,5,5),
                size_hint = (2, f**i)
                ))
            
            self.Astring.add_widget(Button(
                # text = (f'Fret {num}, {f**i}{symbol}'), 
                text = (f''), 
                background_color = (fret_color),
               # background_normal = '',
                border = (5,5,5,5),
                size_hint = (2, f**i)
                ))            

            self.Dstring.add_widget(Button(
                # text = (f'Fret {num}, {f**i}{symbol}'), 
                text = (f'{symbol2}'), 
                background_color = (fret_color),
               # background_normal = '',
                border = (5,5,5,5),
                size_hint = (2, f**i)
                ))            
                
            self.Gstring.add_widget(Button(
                # text = (f'Fret {num}, {f**i}{symbol}'), 
                text = (f''), 
                background_color = (fret_color),
               # background_normal = '',
                border = (5,5,5,5),
                size_hint = (2, f**i)
                ))      
        
 

        # self.fretboard = Label(
        #                 text = "fretboard"
        #                 ) 
        # self.window.add_widget(self.fretboard)

        
        # self.fretboard = 
        # self.layout = BoxLayout(padding=10)

        #self.window = BoxLayout(orientation='vertical')

        #btn1 = Button(text='Hello')
        #btn2 = Button(text='World')
        #self.window.add_widget(btn1)
        #self.window.add_widget(btn2)


        return self.window

if __name__ == "__main__":
    SayHello().run()