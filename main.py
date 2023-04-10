from PIL import ImageTk, Image
from tkinter import messagebox
from CTkMessagebox import CTkMessagebox
import time, sys, os, pygame, customtkinter
from tkinter import *
 
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
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
            #messagebox.showinfo("WAKE UP", "WAKE UP TIME TO WAKE UP!!!!")
            msg = CTkMessagebox(title="WAKE UP!", message="1 HOUR OF CODE IS UP!",
                  icon="warning", option_1="Exit")
    
            if msg.get()=="Exit":
                exit()
                
        total_time -= 1

def stop_program():
    exit()

window = customtkinter.CTk()
window.title("WAKE UP!")

minute=StringVar()
second=StringVar()

# Fixed Time
minute.set("10")
second.set("00")

fpack = ("Noto Sans Mandaic", 100)

canvas1 = Canvas(window, width=650, height=500, relief='raised', background="black")
canvas1.pack()

# Minute Label
# what is causing this label to span the entire screen?
# The problem was the label function, i was using the tkinters built-in instead of CTKLabel.
minutes_box = customtkinter.CTkLabel(master=window, width=0, height=0, font=fpack, fg_color="royal blue", text_color='black', textvariable=minute)
minutes_box.place(x=250, y=150, anchor="center")

# Second Label
seconds_box = customtkinter.CTkLabel(master=window, width=0, height=0, font=fpack, fg_color="royal blue", text_color='black', textvariable=second)
seconds_box.place(x=400, y=150, anchor="center")

# Image for Start button
button_photo = PhotoImage(file='/home/kenji/Desktop/WAKEUP-APP/play-icon.png')
photo_image_one = button_photo.subsample(10, 10)
# Start button
start_button = Button(master=window, text="Start", background='green', image=photo_image_one, command=start_alarm)
                        #width? #height
canvas1.create_window(250, 400, height=50, width=150, window=start_button)

# Image for Stop button
stop_photo = PhotoImage(file='/home/kenji/Desktop/WAKEUP-APP/stop-icon.png')
photo_image_two = stop_photo.subsample(17, 17)

# Stop Button   
stop_button = Button(master=window, text="Stop", background='white', image=photo_image_two, command=stop_program)
canvas1.create_window(410, 400, height=50, width=150, window=stop_button)

window.resizable(False, False)
window.mainloop()

