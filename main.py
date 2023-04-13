from PIL import ImageTk, Image
from tkinter import messagebox
from CTkMessagebox import CTkMessagebox
import time, sys, os, pygame, customtkinter
from threading import *
from tkinter import *
 
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
pygame.mixer.init()


def threading(button_press):
    #    I attempted to multi-thread, but I'm still not knowledgeable enough on the topic.
    if button_press == 'start':
        t1 = Thread(target=start_alarm())
        t1.start()
    elif button_press == 'stop':
        t2 = Thread(target=stop_program())
        t2.start()
    elif button_press == 'play_sound':
        t3 = Thread(target=play_sound())
        t3.start()

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
        # It has to do with time.sleep() according to the docs, time.sleep() pauses the entire program before allowing you do to anything else
        # Hence the multi-thread, but I didn't implement it correctly.
        time.sleep(1)

        if (total_time == 0):
            print("Function is running...")
            threading('play_sound')

        total_time -= 1

def play_sound():
    pygame.mixer.music.load('/home/kenji/Desktop/WAKEUP-APP/affects/alarm-affect.wav')
    pygame.mixer.music.play(loops=0)
    result = messagebox.askyesno('Timer is up!', "The program is done counting, would you like to exit?", icon='warning')

    if result == True:
        exit()
    elif result == False:
        pass

def stop_program():
    exit()

window = customtkinter.CTk()
window.title("Coding Timer")

minute=StringVar()
second=StringVar()

# Fixed Time
minute.set("00")
second.set("04")

fpack = ("Noto Sans Mandaic bold", 80)

canvas1 = Canvas(window, width=650, height=500, relief='raised', background="black")
canvas1.pack()

# Blue background frame to solve (blue span on labels)
frame = customtkinter.CTkFrame(master=window, fg_color='royal blue', width=300, height=124).place(x=320, y=150, anchor='center')

# Minute Label
minutes_box = customtkinter.CTkLabel(window, font=fpack, fg_color="royal blue", textvariable=minute)
minutes_box.place(x=250, y=150, anchor="center")

semi_coloan = customtkinter.CTkLabel(master=frame, text=':', font=('Noto Sans Mandaic bold', 80), fg_color='royal blue', width=20, height=50).place(x=329, y=146, anchor='center')

# Second Label
seconds_box = customtkinter.CTkLabel(master=window, width=0, height=0, font=fpack, fg_color="royal blue", textvariable=second)
seconds_box.place(x=400, y=150, anchor="center")

# Image for Start button
button_photo = PhotoImage(file='/home/kenji/Desktop/WAKEUP-APP/affects/play-icon.png')
photo_image_one = button_photo.subsample(10, 10)
# Start button
start_button = Button(master=window, text="Start", background='white', image=photo_image_one, command=lambda m='start': threading(m))
                        #width? #height
canvas1.create_window(250, 400, height=50, width=150, window=start_button)

# Image for Stop button
stop_photo = PhotoImage(file='/home/kenji/Desktop/WAKEUP-APP/affects/stop-icon.png')
photo_image_two = stop_photo.subsample(17, 17)

# Stop Button   
stop_button = Button(master=window, text="Stop", background='white', image=photo_image_two, command=lambda m='stop': threading(m))
canvas1.create_window(410, 400, height=50, width=150, window=stop_button)


if __name__ == "__main__":
    window.resizable(False, False)
    window.mainloop()

