from pydub import AudioSegment
from pydub.playback import play
from PIL import ImageTk, Image
from tkinter import *
import time, sys, os

def start_alarm():
    time.sleep(1)
    alarm()
def stop_alarm():
    exit()

def alarm():
    try:
        while True:
            sound = AudioSegment.from_wav('/home/kenji/Desktop/WAKEUP-APP/affects/alarm-affect.wav')
            play(sound)
    except KeyboardInterrupt:
        print("Exiting....")

def CountDown():
    pass

window = Tk()
window.title("WAKE UP!")

minute=StringVar()
second=StringVar()

minute.set("60")
second.set("00")

f = ("Arial",24)

canvas1 = Canvas(window, width=650, height=500, relief='raised')
canvas1.pack()

minutes_box = Entry(window, width=3, font=f, textvariable=minute)
minutes_box.place(x=170, y=100)

start_button = Button(text="Start", command=start_alarm)
                        #width? #height
canvas1.create_window(250, 400, height=50, width=150, window=start_button)
   
stop_button = Button(text="Stop", command=stop_alarm)
canvas1.create_window(400, 400, height=50, width=150, window=stop_button)

window.resizable(False, False)
window.mainloop()

