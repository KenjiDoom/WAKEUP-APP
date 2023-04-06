from pydub import AudioSegment
from pydub.playback import play
from PIL import ImageTk, Image
from tkinter import *
import time
import os


def gui():
    window = Tk()
    window.title("WAKE UP!")
    # Canvas
    canvas1 = Canvas(window, width=650, height=500, relief='raised')
    canvas1.pack()
    
    # We two buttons stop and restart
    stop_button = Button(text="Stop")
    canvas1.create_window(500, 300, window=stop_button)
    # Restart button
    restart_button = Button(text="Restart")
    canvas1.create_window(500, 250, window=restart_button)

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
