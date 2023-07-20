import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox
import time
import math
import enum

class page_Status(enum.Enum):
    HOME_PAGE = 0
    AUTOMATIVE_PAGE = 1
    MANUAL_PAGE = 2
    AI_PAGE = 3
class Main_UI:
    dataModel = None
    numButton = 8
    is_on = []
    on_button = []
    inputRatio = []
    outputRatio = []
    ratio_value = [0,1,2,3,4,5]
    page = page_Status.HOME_PAGE
    
    def __init__(self, data):
        self.dataModel = data
        print("Init the UI")
        
        self.window = Tk()
        # self.on = PhotoImage(file="Ni1\Utilities\Images\on_button.png")
        # self.off = PhotoImage(file="Ni1\Utilities\Images\off_button.png")
        # self.on = PhotoImage(file="Utilities\Images\on_button.png")
        # self.off = PhotoImage(file="Utilities\Images\off_button.png")

        for i in range(0, self.numButton):
            self.is_on.append(True)
            self.on_button.append(Button(self.window, bd=0, justify=RIGHT))
            # self.on_button[i].config(command=lambda:self.toggle_button_click(i))

        self.window.attributes('-fullscreen', True)
        # self.window.geometry("1024x600")
        self.window.title("Rapido Project")
        self.window.configure(bg='SlateGrey', highlightbackground='SlateGrey',
                              highlightthickness=10)

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        print("Size:", self.screen_width, self.screen_height)
        # print(self.is_on)
        # print(self.dataModel.BUTTON_STATE)
        
        self.option_frame = tk.Frame(self.window)

        self.option_frame.pack(side = 'left')
        self.option_frame.pack_propagate(False)
        self.option_frame.configure(width = self.screen_width / 5, height = self.screen_height,
                               bg = 'dark gray',
                               highlightbackground='Black',
                               highlightthickness=10)

        self.main_frame = tk.Frame(self.window)

        self.main_frame.pack(side = 'right')
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width = 4*self.screen_width / 5 - 30, height = self.screen_height,
                             bg = 'dark grey',
                             highlightbackground='Black',
                             highlightthickness=10)
        
        # Home button
        self.home_button = Button(self.option_frame, text='Home', font="Helvetica 14 bold",
                                  command=lambda: self.indicate(self.home_button,self.home_page),
                                  activebackground = 'gray',
                                  width = 15, height = 1,
                                  foreground = 'White',
                                  bg = 'MediumBlue',
                                  bd = 5)
        self.home_button.pack(side='top', pady = 20)

        # Auto button
        self.auto_button = Button(self.option_frame, text='Automative', font="Helvetica 14 bold",
                                  command=lambda: self.indicate(self.auto_button, self.automative_page),
                                  activebackground = 'gray',
                                  width = 15, height = 1,
                                  foreground = 'White',
                                  bg = 'RoyalBlue',
                                  bd = 5)
        self.auto_button.pack(side='top', pady = 20)

        # manual button
        self.manual_button = Button(self.option_frame, text='Manual', font="Helvetica 14 bold",
                                    command=lambda: self.indicate(self.manual_button, self.manual_page),
                                    activebackground = 'gray',
                                    width = 15, height = 1,
                                    foreground = 'White',
                                    bg = 'RoyalBlue',
                                    bd = 5)
        self.manual_button.pack(side='top', pady = 20)

        # AI button
        self.ai_button = Button(self.option_frame, text='AI', font="Helvetica 14 bold",
                                command=lambda: self.indicate(self.ai_button, self.ai_page),
                                activebackground = 'gray',
                                width = 15, height = 1,
                                foreground = 'White',
                                bg = 'RoyalBlue',
                                bd = 5)
        self.ai_button.pack(side='top', pady = 20)

        # Exit button
        self.exit_button = Button(self.option_frame, text='Exit', font="Helvetica 14 bold",
                                  command=self.window.destroy,
                                  activebackground = 'gray',
                                  width = 15, height = 1,
                                  foreground = 'White',
                                  bg = 'Red',
                                  bd = 5)
        self.exit_button.pack(side="bottom", pady = 20)

        # first time come to GUI
        self.indicate(self.home_button,self.home_page)
    
    def indicate(self, lb, page):
        # unHighlight buttons
        self.home_button.config(bg = 'RoyalBlue')
        self.auto_button.config(bg = 'RoyalBlue')
        self.manual_button.config(bg = 'RoyalBlue')
        self.ai_button.config(bg = 'RoyalBlue')

        # Highlight Button
        lb.config(bg = 'MediumBlue')

        # Refresh main page
        for frame in self.main_frame.winfo_children():
            frame.destroy()

        page()

    def home_page(self):
        self.page = page_Status.HOME_PAGE

        self.home_frame = tk.Frame(self.main_frame)
        self.home_lb = tk.Label(self.home_frame, text="gioi thieu\n\npage 1", font="Helvetica 12 bold")
        self.home_lb.pack()
        self.home_frame.pack()
    
    def automative_page(self):
        self.page = page_Status.AUTOMATIVE_PAGE

        self.top_manual_frame = tk.LabelFrame(self.main_frame)
        self.top_manual_frame.pack(side = 'top')
        self.top_manual_frame.pack_propagate(False)
        self.top_manual_frame.configure(width = self.main_frame.winfo_screenwidth(), 
                                    height=self.main_frame.winfo_screenheight()/3,
                                    bg='dark gray', padx= 10, pady= 10)
        
        self.bottom_manual_frame = tk.LabelFrame(self.main_frame)
        self.bottom_manual_frame.pack(side = 'top')
        self.bottom_manual_frame.pack_propagate(False)
        self.bottom_manual_frame.configure(width = self.main_frame.winfo_screenwidth(), 
                                            height=2*self.main_frame.winfo_screenheight()/3,
                                            bg='dark gray', padx= 10, pady= 20)

        self.liquidBox(self.top_manual_frame)

        self.bottom_manual_frame.rowconfigure(2, weight=4)
        # self.bottom_manual_frame.rowconfigure(1, weight=3)

        # Setting input liquid
        self.ratioLabel = tk.Label(self.bottom_manual_frame, text="Input",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.ratioLabel.grid(column=0, row=0, padx=12, pady=2, sticky=tk.NS)

        self.ratioLabel0 = tk.Label(self.bottom_manual_frame, text="Ratio",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.ratioLabel0.grid(column=0, row=1, padx=12, pady=2, sticky=tk.NS)

        self.ratioLabel1 = tk.Label(self.bottom_manual_frame, text="Liquid 1",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.ratioLabel1.grid(column=1, row=0, padx=12, pady=2, sticky=tk.NS)

        self.ratioLabel2 = tk.Label(self.bottom_manual_frame, text="Liquid 2 ",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.ratioLabel2.grid(column=2, row=0, padx=12, pady=2, sticky=tk.NS)

        self.ratioLabel3 = tk.Label(self.bottom_manual_frame, text="Liquid 3",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.ratioLabel3.grid(column=3, row=0, padx=12, pady=2, sticky=tk.NS)

        self.ratioBox1 = ttk.Combobox(self.bottom_manual_frame, values=self.ratio_value)
        self.ratioBox1.current(0)
        self.ratioBox1.grid(column=1, row=1, padx=12, pady=2, sticky=tk.NS)

        self.ratioBox2 = ttk.Combobox(self.bottom_manual_frame, values=self.ratio_value)
        self.ratioBox2.current(0)
        self.ratioBox2.grid(column=2, row=1, padx=12, pady=2, sticky=tk.NS)

        self.ratioBox3 = ttk.Combobox(self.bottom_manual_frame, values=self.ratio_value)
        self.ratioBox3.current(0)
        self.ratioBox3.grid(column=3, row=1, padx=12, pady=2, sticky=tk.NS)

        self.totalLiquid = tk.Label(self.bottom_manual_frame, text="Total liquid volume",
                               width=14, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.totalLiquid.grid(column=0, row=2, padx=12, pady=10, sticky=tk.NS, columnspan=2)
        self.totalBox = ttk.Combobox(self.bottom_manual_frame, values=[1000,2000,3000])
        self.totalBox.current(0)
        self.totalBox.grid(column=2, row=2, padx=12, pady=10, sticky=tk.NS)

        self.unitLabel = tk.Label(self.bottom_manual_frame, text="ml",
                               width=14, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.unitLabel.grid(column=3, row=2, padx=12, pady=10, sticky=tk.W)
        # Setting output liquid
        self.outputLabel = tk.Label(self.bottom_manual_frame, text="Output",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.outputLabel.grid(column=0, row=3, padx=12, pady=2, sticky=tk.NS)

        self.outputLabel0 = tk.Label(self.bottom_manual_frame, text="Ratio",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.outputLabel0.grid(column=0, row=4, padx=12, pady=2, sticky=tk.NS)

        self.outputLabel1 = tk.Label(self.bottom_manual_frame, text="Relay 1",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.outputLabel1.grid(column=1, row=3, padx=12, pady=2, sticky=tk.NS)

        self.outputLabel2 = tk.Label(self.bottom_manual_frame, text="Relay 2 ",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.outputLabel2.grid(column=2, row=3, padx=12, pady=2, sticky=tk.NS)

        self.outputLabel3 = tk.Label(self.bottom_manual_frame, text="Relay 3",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.outputLabel3.grid(column=3, row=3, padx=12, pady=2, sticky=tk.NS)

        self.outputRatioBox1 = ttk.Combobox(self.bottom_manual_frame, values=self.ratio_value)
        self.outputRatioBox1.current(0)
        self.outputRatioBox1.grid(column=1, row=4, padx=12, pady=2, sticky=tk.NS)

        self.outputRatioBox2 = ttk.Combobox(self.bottom_manual_frame, values=self.ratio_value)
        self.outputRatioBox2.current(0)
        self.outputRatioBox2.grid(column=2, row=4, padx=12, pady=2, sticky=tk.NS)

        self.outputRatioBox3 = ttk.Combobox(self.bottom_manual_frame, values=self.ratio_value)
        self.outputRatioBox3.current(0)
        self.outputRatioBox3.grid(column=3, row=4, padx=12, pady=2, sticky=tk.NS)

        self.outputEnter = tk.Button(self.bottom_manual_frame, text="Enter values",
                                     command=lambda:self.get_value(),
                                     width = 15, height = 1)
        self.outputEnter.grid(column=1, row=5, padx=12, pady=10, sticky=tk.N, columnspan=2)
    
    def manual_page(self):
        self.page = page_Status.MANUAL_PAGE

        self.top_manual_frame = tk.LabelFrame(self.main_frame)
        self.top_manual_frame.pack(side = 'top')
        self.top_manual_frame.pack_propagate(False)
        self.top_manual_frame.configure(width = self.main_frame.winfo_screenwidth(), 
                                    height=self.main_frame.winfo_screenheight()/3,
                                    bg='dark gray', padx= 10, pady= 10)
        
        self.bottom_manual_frame = tk.LabelFrame(self.main_frame)
        self.bottom_manual_frame.pack(side = 'top')
        self.bottom_manual_frame.pack_propagate(False)
        self.bottom_manual_frame.configure(width = self.main_frame.winfo_screenwidth(), 
                                            height=2*self.main_frame.winfo_screenheight()/3,
                                            bg='dark gray', padx= 10, pady= 20)

        self.liquidBox(self.top_manual_frame)

        ### Button 

        # Relay1
        self.relay1 = tk.Label(self.bottom_manual_frame, text="Relay 1",
                               width=6, height=1, bg='dark gray',
                               font="Helvetica 18 bold")
        self.relay1.grid(column=0, row=0, padx=12, pady=10, sticky=tk.NS)

        self.on_button[0] = tk.Button(self.bottom_manual_frame,text="ON",
                                       command=lambda:self.toggle_button_click(0),
                                       width=6, height=1,
                                       bg="LimeGreen", fg="White",
                                       font="Helvetica 16 bold")
        self.on_button[0].grid(column=1, row=0, padx=12, pady=10)

        # Relay2
        self.relay2 = tk.Label(self.bottom_manual_frame, text="Relay 2",
                               width=6, height=1, bg='dark gray',
                               font="Helvetica 18 bold")
        self.relay2.grid(column=2, row=0, padx=12, pady=10, sticky=tk.NS)

        self.on_button[1] = tk.Button(self.bottom_manual_frame,text="ON",
                                      command=lambda:self.toggle_button_click(1),
                                      width=6, height=1,
                                      bg="LimeGreen", fg="White",
                                      font="Helvetica 16 bold")
        self.on_button[1].grid(column=3, row=0, padx=12, pady=10)

        # Relay3
        self.relay3 = tk.Label(self.bottom_manual_frame, text="Relay 3",
                               width=6, height=1, bg='dark gray',
                               font="Helvetica 18 bold")
        self.relay3.grid(column=4, row=0, padx=12, pady=10, sticky=tk.NS)

        self.on_button[2] = tk.Button(self.bottom_manual_frame,text="ON",
                                      command=lambda:self.toggle_button_click(2),
                                      width=6, height=1,
                                      bg="LimeGreen", fg="White",
                                      font="Helvetica 16 bold")
        self.on_button[2].grid(column=5, row=0, padx=12, pady=10)
        
        # Relay4
        self.relay4 = tk.Label(self.bottom_manual_frame, text="Relay 4",
                               width=6, height=1, bg='dark gray',
                               font="Helvetica 18 bold")
        self.relay4.grid(column=0, row=1, padx=12, pady=10, sticky=tk.NS)

        self.on_button[3] = tk.Button(self.bottom_manual_frame,text="ON",
                                       command=lambda:self.toggle_button_click(3),
                                       width=6, height=1,
                                       bg="LimeGreen", fg="White",
                                       font="Helvetica 16 bold")
        self.on_button[3].grid(column=1, row=1, padx=12, pady=10)
        # Relay5
        self.relay5 = tk.Label(self.bottom_manual_frame, text="Relay 5",
                               width=6, height=1, bg='dark gray',
                               font="Helvetica 18 bold")
        self.relay5.grid(column=2, row=1, padx=12, pady=10, sticky=tk.NS)

        self.on_button[4] = tk.Button(self.bottom_manual_frame,text="ON",
                                      command=lambda:self.toggle_button_click(4),
                                      width=6, height=1,
                                      bg="LimeGreen", fg="White",
                                      font="Helvetica 16 bold")
        self.on_button[4].grid(column=3, row=1, padx=12, pady=10)

        # Relay6
        self.relay6 = tk.Label(self.bottom_manual_frame, text="Relay 6",
                               width=6, height=1, bg='dark gray',
                               font="Helvetica 18 bold")
        self.relay6.grid(column=4, row=1, padx=12, pady=10, sticky=tk.NS)

        self.on_button[5] = tk.Button(self.bottom_manual_frame,text="ON",
                                      command=lambda:self.toggle_button_click(5),
                                      width=6, height=1,
                                      bg="LimeGreen", fg="White",
                                      font="Helvetica 16 bold")
        self.on_button[5].grid(column=5, row=1, padx=12, pady=10)

        # Bump1
        self.bump1 = tk.Label(self.bottom_manual_frame, text="Bump 1",
                               width=6, height=1, bg='dark gray',
                               font="Helvetica 18 bold")
        self.bump1.grid(column=0, row=2, padx=12, pady=10, sticky=tk.NS, columnspan=2)

        self.on_button[6] = tk.Button(self.bottom_manual_frame,text="ON",
                                       command=lambda:self.toggle_button_click(6),
                                       width=6, height=1,
                                       bg="LimeGreen", fg="White",
                                       font="Helvetica 16 bold")
        self.on_button[6].grid(column=1, row=2, padx=12, pady=10, columnspan=2)

        # Bump2
        self.bump2 = tk.Label(self.bottom_manual_frame, text="Bump 2",
                               width=6, height=1, bg='dark gray',
                               font="Helvetica 18 bold")
        self.bump2.grid(column=2, row=2, padx=12, pady=20, sticky=tk.NS, columnspan=2)

        self.on_button[7] = tk.Button(self.bottom_manual_frame,text="ON",
                                      command=lambda:self.toggle_button_click(7),
                                      width=6, height=1,
                                      bg="LimeGreen", fg="White",
                                      font="Helvetica 16 bold")
        self.on_button[7].grid(column=3, row=2, padx=12, pady=10, columnspan=2)

    def ai_page(self):
        self.page = page_Status.AI_PAGE

        self.ai_frame = tk.Frame(self.main_frame)
        self.ai_lb = tk.Label(self.ai_frame, text="Upcoming", font="Helvetica 12 bold")
        self.ai_lb.pack()
        self.ai_frame.pack()
        
    def liquidBox(self, frame):
        # Liquid 1
        self.liquid1 = tk.Button(frame, text="LIQUID 1",
                                 bg="Chocolate", fg="White",
                                 font="Helvetica 16 bold")
        self.liquid1.grid(column=0, row=1, padx=60, pady=5)

        self.boxLiquid1 = tk.Label(frame, text="100%",
                                    width=6, height=1, bg="Chocolate",
                                    font="Helvetica 20 bold")
        self.boxLiquid1.grid(column=0, row=0, padx=60, pady=10, sticky=tk.NS)

        self.boxLiquid1_1 = Canvas(frame, width = 90, height=10, bg="white")
        self.boxLiquid1_1.create_rectangle(4, 52, 89, 161, fill="Chocolate")
        self.boxLiquid1_1.create_text(50,150,text="60%",font="Helvetica 14 bold")
        self.boxLiquid1_1.grid(column=0, row=0, padx=60, pady=10, sticky=tk.NS)
        
        # Liquid 2
        self.liquid2 = tk.Button(frame, text="LIQUID 2",
                                 bg="DodgerBlue", fg="White",
                                 font="Helvetica 16 bold")
        self.liquid2.grid(column=1, row=1, padx=60, pady=5)

        self.boxLiquid2 = tk.Label(frame, text="100%",
                                   width=6, height=1, bg="DodgerBlue",
                                   font="Helvetica 20 bold")
        self.boxLiquid2.grid(column=1, row=0, padx=60, pady=10, sticky=tk.NS)

        self.boxLiquid2_1 = Canvas(frame, width = 90, height=10, bg="white")
        self.boxLiquid2_1.create_rectangle(4, 52, 89, 161, fill="DodgerBlue")
        self.boxLiquid2_1.create_text(50,150,text="60%",font="Helvetica 14 bold")
        self.boxLiquid2_1.grid(column=1, row=0, padx=60, pady=10, sticky=tk.NS)

        # Liquid 3
        self.liquid3 = tk.Button(frame,text="LIQUID 3",
                                bg="Brown", fg="White",
                                font="Helvetica 16 bold")
        self.liquid3.grid(column=2, row=1, padx=60, pady=5)

        self.boxLiquid3 = tk.Label(frame, text="100%",
                               width=6, height=5, bg="Brown",
                               font="Helvetica 20 bold")
        self.boxLiquid3.grid(column=2, row=0, padx=60, pady=10, sticky=tk.NS)

        self.boxLiquid3_1 = Canvas(frame, width = 90, height=10, bg="white")
        self.boxLiquid3_1.create_rectangle(4, 52, 89, 161, fill="Brown")
        self.boxLiquid3_1.create_text(50,150,text="60%",font="Helvetica 14 bold")
        self.boxLiquid3_1.grid(column=2, row=0, padx=60, pady=10, sticky=tk.NS)

    def get_value(self):
        if int(self.ratioBox1.get()) + int(self.ratioBox2.get()) + int(self.ratioBox3.get()) != 0:
            self.inputRatio.append(self.ratioBox1.get())
            self.inputRatio.append(self.ratioBox2.get())
            self.inputRatio.append(self.ratioBox3.get())

            self.outputRatio.append(self.outputRatioBox1.get())
            self.outputRatio.append(self.outputRatioBox2.get())
            self.outputRatio.append(self.outputRatioBox3.get())
            
            if int(self.outputRatioBox1.get()) + int(self.outputRatioBox2.get()) + int(self.outputRatioBox3.get()) == 0:
                response = mbox.askquestion("Output setting", "Are you sure to not activate any relay for output?")
                if response == "yes":
                    print(self.inputRatio)
                    print(self.outputRatio)
                elif response == "no":
                    print("The user said no.")
                else:
                    print("The user canceled.")
            else:
                response = mbox.askquestion("Output setting", "Are you sure to enter these values?")
                if response == "yes":
                    print(self.inputRatio)
                    print(self.outputRatio)
                elif response == "no":
                    print("The user said no.")
                else:
                    print("The user canceled.")
        else:
            mbox.showwarning("Ratio", "Please setting ratio value!!!")

        

    def UI_Refresh(self):
        # self.UI_Set_Text(self.labelDistance1, self.dataModel.distance1_value)
        # self.UI_Set_Text(self.labelDistance2, self.dataModel.distance2_value)
        
        if self.page == page_Status.MANUAL_PAGE:
            for i in range(0, self.numButton):
                if self.dataModel.BUTTON_STATE[i] == True:
                    self.on_button[i].config(text="ON", bg="LimeGreen")
                    self.is_on[i] = True
                else:
                    self.on_button[i].config(text="OFF", bg="gold")
                    self.is_on[i] = False
        self.window.update()


    def UI_Set_Text(self,text_object, data):
        text_object.config(text="%.2f" % data)

    # define the click event of the toggle
    def toggle_button_click(self, number):
        # Determine is on or off
        if self.is_on[number]:
            self.on_button[number].config(text="OFF", bg="gold")
            self.is_on[number] = False
            # self.dataModel.relayController(number, state = 0)
            self.dataModel.BUTTON_STATE[number] = False
        else:
            self.on_button[number].config(text="ON", bg="gold")
            self.is_on[number] = True
            # self.dataModel.relayController(number, state = 1)
            self.dataModel.BUTTON_STATE[number] = True
        print("Button is" + str(number) + " clicked!!!")
        print(self.is_on[number])

    

    