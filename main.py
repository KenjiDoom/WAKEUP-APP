from tkinter import messagebox
from tkinter import *
import customtkinter
import pygame, sys, os, time

pygame.mixer.init()

flag = True

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("650x500")
        self.title("Coding Timer")
        
        # variables for minute and seconds
        self.minute=StringVar()
        self.second=StringVar()

        # Fixed time
        self.minute.set("00")
        self.second.set("05")
        
        # Fonts
        font_pack = ("Noto Sans Mandaic bold", 80)

        # Frame
        self.frame = customtkinter.CTkFrame(master=self, fg_color='royal blue', width=300, height=124).place(x=320, y=150, anchor='center')

        # Semi Colan for frame
        self.semi_coloan = customtkinter.CTkLabel(master=self.frame, text=':', font=font_pack, fg_color='royal blue', width=20, height=50).place(x=329, y=146, anchor='center')
        
        # Minute Label
        self.minutes_box = customtkinter.CTkLabel(master=self, font=font_pack, fg_color="royal blue", textvariable=self.minute)
        self.minutes_box.place(x=250, y=150, anchor="center")

        # Second Label
        self.seconds_box = customtkinter.CTkLabel(master=self, width=0, height=0, font=font_pack, fg_color="royal blue", textvariable=self.second)
        self.seconds_box.place(x=400, y=150, anchor="center")

        # Image for Start button
        self.button_photo = PhotoImage(file='/home/kenji/Desktop/WAKEUP-APP/affects/play-icon.png')
        self.photo_image_one = self.button_photo.subsample(10, 10) # Resizing image
        # Start button
        self.start_button = Button(master=self, text="Start", background='white', image=self.photo_image_one, command=self.start_timer) # Dont foget the command for function
        self.start_button.place(x=150, y=310, height=50, width=150)

        # Image for Stop button
        self.stop_photo = PhotoImage(file='/home/kenji/Desktop/WAKEUP-APP/affects/stop-icon.png')
        self.photo_image_two = self.stop_photo.subsample(17, 17)
        # Stop Button   
        self.stop_button = Button(master=self, text="Stop", background='white', image=self.photo_image_two, command=self.pause_timer)
        self.stop_button.place(x=340, y=310, height=50, width=150)


    def starting_alarm_display(self):
        global flag
        total_time = int(self.minute.get()) * 60 + int(self.second.get())
        while total_time >- 1 and not flag:
            mins, secs = divmod(total_time, 60)
            if mins > 60:
                mins = divmod(mins, 60)
            
            self.minute.set("{0:2d}".format(mins))
            self.second.set("{0:2d}".format(secs))
            self.update()
            
            print('App running')
            self.after(1000)
            total_time -= 1
            if (total_time == 0):
                print('Playing sound....')
                self.play_sound()

    def start_timer(self):
        global flag
        flag = False
        self.starting_alarm_display()
    
    def pause_timer(self):
        print('The app has been pasued')
        global flag
        flag = True

    def play_sound(self):
        pygame.mixer.music.load('/home/kenji/Desktop/WAKEUP-APP/affects/alarm-affect.wav')
        pygame.mixer.music.play(loops=0)
        result = messagebox.askyesno('Timer is up!', "The program is done counting, would you like to exit?", icon='warning')
        if result == True:
            exit()
        elif result == False:
            pygame.mixer.music.stop()

    
    def window_close_event(self):
        result = messagebox.askyesno('Quit', 'Do you want to quit?')

        if result == True:
            self.destroy()
            exit()
        elif result == False:
            print('Resuiming Process')


app = App()
app.configure(fg_color='black')
app.resizable(False, False)
app.protocol("WM_DELETE_WINDOW", app.window_close_event)
app.mainloop()