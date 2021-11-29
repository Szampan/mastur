# Mastur v0.3

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.core.window import Window     # to get resolution

from random import choice
from os.path import join, abspath
from functools import partial
from jsonstore import JsonStore

def resource_path(relative_path):
    import sys      # ???
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = abspath(".")
    return join(base_path, relative_path)

class Mastur(App):

    SOUNDS = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    score = 0
    round_score = 0
    round_number = 0
    round_answers = []
    question = None     

    def build(self):     
        Window.size = (350,700)       # mobile screen ratio moreless
        window_size = Window.size          

        self.icon = resource_path("bass-key-128.ico")
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
                        source = resource_path("logo.png"),
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

        self.console_wgt = Label(
                        # Console stays here just in case..
                        # text = f"Window size: {window_size}\nString E, fret 8: {self.note_name('E', 8)}",  
                        # text = f"{self.question}",  
                        valign = "top",
                        font_size = "10sp",
                        size_hint = (1,3)                 
                        )        
        self.console_wgt.bind(size=self.console_wgt.setter('text_size'))   

        self.start_and_sound_wgt = GridLayout(
                                cols = 1,
                                size_hint = (1,2)   
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
                        background_color = (2.5,0.3,1,1)                        
                        )
        self.start_wgt.bind(on_press = partial(self.start_callback))    

        self.counter = SimpleTimer()
        self.counter.size_hint = (1,10)
        self.counter.bind(size=self.counter.setter('text_size'))

        self.score_wgt = Label(
                        text = f"score: ",
                        valign="top",
                        size_hint = (1,3) 
                        )
        self.score_wgt.bind(size=self.score_wgt.setter('text_size'))      

        self.content.add_widget(self.console_wgt)

        self.content.add_widget(self.start_and_sound_wgt)

        self.start_and_sound_wgt.add_widget(self.sound_question_wgt)
        self.start_and_sound_wgt.add_widget(self.start_wgt)    

        self.content.add_widget(self.counter)

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
        for num in range(frets+1):
            self.E_frets = self.frets("E", num)
            self.E_frets.bind(on_press = partial(self.frets_callback, num, "E"))
            self.E_string.add_widget(self.E_frets)

            self.A_frets = self.frets("A", num)
            self.A_frets.bind(on_press = partial(self.frets_callback, num, "A"))
            self.A_string.add_widget(self.A_frets)

            self.D_frets = self.frets("D", num)
            self.D_frets.bind(on_press = partial(self.frets_callback, num, "D"))
            self.D_string.add_widget(self.D_frets)

            self.G_frets = self.frets("G", num)
            self.G_frets.bind(on_press = partial(self.frets_callback, num, "G"))
            self.G_string.add_widget(self.G_frets)      
         
        return self.window
        
    def frets_callback(self, *args):     
        string = args[1]
        fret_number = args[0]       
        answer = (args[1], args[0])  
        bonus = 1   

        if self.is_right(string, fret_number):            
            if answer in self.round_answers:                
                # console_line_3 = "Try somewhere else!"
                pass
            else:      
                # console_line_3 = f"GOOD"
                if 7 < fret_number <= 15:
                    print("Mastur: Bonus x5 for higher positions")    
                    bonus = 5      
                elif fret_number > 15:
                    print("Mastur: Bonus x10 for higher positions")
                    bonus = 10
                self.round_score += (2 ** len(self.round_answers)) * bonus     # Not needed. Used only in print() messages
                self.score += (2 ** len(self.round_answers)) * bonus     # The score grows exponentially
                self.round_answers.append(answer)
            # self.score_wgt.text = f"score: {(self.score + self.round_score)}"
            self.score_wgt.text = f"score: {self.score}"
        else:
            # console_line_3 = f"Not good..."     
            print("Is_right: Bad answer")
            self.game_over()    
            
        ### Console stuff stays here just in case    
        # console_line_1 = f"string: {string} \nfret number: {fret_number}"
        # console_line_2 = f"sound name: {self.note_name(string, fret_number)}"
        # console_line_4 = self.score
        # console_line_5 = self.round_score
        # self.console_wgt.text = f"{console_line_2}\n{console_line_3}\n{console_line_4}\nRound score: {console_line_5}"
        
    def start_callback(self, *args):        
      
        # self.console_wgt.text = f"Mastur: Start!"   
        self.score = 0     # RESET
        
        self.new_round()
        
        self.score_wgt.text = f"score: 0"
        self.start_wgt.size_hint = (0, 0)
        self.start_wgt.opacity = 0
        self.start_wgt.disabled = True
        self.sound_question_wgt.size_hint = (1,1)
        self.sound_question_wgt.opacity = 1                       

    def new_round(self):   
        self.round_number += 1       
        print("Mastur: Round number ", self.round_number)   
        
        self.counter.opacity = 1
        self.fretboard.disabled = False        
        
        self.question = self.random_sound()
        print(f"Mastur: Sound to guess: {self.question}")
        self.sound_question_wgt.text = f"{self.question}"
        self.counter.start(self.round_over, self.new_round, self.round_number)       

    def round_over(self):
        print("Mastur: The round is over")
        
        ### add round counter

        if self.round_score == 0:
            print("Mastur: Game over (time's up)")
            self.game_over()
        else:
            print(f"Mastur: Gained {self.round_score} in this round")
            self.score += self.round_score
            self.round_score = 0        # RESET     
            self.round_answers.clear()  # RESET       
            self.new_round()

    def game_over(self):
        self.check_highscore(self.score)

        self.sound_question_wgt.size_hint = (0,0)
        self.sound_question_wgt.opacity = 0     

        self.start_wgt.size_hint = (1, 1)          # Add function hide_wgt(wgt, state=False)
        self.start_wgt.opacity = 1
        self.counter.opacity = 0
        self.start_wgt.disabled = False
        self.fretboard.disabled = True      
      
        self.round_number = 0
        self.round_answers.clear()          # RESET
        self.counter.event.cancel()         # Works great

    def frets(self, *args):
        string = args[0]        
        num = args[1]
        fret_color = (2.5,0.3,1,1) if num !=0 else (0.3,0.3,0.3,1)  #                                   NA ZEWNĄTRZ?    
        
        f = 0.944                   # length of each subsequent fret       
        
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
            size_hint = (2, f**num) if num !=0 else (1,0.5)
            )
        return btn

    def note_name(self, *args): # return a name of the sound assigned to a fret on the particular string
        string_name = str(args[0])
        fret = args[1]
        sounds = self.SOUNDS
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
        while True:
            print("Mastur: Generate new sound")
            new_question = choice(self.SOUNDS)
            if new_question != self.question:
                break
        return new_question   

    def is_right(self, *args):        
        string_name = args[0]
        fret = args[1]
        if self.note_name(string_name, fret) == self.question:        # do czego przypisać question?            
            return True
        else:            
            return False
    
    def check_highscore(self, current_score):
        data_dir = getattr(self, 'user_data_dir')      
        score_file = JsonStore(join(data_dir, 'mastur_hs.json'))        
        ### Try this if directory problems on other platforms ###
        # from kivy import kivy_home_dir          
        # score_file = JsonStore(join(kivy_home_dir, 'highscore.json'))        
        # print(data_dir)

        try:  
            old_highscore = score_file.highscore      
            if current_score > old_highscore:
                score_file.highscore = current_score                
                self.score_wgt.text = f"new highscore: {score_file.highscore}!"
                print(f"Score:New highscore: {score_file.highscore}!")
            else:       
                self.score_wgt.text = f"score: {current_score} \nhighscore: {score_file.highscore}"
                print(f"score: {current_score} \nhighscore: {score_file.highscore}")
        except:            
            print("Score: Create highscore record")
            score_file.highscore = current_score      

class SimpleTimer(Label):
    round_length = 5            # round duration [SECONDS]    
    stored_round_over = None    # round over
    stored_new_round = None     # new round
    stored_arg = 1              # round number

    def start(self, *args):
        self.stopped = False       
        if args:            
            self.stored_round_over = args[0]    # round over
            self.stored_new_round = args[1]     # new round
            self.stored_arg = args[2]           # round number
        self.start_round()     

    def start_round(self):
        print("SimpleTimer: New round has started.")
        print("SimpleTimer: Interval: ", self.interval())
        self.eta = self.round_length
        self.text = str(self.eta)
        self.event = Clock.schedule_interval(self.timer, self.interval())
        print("SimpleTimer: ", str(self.eta))

    def stop(self, *args):  
        self.stopped = True
        self.event.cancel()     
        if self.stored_round_over:
            self.stored_round_over()
    
    def interval(self):
        return 0.95 ** self.stored_arg
        
    def timer(self, dt):
        print("SimpleTimer: working...")

        if not self.stopped:
            if self.eta != 0:            
                self.eta -= 1
                self.text = str(self.eta)
                print("SimpleTimer: ", str(self.eta))
            else:                
                print("SimpleTimer: End of the round!")
                self.stop() 
        else:                                               # aborting timer
            print("SimpleTimer: Stop timer")
            if self.stored_round_over:
                self.stored_round_over()
                    
Builder.load_string('''
<SimpleTimer>
    # text: str(round(self.a))
    font_size: '150sp'
    color: '#1A1A1A'
    valign: 'middle' 
    opacity: '1'
''')    
                    

if __name__ == "__main__":
    Mastur().run()

