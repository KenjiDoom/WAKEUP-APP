from PIL import ImageTk, Image
from tkinter import messagebox
import time, sys, os, pygame
from tkinter import *
 
pygame.mixer.init()

def start_alarm():
    try:
        total_time = int(minute.get()) * 60 + int(second.get())
    except:
        messagebox.showwarning('', 'Invalid Input!')
    while total_time >- 1:
        mins, secs = divmod(total_time, 60)
        if mins > 60:
            mins = divmod(mins, 60)
        
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        window.update()
        time.sleep(1)

        if (total_time == 0):
            pygame.mixer.music.load("/home/kenji/Desktop/WAKEUP-APP/affects/alarm-affect.wav")
            pygame.mixer.music.play(loops=0)
            messagebox.showinfo("WAKE UP", "WAKE UP TIME TO WAKE UP!!!!")
            exit()

        total_time -= 1

def stop_program():
    exit()

window = Tk()
window.title("WAKE UP!")

minute=StringVar()
second=StringVar()

minute.set("00")
second.set("01")

fpack = ("Noto Sans Mandaic",40)

canvas1 = Canvas(window, width=650, height=500, relief='raised')
canvas1.pack()


# Minute Label
minutes_box = Label(window, width=3, font=fpack, textvariable=minute)
minutes_box.place(x=170, y=100)

# Second Label
seconds_box = Label(window, width=3, font=fpack, textvariable=second)
seconds_box.place(x=300, y=100)

# Start button
start_button = Button(text="Start", command=start_alarm)
                        #width? #height
canvas1.create_window(250, 400, height=50, width=150, window=start_button)

# Stop Button   
stop_button = Button(text="Stop", command=stop_program)
canvas1.create_window(400, 400, height=50, width=150, window=stop_button)

window.resizable(False, False)
window.mainloop()

