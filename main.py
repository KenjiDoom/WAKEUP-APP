import customtkinter
from tkinter import *
import pygame, sys, os, time

pygame.mixer.init()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("650x500")
        self.title("Coding Timer")
        
        # variables for minute and seconds
        self.minute=StringVar()
        self.second=StringVar()

        self.minute.set("10")
        self.second.set("10")
        
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
        self.start_button = Button(master=self, text="Start", background='white', image=self.photo_image_one) # Dont foget the command for function
        self.start_button.place(x=250, y=400, height=50, width=150)

        # Image for Stop button
        self.stop_photo = PhotoImage(file='/home/kenji/Desktop/WAKEUP-APP/affects/stop-icon.png')
        self.photo_image_two = self.stop_photo.subsample(17, 17)

        # Stop Button   
        self.stop_button = Button(master=self, text="Stop", background='white', image=self.photo_image_two)
        self.stop_button.place(x=410, y=400, height=50, width=150)
app = App()
app.configure(fg_color='black')
app.resizable(False, False)
app.mainloop()