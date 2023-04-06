from pydub import AudioSegment
from pydub.playback import play
from PIL import ImageTk, Image
from tkinter import *
import time
import os

def start_alarm():
    pass
def stop_alarm():
    pass

def gui():
    window = Tk()
    window.title("WAKE UP!")
    # Canvas
    canvas1 = Canvas(window, width=650, height=500, relief='raised')
    canvas1.pack()
    
    start_button = Button(text="Start", command=start_alarm)
                        #width? #height
    canvas1.create_window(250, 400, height=50, width=150, window=start_button)
   
    stop_button = Button(text="Stop", command=stop_alarm)
    canvas1.create_window(400, 400, height=50, width=150, window=stop_button)

    window.resizable(False, False)
    window.mainloop()

def alarm():
    print("Alarm will go off in 1 hour")
    time.sleep(1)
    notification()

def notification():
    print("WAKE UP WAKE UP WAKE UP")
    try:
        while True:
            sound = AudioSegment.from_wav('/home/kenji/Desktop/WAKEUP-APP/affects/alarm-affect.wav')
            play(sound)
    except KeyboardInterrupt:
        print("exiting...")



if __name__ == '__main__':
    gui()
