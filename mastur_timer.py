from random import randint
from kivy.animation import Animation
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.label import Label


class IncrediblyCrudeClock(Label):
    a = NumericProperty(0)  # Number of seconds to countdown

    def __init__(self, **kwargs):        
        self.max_laps = kwargs.pop('laps', 2)  # default is to do 2 laps (zadziała jeśli lapsy nie będą podane)
        self.lap_counter = 0
        super(IncrediblyCrudeClock, self).__init__(**kwargs)    # most classes must have their own __init__() executed in order to work correctly. The super calls the __init__() of the Label

    def start(self, *args):
        self.lap_counter += 1
        self.a = 3      # seconds
        self.anim = Animation(a=0, duration=self.a)
        if self.lap_counter >= self.max_laps:
            # this is the last lap, set on_complete to call self.finish_callback
            self.anim.bind(on_complete=self.finish_callback)

        else:
            # not finished yet, call self.start again
            # MASTUR: call function generating new sound name 
            print('Start!')
            self.anim.bind(on_complete=self.start)
        print('starting anim number', self.lap_counter)
        self.anim.start(self)

    def finish_callback(self, animation, incr_crude_clock):
        print('in finish_callback')
        # MASTUR: Well done. Your score: XXX
        self.text = 'FINISHED' 

Builder.load_string('''
<IncrediblyCrudeClock>
    text: str(round(self.a))
''')


class TimeApp(App):
    def build(self):
        # specify the number of repetitions in the constructor
        crudeclock = IncrediblyCrudeClock(laps=3)
        crudeclock.start()
        return crudeclock

if __name__ == "__main__":
    TimeApp().run()