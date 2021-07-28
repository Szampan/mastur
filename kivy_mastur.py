from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
# from kivy.uix.layout import Layout


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

        # leftpanel widget          ### ADD LOGO
        self.leftpanel = GridLayout(
                                    rows=6,
                                    size_hint = (1,1),
                                    # padding = (10,0)
                                    )
        self.window.add_widget(self.leftpanel)     

        self.logo = Image(
                        source = "logo.png",
                        size_hint = (0.9,2)
                        )                        
        self.leftpanel.add_widget(self.logo)

        # content widget inside of leftpanel
        self.content = GridLayout(
                                rows=5,
                                size_hint = (1,18),
                                padding = (16,0)
                                )   
        self.leftpanel.add_widget(self.content)

        self.console = Label(
                        text = f"text\n{window_size}\n{self.leftpanel.size}\n{window_size[1]}",  
                        valign = "top",
                        font_size = "10sp",
                        # padding_y = (20, 20),
                        # text_size = [150, None],  
                        # halign = "left",
                        size_hint = (1,2)                 
                        )        
        self.console.bind(size=self.console.setter('text_size'))    # how does it work? 
        self.play = Label(
                        text = f"play" ,
                        valign = "bottom",
                        size_hint = (1,1)                     
                        ) 
        self.play.bind(size=self.play.setter('text_size')) 
        self.sound_name = Label(            
                        text = f"C#",  
                        valign = "middle",                      
                        font_size =  "65sp",
                        color = "#DC1A58",
                        bold = True,
                        # font_name :       # change font? Roboto -> Lato (font file)
                        # font family:  # ?
                        size_hint = (1,2) 
                        )
        self.sound_name.bind(size=self.sound_name.setter('text_size')) 
        self.timer = Label(
                        text = f"00:00",
                        valign = "middle",
                        halign = "center",
                        size_hint = (1,10) 
                        )
        self.timer.bind(size=self.timer.setter('text_size')) 
        self.score = Label(
                        text = f"score: 0",
                        valign="top",
                        size_hint = (1,3) 
                        )
        self.score.bind(size=self.score.setter('text_size')) 
        



        self.content.add_widget(self.console)
        self.content.add_widget(self.play)
        self.content.add_widget(self.sound_name)
        self.content.add_widget(self.timer)
        self.content.add_widget(self.score)




        # fretboard widget
        self.fretboard = GridLayout() 
        self.fretboard.cols = 4
        self.fretboard.size_hint = (0.6,1)
        self.window.add_widget(self.fretboard)

        # EADG strings widgets inside of the fretboard widget        
        frets = 24   

        self.E_string = GridLayout()
        self.E_string.rows = frets+1    

        self.A_string = GridLayout()
        self.A_string.rows = frets+1
        
        self.D_string = GridLayout()
        self.D_string.rows = frets+1
        
        self.G_string = GridLayout()
        self.G_string.rows = frets+1
        
        self.fretboard.add_widget(self.E_string)
        self.fretboard.add_widget(self.A_string)
        self.fretboard.add_widget(self.D_string)
        self.fretboard.add_widget(self.G_string)        

        # fret buttons inside of EADG strings widgets
        for i in range(frets+1):
            # num = i + 1 
            num = i

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
    
    def update(self, *args):
        pass
    
    def callback(self, *args):
        self.console.text = f"string {args[1]} \nfret number {args[0]}"   

    def Frets(self, *args):
        string = args[0]
        i = args[1]       
        num = args[2]
        fret_color = (2.5,0.3,1,1) if num !=0 else (0.3,0.3,0.3,1)  #                                   NA ZEWNĄTRZ?    
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
            size_hint = (2, f**i) if num !=0 else (1,0.5)
            )
        return btn


    # def callback(self, event):
    #     import random
    #     responses = ("OUCH", "Can't touch this!", "Does your mother \nknow about it?", "You are SO oppresive.", "Stop pushing me!", "Get your filthy \nhands of me!")
    #     self.leftpanel.text = str(event.text) + " \n" + str(random.choice(responses)) + "\n\n ...oh, it's you\n\n" 

if __name__ == "__main__":
    Mastur().run()