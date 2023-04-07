from pydub import AudioSegment
from pydub.playback import play
from PIL import ImageTk, Image
from tkinter import *
import time, sys, os

def start_alarm():
    try:
        total_time = int(minute.get()) * 60 + int(second.get())
    except:
        messagebox.showwarning('', 'Invalid Input!')
    while total_time >= 1:
        mins, secs = divmod(total_time, 60)
        if mins > 60:
            mins = divmod(mins, 60)
        
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        window.update()
        time.sleep(1)

        if (total_time == 0):
            messagebox.showinfo("WAKE UP", "WAKE UP TIME TO WAKE UP!!!!")
            
        total_time -= 1

def stop_alarm():
    exit()

def alarm():
    try:
        while True:
            sound = AudioSegment.from_wav('/home/kenji/Desktop/WAKEUP-APP/affects/alarm-affect.wav')
            play(sound)
    except KeyboardInterrupt:
        print("Exiting....")

window = Tk()
window.title("WAKE UP!")

minute=StringVar()
second=StringVar()

minute.set("00")
second.set("03")

fpack = ("Arial",24)

canvas1 = Canvas(window, width=650, height=500, relief='raised')
canvas1.pack()

minutes_box = Entry(window, width=3, font=fpack, textvariable=minute)
minutes_box.place(x=170, y=100)

seconds_box = Entry(window, width=3, font=fpack, textvariable=second)
seconds_box.place(x=250, y=100)

start_button = Button(text="Start", command=start_alarm)
                        #width? #height
canvas1.create_window(250, 400, height=50, width=150, window=start_button)
   
stop_button = Button(text="Stop", command=stop_alarm)
canvas1.create_window(400, 400, height=50, width=150, window=stop_button)

window.resizable(False, False)
window.mainloop()

