import tkinter as tk
from tkinter import *
from PIL import Image
import time
class IotGateway_UI:
    dataModel = None
    def __init__(self,data):
        self.dataModel = data
        print("Init the UI!!")
        self.is_on = True
        self.window = tk.Tk()
        self.on = PhotoImage(file="on1.png")
        self.off = PhotoImage(file="off1.png")

        self.window.attributes('-fullscreen', True)
        self.window.title("IotGateway UI")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        print("Size = ", screen_width, screen_height)

        self.button = Button(self.window, image=self.on, bd=0, command=self.toggle_button_click)
        self.button.place(x=screen_width/2, y=0)

        self.Relay = Label(self.window, text="RELAY",fg="#0000ff", font= "Helvetica 50 bold")
        self.Relay.place(x=0, y=0, width=screen_width/2, height=100)

        self.labelDistance1 = tk.Label(text="Distance",
                                        fg="#0000ff",
                                        justify=CENTER,
                                        # bg = "#000",
                                        font="Helvetica 50 bold")

        self.labelDistance1.place(x=0, y=110, width=screen_width / 3, height=100)

        self.labelDistance1Unit = tk.Label(text="mm",
                                       fg="#0000ff",
                                       justify=CENTER,
                                       # bg = "#000",
                                       font="Helvetica 30 bold")

        self.labelDistance1Unit.place(x=screen_width / 3, y=110, width=screen_width / 3, height=100)

        self.labelDistance1Value = tk.Label(text="3000",
                                           fg="#0000ff",
                                           justify=CENTER,
                                           # bg = "#000",
                                           font="Helvetica 50 bold")

        self.labelDistance1Value.place(x=2 * screen_width / 3, y=110, width=screen_width / 3, height=100)



    def toggle_button_click(self):
        print("Button is clicked!!")
        if self.is_on:
            self.button.configure(image=self.off)
            self.is_on = False
            # gửi lệnh tắt relay
            self.dataModel.setPumpOn()
        else:
            self.button.configure(image=self.on)
            self.is_on = True
            # gửi lệnh bật relay
            self.dataModel.setPumpOff()

    def UI_Refresh(self):
        self.UI_Set_Text(self.labelDistance1Value, self.dataModel.DIS_Value)
        if self.dataModel.BUTTON_STATE == True:
            self.button.config(image = self.on)
            self.is_on = True
        else:
            self.button.config(image = self.off)
            self.is_on = False
        self.window.update()

    def UI_Set_Text(self, text_object, data):
        text_object.config(text="%.2f" % data)
