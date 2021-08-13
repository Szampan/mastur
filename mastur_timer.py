from random import randint
from kivy.animation import Animation
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.label import Label


class IncrediblyCrudeClock(Label):
    a = NumericProperty(0)  # Number of seconds to countdown
    stored_func_1 = None
    stored_func_2 = None

    def __init__(self, **kwargs):        
        self.max_laps = kwargs.pop('laps', 2)  # default is to do 2 laps (zadziała jeśli lapsy nie będą podane)
        self.lap_counter = 0
        super(IncrediblyCrudeClock, self).__init__(**kwargs)    # most classes must have their own __init__() executed in order to work correctly. The super calls the __init__() of the Label

    def stop(self):
        print("KONIEC")
        
        return      #  timer się nie wyłącza !!!!! 
                    # ta funkcja mogłaby wysyłać sygnał

    '''
    def signal cośtam
    a ta funkcja mogłaby odpalać funkcję start i czekać na sygnał do wyłączenia
    '''

    def start(self, *args):    
        # print(TEST)
        
        if self.lap_counter == 0 and args:
            print("zewnętrzny argument: ", args[0])
            self.stored_func_1 = args[0]
            self.stored_func_2 = args[1]

        self.lap_counter += 1
        self.a = 3.3      # seconds
        self.anim = Animation(a=0, duration=self.a)
        if self.lap_counter >= self.max_laps:
            # this is the last lap, set on_complete to call self.finish_callback
            self.anim.bind(on_complete=self.finish_callback)
            
        else:          
            print('Start!')
            self.anim.bind(on_complete=self.start)
        print('starting anim number', self.lap_counter)        
        if self.stored_func_2:
            self.stored_func_2()    # call new round
        self.anim.start(self)

    def finish_callback(self, animation, incr_crude_clock):        
        self.text = '' 
        self.lap_counter = 0
        
        print("KONIEC")
        if self.stored_func_1:            
            self.stored_func_1()    # call game over            

Builder.load_string('''
<IncrediblyCrudeClock>
    text: str(round(self.a))
    font_size: '150sp'
    color: '#1A1A1A'
    valign: 'middle' 
    # opacity: '0'
''')


class TimeApp(App):
    def build(self):
        # specify the number of repetitions in the constructor
        crudeclock = IncrediblyCrudeClock(laps=3)
        crudeclock.start()
        return crudeclock

if __name__ == "__main__":
    TimeApp().run()