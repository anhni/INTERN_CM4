import tkinter as tk
from tkinter import *
from PIL import Image
import time
class Main_UI:
    dataModel = None

    def init_fun(self,data):
        self.dataModel = data
        print("Init the UI")
        self.is_on = True
        self.window = Tk()
        print("hehe")
        # self.logo = PhotoImage(file='bku_s.JPEG')
        # self.on = PhotoImage(file="on_button.JPEG")
        # self.off = PhotoImage(file="off_button.JPEG")

        self.window.attributes('-fullscreen', True)
        self.window.title("Rapido Project")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        # self.logo = PhotoImage(file= "Duc_Tai\\UI\\ku.png")

        self.on = PhotoImage(file="Duc_Tai\\UI\\button_on.png")
        self.off = PhotoImage(file="Duc_Tai\\UI\\button_off.png")
        print("Size:", screen_width, screen_height)

        self.on_button = Button(self.window, image=self.on, bd=0, command=self.toggle_button_click, justify=CENTER)
        # self.logo_button = Button(self.window, image = self.logo, bd=0, justify = RIGHT)

        self.labelAMONIACaption = tk.Label(text="AMONIA",
                                      fg="#0000ff",
                                      justify=CENTER,
                                      # bg = "#000",
                                      font="Helvetica 50 bold")

        self.labelAMONIACaption.place(x=0, y=0, width=screen_width / 3, height=120)

        self.labelTDSCaption = tk.Label(text="TDS",
                                   fg="#0000ff",
                                   justify=CENTER,
                                   # bg = "#000",
                                   font="Helvetica 50 bold")

        self.labelTDSCaption.place(x=screen_width / 3, y=0, width=screen_width / 3, height=120)

        self.labelPHCaption = tk.Label(text="PH",
                                  fg="#0000ff",
                                  justify=CENTER,
                                  # bg = "#000",
                                  font="Helvetica 50 bold")

        self.labelPHCaption.place(x=2 * screen_width / 3, y=0, width=screen_width / 3, height=120)

        self.labelAMONIAUnit = tk.Label(text="(PPM)",
                                   fg="#0000ff",
                                   justify=CENTER,
                                   # bg = "#000",
                                   font="Helvetica 15 bold")

        self.labelAMONIAUnit.place(x=0, y=130, width=screen_width / 3, height=50)

        self.labelTDSUnit = tk.Label(text="(NTU)",
                                fg="#0000ff",
                                justify=CENTER,
                                # bg = "#000",
                                font="Helvetica 15 bold")

        self.labelTDSUnit.place(x=screen_width / 3, y=130, width=screen_width / 3, height=50)

        self.labelPHUnit = tk.Label(text="( )",
                               fg="#0000ff",
                               justify=CENTER,
                               # bg = "#000",
                               font="Helvetica 15 bold")

        self.labelPHUnit.place(x=2 * screen_width / 3, y=130, width=screen_width / 3, height=50)

        self.labelAMONIAValue = tk.Label(text="5.12",
                                    fg="#0000ff",
                                    justify=CENTER,
                                    # bg = "#000",
                                    font="Helvetica 60 bold")

        self.labelAMONIAValue.place(x=0, y=200, width=screen_width / 3, height=100)

        self.labelTDSValue = tk.Label(text="20",
                                 fg="#0000ff",
                                 justify=CENTER,
                                 # bg = "#000",
                                 font="Helvetica 60 bold")

        self.labelTDSValue.place(x=screen_width / 3, y=200, width=screen_width / 3, height=100)

        self.labelPHValue = tk.Label(text="7.11",
                                fg="#0000ff",
                                justify=CENTER,
                                # bg = "#000",
                                font="Helvetica 60 bold")

        self.labelPHValue.place(x=2 * screen_width / 3, y=200, width=screen_width / 3, height=100)

        # define on and off stage of the toggle
        self.labelon_button = tk.Label(text="Replay",
                                fg="#0000ff",
                                justify=CENTER,
                                # bg = "#000",
                                font="Helvetica 60 bold")
        self.labelon_button.place(x=0, y=400, width=screen_width / 3, height=100)
        self.on_button.place(x=0, y=350, width=screen_width)

        self.labelDistance1 = tk.Label(text="Distance 9",
                                fg="#0000ff",
                                justify=CENTER,
                                # bg = "#000",
                                font="Helvetica 60 bold")
        self.labelDistance1.place(x=0, y=600, width=screen_width / 3, height=100)
        self.labelDistance1Value = tk.Label(text="3000",
                                           fg="#0000ff",
                                           justify=CENTER,
                                           # bg = "#000",
                                           font="Helvetica 50 bold")

        self.labelDistance1Value.place(x=600, y=600, width=screen_width / 3, height=100)

        self.labelDistance2 = tk.Label(text="Distance 12",
                                fg="#0000ff",
                                justify=CENTER,
                                # bg = "#000",
                                font="Helvetica 60 bold")
        self.labelDistance2.place(x=0, y=700, width=screen_width / 3, height=100)
        self.labelDistance2Value = tk.Label(text="3000",
                                           fg="#0000ff",
                                           justify=CENTER,
                                           # bg = "#000",
                                           font="Helvetica 50 bold")

        self.labelDistance2Value.place(x=600, y=700, width=screen_width / 3, height=100)
        # self.logo_button.place(x=screen_width - 600, y=300, width=500)
        # print("hehe")
        # self.window.update()

    # define the click event of the toggle
    def toggle_button_click(self):
        # Determine is on or off
        if self.is_on:
            self.on_button.config(image = self.off)
            self.is_on = False
            self.dataModel.setPumpOff()
            self.dataModel.BUTTON_STATE = False
        else:
            self.on_button.config(image = self.on)
            self.is_on = True
            self.dataModel.setPumpOn()
            self.dataModel.BUTTON_STATE = True
        print("Button is clicked!!!")


    def UI_Refresh(self):
        self.UI_Set_Text(self.labelDistance1Value, self.dataModel.DIS_Value[0])
        self.UI_Set_Text(self.labelDistance2Value, self.dataModel.DIS_Value[1])
        if self.dataModel.BUTTON_STATE == True:
            self.on_button.config(image = self.on)
            self.is_on = True
        else:
            self.on_button.config(image = self.off)
            self.is_on = False
        self.window.update()
 


    def UI_Set_Text(self,text_object, data):
        text_object.config(text="%.2f" % data)

# main = Main_UI()
# main.init_fun()
# main.UI_Refresh()
