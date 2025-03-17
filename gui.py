from tkinter import *
from tkinter import ttk
from dimits import Dimits
import os
from pygame import mixer
import sys

voice_name = ""
print(len(sys.argv))
if len(sys.argv) > 1:
    voice_name = sys.argv[1]
else:
    print("No model specified.")
    exit()
dt = Dimits(voice_name)
mixer.init()

def piper_kb(*args):
    piper()

def clear_input(*args):
    global T
    T.delete('1.0', END)

def piper():
    global dt
    global mixer
    input = T.get("1.0",END)
    dt.text_2_audio_file(input, 'output', './output', format="wav")
    sound = mixer.Sound("./output/output.wav")
    sound.play()

root = Tk()

l = Label(root, text = "Quick Piper GUI v0.0.1")
T = Text(root, height = 5, width = 52)
citeste = Button(root, text = "Read", command = piper) 
distruge = Button(root, text = "Exit", command = root.destroy) 

l.pack()
T.pack()
citeste.pack()
distruge.pack()

root.bind('<Control-Return>', piper_kb)
root.bind('<Control-a>', clear_input)


root.mainloop()