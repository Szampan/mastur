from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.image import Image



class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 2

        # add widgets to window

        # text widget
        self.left = Label(
                        text = "text"
                        ) 
        self.window.add_widget(self.left)


        # fretboard widget
        self.fretboard = GridLayout() 
        self.fretboard.rows = 24
        self.window.add_widget(self.fretboard)

        for i in range(24):
            self.fretboard.add_widget(Button(text=(f'Hello {i+1}')))
        
 

        # self.fretboard = Label(
        #                 text = "fretboard"
        #                 ) 
        # self.window.add_widget(self.fretboard)

        
        # self.fretboard = 
        # self.layout = BoxLayout(padding=10)

        #self.window = BoxLayout(orientation='vertical')

        #btn1 = Button(text='Hello')
        #btn2 = Button(text='World')
        #self.window.add_widget(btn1)
        #self.window.add_widget(btn2)


        return self.window

if __name__ == "__main__":
    SayHello().run()