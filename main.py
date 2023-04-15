import customtkinter
from tkinter import *

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

app = App()
app.configure(fg_color='black')
app.resizable(False, False)
app.mainloop()