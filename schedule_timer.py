import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class DaTimer(Label):
    stopped = False
    round_length = 5    # round duration [seconds]
    round_number = 3    # how many rounds
    eta = round_length
    round_counter = 0

    def start(self, *args):
        self.text = str(self.eta)

        # OZNACZYC PRZYJMOWANE ARGUMENTY

        # ZROBIĆ RUNDY (w tej klasie albo w głównym programie)
        # DODAĆ AKCJE STERUJĄCE MASTURBEJSEM

        self.main_box = BoxLayout(orientation='vertical')        
        self.button = Button(text=str(self.eta), font_size=100)
        self.main_box.add_widget(self.button)
    
        self.bind(on_press=self.stop)



        self.event = Clock.schedule_interval(self.timer, 1)
        
        # return self.main_box
    
    def stop(self, button):
        

        self.stopped = True
        print(self.stopped)
        
    def timer(self, dt):
        ### REBUILD THIS LOGIC. CHECK ROUND FIRST ###
        print("working...")
        if not self.stopped and self.eta != 0:
            if self.round_counter == 0:
                self.round_counter += 1
                print("Round number ", self.round_counter)              
            self.eta -= 1
            self.text = str(self.eta)
            print(str(self.eta))
        elif self.eta == 0:                                 # end of time
            if self.round_counter < self.round_number:      # next round or..
                print("once again!")
                self.round_counter += 1
                self.start
                self.eta = self.round_length
                print("Round number ", self.round_counter)
                self.text = str(self.eta)
                print(str(self.eta))
            else:                                           # ..nomore rounds
                self.event.cancel()
                self.text = ""
                print("FINISHED")
        else:                                               # aborting timer
            print("Stop timer")
            self.event.cancel()
            

            
            

class MyApp(App):
    def build(self):
            
        count = DaTimer()
        count.start()
        return count


if __name__ == '__main__':
    MyApp().run()