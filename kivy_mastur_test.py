from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.image import Image

from functools import partial

from kivy.core.window import Window     # to get resolution

from kivymd.uix.button import MDFlatButton

from kivy.config import Config


class Mastur(App):
    def build(self):
                     
        Window.size = (350,700)       # mobile screen ratio moreless
        window_size = Window.size  

        self.window = GridLayout()       
        self.window.cols = 2

        # add widgets to window     

        # leftpanel widget
        self.leftpanel = Label(
                        text = f"text\n{window_size}"                     
                        ) 
        self.window.add_widget(self.leftpanel)

        # fretboard widget
        self.fretboard = GridLayout() 
        self.fretboard.cols = 4
        self.fretboard.size_hint = (0.6,1)
        self.window.add_widget(self.fretboard)

        # EADG strings widgets inside of the fretboard widget        
        frets = 24   

        self.E_string = GridLayout()
        self.E_string.rows = frets

        self.A_string = GridLayout()
        self.A_string.rows = frets
        
        self.D_string = GridLayout()
        self.D_string.rows = frets
        
        self.G_string = GridLayout()
        self.G_string.rows = frets
        
        self.fretboard.add_widget(self.E_string)
        self.fretboard.add_widget(self.A_string)
        self.fretboard.add_widget(self.D_string)
        self.fretboard.add_widget(self.G_string)        

        # fret buttons inside of EADG strings widgets
        for i in range(frets):
            num = i + 1 

            self.E_frets = self.Frets("E", i, num)
            self.E_frets.bind(on_press = partial(self.callback, num, "E"))
            self.E_string.add_widget(self.E_frets)

            self.A_frets = self.Frets("A", i, num)
            self.A_frets.bind(on_press = partial(self.callback, num, "A"))
            self.A_string.add_widget(self.A_frets)

            self.D_frets = self.Frets("D", i, num)
            self.D_frets.bind(on_press = partial(self.callback, num, "D"))
            self.D_string.add_widget(self.D_frets)

            self.G_frets = self.Frets("G", i, num)
            self.G_frets.bind(on_press = partial(self.callback, num, "G"))
            self.G_string.add_widget(self.G_frets)      
         
        return self.window
    
    def callback(self, *args):
        self.leftpanel.text = f"string {args[1]} \nfret number {args[0]}"   

    def Frets(self, *args):
        string = args[0]
        i = args[1]       
        num = args[2]
        fret_color = (2.5,0.3,1,1)  #                                   NA ZEWNĄTRZ?    
        f = 0.944                   # length of each subsequent fret    NA ZEWNĄTRZ?        
        
        symbol, symbol1, symbol2 = " " *3
        if num in (3, 5, 7, 9, 15, 17, 21) :
            symbol1 = "•"
        elif num in (12, 24):
            symbol1, symbol2 ="•" *2

        if string == "E":
            symbol = symbol1
        elif string == "D":
            symbol = symbol2

        btn = Button(                 
            text = (f'{symbol}'),
            background_color = (fret_color),               
            border = (5,5,5,5),
            size_hint = (2, f**i)
            )
        return btn


    # def callback(self, event):
    #     import random
    #     responses = ("OUCH", "Can't touch this!", "Does your mother \nknow about it?", "You are SO oppresive.", "Stop pushing me!", "Get your filthy \nhands of me!")
    #     self.leftpanel.text = str(event.text) + " \n" + str(random.choice(responses)) + "\n\n ...oh, it's you\n\n" 

if __name__ == "__main__":
    Mastur().run()