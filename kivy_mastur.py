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
        f = 0.944       # length of every next fret
        frets = 24     
        fret_color = (2.5,0.3,1,1)

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
            num = i + 1                                     # TODO: clean this part
            symbol1 = ""
            symbol2 = ""
            if num in (3, 5, 7, 9, 15, 17, 21) :
                symbol1 = "•"
            elif num in (12, 24):
                symbol1 += "•"
                symbol2 ="•"

            self.E_frets = Button(                 # TODO: create class for fret buttons
                # text = (f'Fret {num}, {f**i}{symbol}'), 
                text = (f'{symbol1} {num}'), 
                background_color = (fret_color),
               # background_normal = '',
                border = (5,5,5,5),
                size_hint = (2, f**i),
                )
                
            self.E_frets.bind(on_press = partial(self.callback, num)) # w dokumentacji o eventach jest np coś z lambdą albo z **kwargs
            # self.E_frets.bind(on_press = partial(self.callback, "WOW")) 
            self.E_string.add_widget(self.E_frets)

            # self.Estring.add_widget(Button(                 # TODO: create class for fret buttons
            #     # text = (f'Fret {num}, {f**i}{symbol}'), 
            #     text = (f'{symbol1}'), 
            #     background_color = (fret_color),
            #    # background_normal = '',
            #     border = (5,5,5,5),
            #     size_hint = (2, f**i),
            #     # bind = on_press = self.callback
            #     ))            
            self.A_string.add_widget(Button(
                # text = (f'Fret {num}, {f**i}{symbol}'), 
                text = (f''), 
                background_color = (fret_color),
               # background_normal = '',
                border = (5,5,5,5),
                size_hint = (2, f**i)
                ))
            self.D_string.add_widget(Button(
                # text = (f'Fret {num}, {f**i}{symbol}'), 
                text = (f'{symbol2}'), 
                background_color = (fret_color),
               # background_normal = '',
                border = (5,5,5,5),
                size_hint = (2, f**i)
                ))
            self.G_string.add_widget(Button(
                # text = (f'Fret {num}, {f**i}{symbol}'), 
                text = (f''), 
                background_color = (fret_color),
               # background_normal = '',
                border = (5,5,5,5),
                size_hint = (2, f**i)
                ))      
            
         
        return self.window
    
    def callback(self, *args):
        self.leftpanel.text = f"string X \nfret number {args[0]}"   


    # def callback(self, event):
    #     import random
    #     responses = ("OUCH", "Can't touch this!", "Does your mother \nknow about it?", "You are SO oppresive.", "Stop pushing me!", "Get your filthy \nhands of me!")
    #     self.leftpanel.text = str(event.text) + " \n" + str(random.choice(responses)) + "\n\n ...oh, it's you\n\n" 

if __name__ == "__main__":
    Mastur().run()