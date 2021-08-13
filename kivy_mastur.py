from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

from kivy.core.window import Window     # to get resolution

# from kivy.lang import Builder

from functools import partial
from random import choice

from mastur_timer import IncrediblyCrudeClock



class Mastur(App):

    sounds = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    score = 0
    question = None     

    def build(self):     
        Window.size = (350,700)       # mobile screen ratio moreless
        window_size = Window.size          

        self.window = GridLayout()       
        self.window.cols = 2

        # leftpanel widget         
        self.leftpanel = GridLayout(
                                    rows=2,
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
                                rows=6, # docelowo ma być 5 (6 jest na potrzeby testów)
                                size_hint = (1,18),
                                padding = (16,0)
                                )   
        self.leftpanel.add_widget(self.content)

        self.console_wgt = Label(
                        # text = f"Window size: {window_size}\nString E, fret 8: {self.note_name('E', 8)}",  
                        text = f"{self.question}",  
                        valign = "top",
                        font_size = "10sp",
                        # padding_y = (20, 20),
                        # text_size = [150, None],  
                        # halign = "left",
                        size_hint = (1,2)                 
                        )        
        self.console_wgt.bind(size=self.console_wgt.setter('text_size'))    # how does it work? 
        self.play_txt_wgt = Label(              # CHYBA NIEPOTRZEBNY
                        text = f"",             # było "play"
                        valign = "bottom",
                        size_hint = (1,1)                     
                        ) 
        self.play_txt_wgt.bind(size=self.play_txt_wgt.setter('text_size')) 

        self.start_and_sound_wgt = GridLayout(
                                cols = 1,
                                size_hint = (1,2)                               # 
                                
                                )

        self.sound_question_wgt = Label(           # SHOW AFTER START, HIDE WHEN GAME OVER
                        text = f"{self.question}",  
                        valign = "middle",                      
                        font_size =  "65sp",
                        color = "#DC1A58",
                        bold = True,                     
                        size_hint = (0,0),  
                        opacity = 0
                        )
        self.sound_question_wgt.bind(size=self.sound_question_wgt.setter('text_size')) 


        self.start_wgt = Button(                    # HIDE AFTER START, SHOW WHEN GAME OVER
                        text = "START",
                        background_color = (2.5,0.3,1,1),
                        # opacity = 0.5,
                        # disabled = True,
                        
                        )
        self.start_wgt.bind(on_press = partial(self.start_callback))    

        self.crudeclock = IncrediblyCrudeClock(laps=3)  
        self.crudeclock.size_hint = (1,10)        
        self.crudeclock.bind(size=self.crudeclock.setter('text_size')) 
        # self.timer_wgt = Label(
        #                 text = f"00:00",
        #                 valign = "middle",
        #                 halign = "center",
        #                 size_hint = (1,10) 
        #                 )
        # self.timer_wgt.bind(size=self.timer_wgt.setter('text_size')) 


  
        # self.crudeclock.start()


        self.score_wgt = Label(
                        text = f"score: ",
                        valign="top",
                        size_hint = (1,3) 
                        )
        self.score_wgt.bind(size=self.score_wgt.setter('text_size'))      

        self.content.add_widget(self.console_wgt)
        self.content.add_widget(self.play_txt_wgt)      # CHYBA NIEPOTRZEBNE

        self.content.add_widget(self.start_and_sound_wgt)

        self.start_and_sound_wgt.add_widget(self.sound_question_wgt)
        # self.content.add_widget(self.timer_wgt)
        self.start_and_sound_wgt.add_widget(self.start_wgt)      # testowo

        self.content.add_widget(self.crudeclock)
        self.content.add_widget(self.score_wgt)

        # fretboard widget
        self.fretboard = GridLayout(
                        cols = 4,
                        size_hint = (0.6,1),
                        disabled = True
                        )        
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
            self.E_frets = self.frets("E", i, num)
            self.E_frets.bind(on_press = partial(self.callback, num, "E"))
            self.E_string.add_widget(self.E_frets)

            self.A_frets = self.frets("A", i, num)
            self.A_frets.bind(on_press = partial(self.callback, num, "A"))
            self.A_string.add_widget(self.A_frets)

            self.D_frets = self.frets("D", i, num)
            self.D_frets.bind(on_press = partial(self.callback, num, "D"))
            self.D_string.add_widget(self.D_frets)

            self.G_frets = self.frets("G", i, num)
            self.G_frets.bind(on_press = partial(self.callback, num, "G"))
            self.G_string.add_widget(self.G_frets)      
         
        return self.window
    
    # def update(self, *args):
    #     pass
    
    def callback(self, *args):     
        string = args[1]
        fret_number = args[0]           
        line_1 = f"string: {string} \nfret number: {fret_number}"
        line_2 = f"sound name: {self.note_name(string, fret_number)}"

        if self.is_right(string, fret_number):
            line_3 = f"GOOD"
            self.score += 1
        else:
            line_3 = f"Not good..."
            # self.score = 0    # old version 
            self.game_over()    # NAPRAWIĆ: game over nie przerywa timera
            
        line_4 = self.score

        self.console_wgt.text = f"{line_2}\n{line_3}\n{line_4}"   
        self.score_wgt.text = f"score: {self.score}"
        # self.console.text = f"string {args[1]} \nfret number {args[0]}\nString E, fret 8: {self.note_name('e', 8)}"   

    def start_callback(self, *args):        
      
        # self.question = self.random_sound()
        # print(f"Sound to guess: {self.question}")
        # self.sound_question_wgt.text = f"{self.question}"

        # self.new_round()
        self.console_wgt.text = f"Start!"   
        self.score = 0
        self.crudeclock.start(self.game_over, self.new_round)         # function passed to a child as an argument
        
        self.start_wgt.size_hint = (0, 0)
        self.start_wgt.opacity = 0
        self.start_wgt.disabled = True
        self.sound_question_wgt.size_hint = (1,1)
        self.sound_question_wgt.opacity = 1
               

    def new_round(self):        
        # wprowadzić do klasy atrybut przechowujący stan gry (runda trwa, albo nie). 
        # jeśli runda nie trwa, to timer się wyłącza? (jak?)
        # a fretboard pozostaje disabled
        # ROZWIĄZANIE 1: przepisać klasę timera do głównego pliku i wykorzystać loop=True sprawdzany co odświeżenie timera

        self.question = self.random_sound()
        print(f"Sound to guess: {self.question}")
        self.sound_question_wgt.text = f"{self.question}"
        self.crudeclock.opacity = 1
        self.fretboard.disabled = False

    def game_over(self):
        
        self.console_wgt.text = f"Game over\nYour score: {self.score}"  
        print(f"Game over\nYour score: {self.score}")

        self.sound_question_wgt.size_hint = (0,0)
        self.sound_question_wgt.opacity = 0     

        self.start_wgt.size_hint = (1, 1)          # zrobić funkcję hide_wgt(wgt, state=False)
        self.start_wgt.opacity = 1
        self.start_wgt.disabled = False
        self.fretboard.disabled = True      

        IncrediblyCrudeClock().stop() #   próba wyłączenia timera..

    def frets(self, *args):
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

    def note_name(self, *args): # return a name of the sound assigned to a fret on the particular string
        string_name = str(args[0])
        fret = args[1]
        sounds = self.sounds
        if fret > 24:
            print("There are 24 frets!")        
        else:
            if string_name == "E":
                while fret > 4:
                    fret -= 12
                sound = sounds[fret + 7]
                return sound
            elif string_name == "A":
                while fret > 11:
                    fret -= 12
                sound = sounds[fret]
                return sound        
            elif string_name == "D":
                while fret > 6:
                    fret -= 12
                sound = sounds[fret + 5]
                return sound
            elif string_name == "G":
                while fret > 1:
                    fret -= 12
                sound = sounds[fret + 10]
                return sound
            else:
                print(f"Error\nname: {string_name}\nfret: {fret}")
                return "-"

    def random_sound(self):
        return choice(self.sounds)
    

    def is_right(self, *args):        
        string_name = args[0]
        fret = args[1]
        # self.q_test = args[2]
        if self.note_name(string_name, fret) == self.question:        # do czego przypisać question?
            print("ok!")
            return True
        else:
            print("wrong")
            return False


# question = Mastur().random_sound()


    # def callback(self, event):
    #     import random
    #     responses = ("OUCH", "Can't touch this!", "Does your mother \nknow about it?", "You are SO oppresive.", "Stop pushing me!", "Get your filthy \nhands of me!")
    #     self.leftpanel.text = str(event.text) + " \n" + str(random.choice(responses)) + "\n\n ...oh, it's you\n\n" 

if __name__ == "__main__":
    Mastur().run()