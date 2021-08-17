# import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

class SimpleTimer(Label):
    round_length = 5        # ROUND DURATION [SECONDS]    
    eta = round_length  # chyba niepotrzebne, skoro jest w start()
    round_counter = 0   # chyba niepotrzebne, skoro jest w start()
    stored_func_1 = None    # game over
    stored_func_2 = None    # new round
    stored_arg = 1       # round number


    # stopped = False     # chyba niepotrzebne, skoro jest w start() i cancel()
    # round_number = 3      # how many rounds

    def start(self, *args):
        self.stopped = False    # chyba niepotrzebne skoro jest cancel
        # self.eta = self.round_length # hcyba niepotrzebne skoro jest w new_round

        if args:            
            self.stored_func_1 = args[0]    # game over
            self.stored_func_2 = args[1]    # new round
            self.stored_arg = args[2]    # round number
        self.start_round()     

    def start_round(self):
        print("SimpleTimer: New round has started.")
        print("SimpleTimer: Interval: ", self.interval())
        self.eta = self.round_length
        # if self.stored_func_2:  
        #     self.stored_func_2()    # stored new_round
        self.text = str(self.eta)
        self.event = Clock.schedule_interval(self.timer, self.interval())
        print("SimpleTimer: ", str(self.eta))

    def stop(self, *args):   # zatrzymuje wykonywanie funkcji, ale nie Clock
        self.stopped = True
        self.event.cancel()     
        if self.stored_func_1:
            self.stored_func_1()
    
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
                # self.event.cancel()      
                #          
                #### run function end_of_the_round() (from main module)
        else:                                               # aborting timer
            print("SimpleTimer: Stop timer")
            if self.stored_func_1:
                self.stored_func_1()
            # self.event.cancel()
                    
Builder.load_string('''
<SimpleTimer>
    # text: str(round(self.a))
    font_size: '150sp'
    color: '#1A1A1A'
    valign: 'middle' 
    opacity: '1'
''')

class MyApp(App):
    def build(self):
            
        count = SimpleTimer()
        count.start()
        return count


if __name__ == '__main__':
    MyApp().run()