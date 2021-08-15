import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

class DaTimer(Label):
    stopped = False
    round_length = 5    # round duration [seconds]
    round_number = 3    # how many rounds
    eta = round_length
    round_counter = 0
    # stored_func_1 = None
    # stored_func_2 = None

    def start(self, *args):
        self.stopped = False
        self.round_counter = 0
        self.eta = self.round_length

        if args:
            # print("zewnętrzne argumenty: ", list(args))
            self.stored_func_1 = args[0]    # game over
            self.stored_func_2 = args[1]    # new round

        self.new_round()
                
        # dodać do klasy DaTimer przyjmowanie argumentów z ilością i długością rund?
     
        self.main_box = BoxLayout(orientation='vertical')        
        self.button = Button(text=str(self.eta), font_size=100)
        self.main_box.add_widget(self.button)
    
        self.bind(on_press=self.stop)


        # self.text = str(self.eta)
        # self.event = Clock.schedule_interval(self.timer, 1)
        
      
    def new_round(self):
        print("DaTimer: Next round started.")
        self.eta = self.round_length
        if self.stored_func_2:
            self.stored_func_2()
        self.text = str(self.eta)
        self.event = Clock.schedule_interval(self.timer, 1)
        print("DaTimer: ", str(self.eta))

    def stop(self, *args):      
        self.stopped = True
        print("DaTimer: ", self.stopped)
        
    def timer(self, dt):
        ### REBUILD THIS LOGIC. CHECK ROUND FIRST ###

        ### Źle 1: Po upływie czasu tury, zaczynają lecieć dwa równoległe czasy i coś się pieprzy

        ### Źle 2: po upływie czasu, kiedy przynajmniej jeden dźwięk 
        ### nie był odgadnięty, powinien być game over.
        ### Może przenieść liczenie rund do modułu głównego, żeby było  
        ### bardziej związane z liczeniem punktów?

        print("DaTimer: working...")
        if not self.stopped and self.eta != 0:              # round
            if self.round_counter == 0:
                self.round_counter += 1
                print("DaTimer: Round number ", self.round_counter)  
                # if self.stored_func_2:
                #     self.stored_func_2()            
            self.eta -= 1
            self.text = str(self.eta)
            print("DaTimer: ", str(self.eta))
        elif self.eta == 0:                                 # end of round
            if self.round_counter < self.round_number:      # next round or..
                print("DaTimer: Next round!")
                self.round_counter += 1                
                # self.eta = self.round_length
                print("DaTimer: Round number ", self.round_counter)
                self.new_round()
                # if self.stored_func_2:
                #     self.stored_func_2()            
                # self.text = str(self.eta)
                # print("DaTimer: ", str(self.eta))
            else:                                           # ..nomore rounds
                # self.event.cancel()
                self.text = ""
                print("DaTimer: FINISHED")
                if self.stored_func_1:
                    self.stored_func_1()
        else:                                               # aborting timer
            print("DaTimer: Stop timer")
            if self.stored_func_1:
                self.stored_func_1()
            # self.event.cancel()
                    
Builder.load_string('''
<DaTimer>
    # text: str(round(self.a))
    font_size: '150sp'
    color: '#1A1A1A'
    valign: 'middle' 
    opacity: '0'
''')

class MyApp(App):
    def build(self):
            
        count = DaTimer()
        count.start()
        return count


if __name__ == '__main__':
    MyApp().run()