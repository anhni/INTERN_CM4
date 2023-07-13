import tkinter as tk
from tkinter import *
import time
class Main_UI:
    dataModel = None
    numButton = 6
    is_on = []
    on_button = []
    
    def __init__(self, data):
        self.dataModel = data
        print("Init the UI")
        
        self.window = Tk()
        self.on = PhotoImage(file="Ni1\Utilities\Images\on_button.png")
        self.off = PhotoImage(file="Ni1\Utilities\Images\off_button.png")
        # self.logo = PhotoImage(file="Utilities\Images\on_button.png")

        for i in range(0, self.numButton):
            self.is_on.append(True)
            self.on_button.append(Button(self.window, image=self.on, bd=0, justify=RIGHT))

        self.window.attributes('-fullscreen', True)
        self.window.title("Rapido Project")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        print("Size:", screen_width, screen_height)
        # print(self.is_on)
        # print(self.dataModel.BUTTON_STATE)
        
        # relay1
        self.relay1 = tk.Label(text="RELAY 1",
                                      fg="#0000ff",
                                      justify=RIGHT,
                                      # bg = "#000",
                                      font="Helvetica 20 bold")

        self.relay1.place(x=0, y=30, width=screen_width / 3, height=120)
        # self.on_button[0] = Button(self.window, image=self.on, bd=0, command=self.toggle_button_click(0), justify=RIGHT)
        self.on_button[0].config(command=self.toggle_button_click_0)
        self.on_button[0].place(x=400, y=30, width=200, height = 120)

        # relay2
        self.relay2 = tk.Label(text="RELAY 2",
                                      fg="#0000ff",
                                      justify=RIGHT,
                                      # bg = "#000",
                                      font="Helvetica 20 bold")

        self.relay2.place(x=0, y=200, width=screen_width / 3, height=120)
        # self.on_button[1] = Button(self.window, image=self.on, bd=0, command=self.toggle_button_click(1), justify=RIGHT)
        self.on_button[1].config(command=self.toggle_button_click_1)
        self.on_button[1].place(x=400, y=200, width=200, height = 120)

    def UI_Refresh(self):
        # self.UI_Set_Text(self.labelPHValue, self.dataModel.PH_Value)
        # self.UI_Set_Text(self.labelTDSValue, self.dataModel.TSS_Value)
        # self.UI_Set_Text(self.labelAMONIAValue, self.dataModel.NH3_Value)
        # self.UI_Set_Text(self.labelPHValue, 0)
        # self.UI_Set_Text(self.labelTDSValue, 0)
        # self.UI_Set_Text(self.labelAMONIAValue, 0)
        for i in range(0, self.numButton):
            if self.dataModel.BUTTON_STATE[i] == True:
                self.on_button[i].config(image = self.on)
                self.is_on[i] = True
            else:
                self.on_button[i].config(image = self.off)
                self.is_on[i] = False
        self.window.update()


    def UI_Set_Text(self,text_object, data):
        text_object.config(text="%.2f" % data)

    # define the click event of the toggle
    def toggle_button_click_0(self):
        # Determine is on or off
        if self.is_on[0]:
            self.on_button[0].config(image = self.off)
            self.is_on[0] = False
            # self.dataModel.setPumpOff()
            self.dataModel.relayController(1, 0)
            self.dataModel.BUTTON_STATE[0] = False
        else:
            self.on_button[0].config(image = self.on)
            self.is_on[0] = True
            # self.dataModel.setPumpOn()
            self.dataModel.relayController(1, 1)
            self.dataModel.BUTTON_STATE[0] = True
        print("Button is clicked!!!")
        print(self.is_on[0])
    
    # define the click event of the toggle
    def toggle_button_click_1(self):
        # Determine is on or off
        if self.is_on[1]:
            self.on_button[1].config(image = self.off)
            self.is_on[1] = False
            # self.dataModel.setPumpOff()
            self.dataModel.relayController(2, 0)
            self.dataModel.BUTTON_STATE[1] = False
        else:
            self.on_button[1].config(image = self.on)
            self.is_on[1] = True
            # self.dataModel.setPumpOn()
            self.dataModel.relayController(2, 1)
            self.dataModel.BUTTON_STATE[1] = True
        print("Button is clicked!!!")
        print(self.is_on[1])
    
    # define the click event of the toggle
    def toggle_button_click_2(self):
        # Determine is on or off
        if self.is_on[2]:
            self.on_button[2].config(image = self.off)
            self.is_on[2] = False
            # self.dataModel.setPumpOff()
            self.dataModel.BUTTON_STATE[2] = False
        else:
            self.on_button[2].config(image = self.on)
            self.is_on[2] = True
            # self.dataModel.setPumpOn()
            self.dataModel.BUTTON_STATE[2] = True
        print("Button is clicked!!!")
        print(self.is_on[2])
    

    