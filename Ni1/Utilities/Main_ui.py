import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox
from PIL import ImageTk, Image
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
    inputRatio = [0,0,0]
    outputRatio = [0,0,0]
    ratio_value = [0,1,2,3,4,5]
    max_liquid_box = 5
    min_liquid_box = 160
    # Ex change ratio 24000ml ~ 100%
    exchange_ratio = 24000/100
    # Time exchange 200ml/1000ms => 5ms/1ml
    time_exchange = 5
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

        # self.window.attributes('-fullscreen', True)
        self.window.geometry("1024x600")
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
        self.main_frame.configure(width = 4*self.screen_width / 5, height = self.screen_height,
                             bg = 'dark grey',
                             highlightbackground='Black',
                             highlightthickness=10)
        
        # Home button
        self.home_button = Button(self.option_frame, text='Home', font="Helvetica 14 bold",
                                  command=lambda: self.indicate(self.home_button,self.home_page),
                                  activebackground = 'gray',
                                  width = 12, height = 1,
                                  foreground = 'White',
                                  bg = 'MediumBlue',
                                  bd = 5)
        self.home_button.pack(side='top', pady = 20)

        # Auto button
        self.auto_button = Button(self.option_frame, text='Automative', font="Helvetica 14 bold",
                                  command=lambda: self.indicate(self.auto_button, self.automative_page),
                                  activebackground = 'gray',
                                  width = 12, height = 1,
                                  foreground = 'White',
                                  bg = 'RoyalBlue',
                                  bd = 5)
        self.auto_button.pack(side='top', pady = 20)

        # manual button
        self.manual_button = Button(self.option_frame, text='Manual', font="Helvetica 14 bold",
                                    command=lambda: self.indicate(self.manual_button, self.manual_page),
                                    activebackground = 'gray',
                                    width = 12, height = 1,
                                    foreground = 'White',
                                    bg = 'RoyalBlue',
                                    bd = 5)
        self.manual_button.pack(side='top', pady = 20)

        # AI button
        self.ai_button = Button(self.option_frame, text='AI', font="Helvetica 14 bold",
                                command=lambda: self.indicate(self.ai_button, self.ai_page),
                                activebackground = 'gray',
                                width = 12, height = 1,
                                foreground = 'White',
                                bg = 'RoyalBlue',
                                bd = 5)
        self.ai_button.pack(side='top', pady = 20)

        # Exit button
        self.exit_button = Button(self.option_frame, text='Exit', font="Helvetica 14 bold",
                                  command=self.window.destroy,
                                  activebackground = 'gray',
                                  width = 12, height = 1,
                                  foreground = 'White',
                                  bg = 'Red',
                                  bd = 5)
        self.exit_button.pack(side="bottom", pady = 20)

        # first time come to GUI
        self.indicate(self.home_button,self.home_page)
        # self.dataModel.getDistanceAll()
    
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
        # self.home_lb = tk.Label(self.home_frame, text="Home", font="Helvetica 12 bold")
        # self.home_lb.pack()

        # self.system_img = PhotoImage(file="Ni1\\Utilities\\Images\\system.jpg")
        self.system_img = ImageTk.PhotoImage(file='Ni1\\Utilities\\Images\\system (2).jpg')

        self.home_top = tk.Frame(self.home_frame)
        self.home_top.pack(side="left")
        self.home_top.pack_propagate(False)
        self.home_top.configure(width=int(self.main_frame.winfo_screenwidth()/4), 
                                    height=int(self.main_frame.winfo_screenheight()),
                                    )
        
        # self.home_bottom = tk.Frame(self.home_frame)
        # self.home_bottom.pack(side="left")
        # self.home_bottom.pack_propagate(False)
        # self.home_bottom.configure(width=int(self.main_frame.winfo_screenwidth()/4), 
        #                             height=int(self.main_frame.winfo_screenheight()),
        #                             )
        
        self.home_text1 = tk.Label(self.home_top, text="Project la mot he thong\n duoc thiet ke de phan phoi nuoc\n cho cay trong \n",
                                   width=50, bg='dark gray',
                                   font="Helvetica 12 bold")
        self.home_text1.grid(column=0, row=0, padx=12, pady=2, sticky=tk.W)
        # self.home_text1 = tk.Label(self.home_top, text="Project la mot he thong\n duoc thiet ke de phan phoi nuoc\n cho cay trong \n",
        #                            width=30, bg='dark gray',
        #                            font="Helvetica 12 bold")
        # self.home_text1.grid(column=0, row=1, padx=12, pady=2, sticky=tk.W)
        self.home_text2 = tk.Label(self.home_top,
                                   width=500, image= self.system_img,  bg='dark gray',
                                   font="Helvetica 12 bold")
        self.home_text2.grid(column=0, row=1, padx=12, pady=2, sticky=tk.W)
        # self.home_text1 = tk.Label(self.main_frame, text="Project la mot he thong\n duoc thiet ke de phan phoi nuoc\n cho cay trong \n",
        #                            width=30, height=20, bg='dark gray',
        #                            font="Helvetica 12 bold")
        # self.home_text1.grid(column=0, row=0, padx=12, pady=2, sticky=tk.W)

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
                               width=18, height=1, bg='dark gray',
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

        self.outputLabel1 = tk.Label(self.bottom_manual_frame, text="Relay 4",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.outputLabel1.grid(column=1, row=3, padx=12, pady=2, sticky=tk.NS)

        self.outputLabel2 = tk.Label(self.bottom_manual_frame, text="Relay 5 ",
                               width=10, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.outputLabel2.grid(column=2, row=3, padx=12, pady=2, sticky=tk.NS)

        self.outputLabel3 = tk.Label(self.bottom_manual_frame, text="Relay 6",
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

        self.totalLiquid1 = tk.Label(self.bottom_manual_frame, text="Side liquid volume",
                               width=18, height=1, bg='dark gray',
                               font="Helvetica 12 bold")
        self.totalLiquid1.grid(column=0, row=5, padx=12, pady=10, sticky=tk.NS, columnspan=2)
        self.totalBox1 = ttk.Combobox(self.bottom_manual_frame, values=[10000,20000,30000])
        self.totalBox1.current(0)
        self.totalBox1.grid(column=2, row=5, padx=12, pady=10, sticky=tk.NS)

        self.outputEnter = tk.Button(self.bottom_manual_frame, text="Enter values",
                                     command=lambda:self.get_value(),
                                     width = 15, height = 1)
        self.outputEnter.grid(column=3, row=5, padx=12, pady=10, sticky=tk.N)
    
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
        # self.boxLiquid1_1.create_rectangle(3, 72, 89, 161, fill="Chocolate")
        # self.boxLiquid1_1.create_text(50,120,text="30%",font="Helvetica 14 bold")
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
        # self.boxLiquid2_1.create_rectangle(3, 92, 89, 161, fill="DodgerBlue")
        # self.boxLiquid2_1.create_text(50,120,text="60%",font="Helvetica 14 bold")
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
        # self.boxLiquid3_1.create_rectangle(4, 82, 89, 161, fill="Brown")
        # self.boxLiquid3_1.create_text(50,120,text="60%",font="Helvetica 14 bold")
        self.boxLiquid3_1.grid(column=2, row=0, padx=60, pady=10, sticky=tk.NS)

    def get_value(self):
        self.sensorValueConvert()
        
        temp = int(self.ratioBox1.get()) + int(self.ratioBox2.get()) + int(self.ratioBox3.get())       
        
        if int(self.totalBox.get()) >= 0 and int(self.totalBox1.get()) >= 0:
            if temp != 0: 
                if self.input_check():
                    self.output_check()                           
            else:
                response = mbox.askquestion("Ratio", "Are you sure not to activate any relay for input?")
                if response == "yes":
                    self.output_check()
                elif response == "no":
                    print("The user said no.")
                else:
                    print("The user canceled.")        
        else:
            mbox.showwarning("Ratio", "Please setting total luiquid value!!!")

        # else:
        #     mbox.showwarning("Ratio", "Please setting ratio value!!!")
    
    def input_check(self):
        temp = int(self.ratioBox1.get()) + int(self.ratioBox2.get()) + int(self.ratioBox3.get())
        return_value = 1 
        if int(self.totalBox.get())*int(self.ratioBox1.get())/temp > self.liquid1Percent*self.exchange_ratio:
            mbox.showwarning("Ratio", "Luiquid 1 is not enough!!! Please re-setting luiquid 1 ratio value!!!")
            return_value = 0 
        if int(self.totalBox.get())*int(self.ratioBox2.get())/temp > self.liquid2Percent*self.exchange_ratio:
            mbox.showwarning("Ratio", "Luiquid 2 is not enough!!! Please re-setting luiquid 2 ratio value!!!")
            return_value = 0 
        if int(self.totalBox.get())*int(self.ratioBox3.get())/temp > self.liquid3Percent*self.exchange_ratio:
            mbox.showwarning("Ratio", "Luiquid 3 is not enough!!! Please re-setting luiquid 3 ratio value!!!") 
            return_value = 0 
        
        return return_value

    def output_check(self):
        if int(self.outputRatioBox1.get()) + int(self.outputRatioBox2.get()) + int(self.outputRatioBox3.get()) == 0:
            response = mbox.askquestion("Output setting", "Are you sure not to activate any relay for output?")
            if response == "yes":
                self.update_timer()
            elif response == "no":
                print("The user said no.")
            else:
                print("The user canceled.")
        else:
            response = mbox.askquestion("Output setting", "Are you sure to enter these values?")
            if response == "yes":
                self.update_timer()
            elif response == "no":
                print("The user said no.")
            else:
                print("The user canceled.")
    
    def update_timer(self):
        # self.inputRatio[0] = int(self.ratioBox1.get())
        # self.inputRatio[1] = int(self.ratioBox2.get())
        # self.inputRatio[2] = int(self.ratioBox3.get())

        # self.outputRatio[0] = int(self.outputRatioBox1.get())
        # self.outputRatio[1] = int(self.outputRatioBox2.get())
        # self.outputRatio[2] = int(self.outputRatioBox3.get())
        temp = int(self.ratioBox1.get()) + int(self.ratioBox2.get()) + int(self.ratioBox3.get())
        if temp != 0:
            self.dataModel.PUMP_ON_DELAY[0] = round(int(self.ratioBox1.get())*int(self.totalBox.get())*self.time_exchange/temp)
            self.dataModel.PUMP_ON_DELAY[1] = round(int(self.ratioBox2.get())*int(self.totalBox.get())*self.time_exchange/temp)
            self.dataModel.PUMP_ON_DELAY[2] = round(int(self.ratioBox3.get())*int(self.totalBox.get())*self.time_exchange/temp)
        else:
            self.dataModel.PUMP_ON_DELAY[0] = 0
            self.dataModel.PUMP_ON_DELAY[1] = 0
            self.dataModel.PUMP_ON_DELAY[2] = 0
        
        temp = int(self.outputRatioBox1.get()) + int(self.outputRatioBox2.get()) + int(self.outputRatioBox3.get())
        if temp != 0:
            self.dataModel.PUMP_ON_DELAY[3] = round(int(self.outputRatioBox1.get())*(int(self.totalBox.get())+int(self.totalBox1.get()))*self.time_exchange/temp)
            self.dataModel.PUMP_ON_DELAY[4] = round(int(self.outputRatioBox2.get())*(int(self.totalBox.get())+int(self.totalBox1.get()))*self.time_exchange/temp)
            self.dataModel.PUMP_ON_DELAY[5] = round(int(self.outputRatioBox3.get())*(int(self.totalBox.get())+int(self.totalBox1.get()))*self.time_exchange/temp)
        else:
            self.dataModel.PUMP_ON_DELAY[3] = 0
            self.dataModel.PUMP_ON_DELAY[4] = 0
            self.dataModel.PUMP_ON_DELAY[5] = 0
        
        print(self.dataModel.PUMP_ON_DELAY)
    
    def UI_Refresh(self):
        # Liquid box
        if self.page == page_Status.MANUAL_PAGE or self.page == page_Status.AUTOMATIVE_PAGE:
            self.sensorValueConvert()
            self.boxLiquid1_1.create_rectangle(3, self.liquid1BoxRatio, 89, 161, fill="Chocolate")
            self.boxLiquid1_1.create_text(50,120,text=str(self.liquid1Percent) + "%",font="Helvetica 14 bold")

            self.boxLiquid2_1.create_rectangle(3, self.liquid2BoxRatio, 89, 161, fill="DodgerBlue")
            self.boxLiquid2_1.create_text(50,120,text=str(self.liquid2Percent) + "%",font="Helvetica 14 bold")

            self.boxLiquid3_1.create_rectangle(3, self.liquid3BoxRatio, 89, 161, fill="Brown")
            self.boxLiquid3_1.create_text(50,120,text=str(self.liquid3Percent) + "%",font="Helvetica 14 bold")
        
        # Button config
        if self.page == page_Status.MANUAL_PAGE:
            for i in range(0, self.numButton):
                if self.dataModel.BUTTON_STATE[i] == True:
                    self.on_button[i].config(text="ON", bg="LimeGreen")
                    self.is_on[i] = True
                else:
                    self.on_button[i].config(text="OFF", bg="gold")
                    self.is_on[i] = False
        
        self.window.update()

    def sensorValueConvert(self):
        self.liquid1Percent = math.floor((self.dataModel.distanceMax_value - self.dataModel.distance1_value)*100/self.dataModel.distanceMax_value)
        self.liquid2Percent = math.floor((self.dataModel.distanceMax_value - self.dataModel.distance2_value)*100/self.dataModel.distanceMax_value)
        self.liquid3Percent = math.floor((self.dataModel.distanceMax_value - self.dataModel.distance3_value)*100/self.dataModel.distanceMax_value)

        self.liquid1BoxRatio = self.min_liquid_box - (self.liquid1Percent*(self.min_liquid_box - self.max_liquid_box))/100
        self.liquid2BoxRatio = self.min_liquid_box - (self.liquid2Percent*(self.min_liquid_box - self.max_liquid_box))/100
        self.liquid3BoxRatio = self.min_liquid_box - (self.liquid3Percent*(self.min_liquid_box - self.max_liquid_box))/100

    def UI_Set_Text(self,text_object, data):
        text_object.config(text="%.2f" % data)

    # define the click event of the toggle
    def toggle_button_click(self, number):
        # Determine is on or off
        if self.is_on[number]:
            self.on_button[number].config(text="OFF", bg="gold")
            self.is_on[number] = False
            self.dataModel.relayController(number, state = 0)
            self.dataModel.BUTTON_STATE[number] = False
        else:
            self.on_button[number].config(text="ON", bg="LimeGreen")
            self.is_on[number] = True
            self.dataModel.relayController(number, state = 1)
            self.dataModel.BUTTON_STATE[number] = True
        print("Button is" + str(number) + " clicked!!!")
        print(self.is_on[number])

    

    