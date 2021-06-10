import pyttsx3

engine = pyttsx3.init()
name = input("What's your name?")
engine.say(name)
engine.runAndWait()