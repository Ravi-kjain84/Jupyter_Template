#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:48:21 2020

@author: arnav
"""

import tkinter as tk
import tkinter.font as font


class main_frames(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("1500x1200")
        
        self.title("Add New Section")

        self.top_frame = tk.LabelFrame(self,width = 100, height = 200, bg="khaki1")
        #self.top_frame.pack(side = "top", fill = "x")
        self.top_frame.place(relheight = 0.2,relwidth = 1,rely = 0,relx=0)
        
        self.bottom_frame = tk.LabelFrame(self,width = 100, height = 200, bg="khaki1")
        #self.bottom_frame.pack(side = "bottom", fill = "x")
        self.bottom_frame.place(relheight = 0.2,relwidth = 1,rely = 0.8,relx=0)

        self.left_frame = tk.LabelFrame(self,width = 300, height = 800, bg="khaki1")
        #self.left_frame.pack(side = "left", fill = "y")
        self.left_frame.place(relheight = 0.6,relwidth = 0.2,rely = 0.2,relx=0)
        
        self.right_frame = tk.LabelFrame(self,width = 300, height = 800, bg="khaki1")
        #self.right_frame.pack(side = "right", fill = "y")
        self.right_frame.place(relheight = 0.6,relwidth = 0.2,rely = 0.2,relx=0.8)

        self.center_frame = tk.LabelFrame(self,width = 900, height = 800, bg="khaki1")
        #self.center_frame.pack(side = "top", fill = "both")
        self.center_frame.place(relheight = 0.6,relwidth = 0.6,rely = 0.2,relx=0.2)
        
        
        self.input  = 9
        self.output = 10
        self.repair = 10


class user_interact_frames(main_frames):
    def __init__(self):
        super().__init__()

        self.user_interfaces(self.input,self.left_frame, "input_output")
        self.user_interfaces(self.output,self.right_frame, "input_output")
        self.user_interfaces(self.repair,self.center_frame, "repair")

        for i in range(0, self.repair):
            self.f = tk.LabelFrame(self.center_frame, width = 225, height = 125, bg = 'lightblue')
            #self.f.place(relheight = 0.2,relwidth = 0.2,rely = 0.4,relx = 0.2*i)

        for i in range(0, self.output):
            self.f = tk.LabelFrame(self.right_frame, width = 300, height = 125, bg = 'lightblue')
            #self.f.place(relheight = 0.2,relwidth = 1,rely = 0.2*i)
            
            
    def user_interfaces(self,frame_count, base_frame, type = "input_output"):

        for i in range(0, self.input):

            frac = 1/frame_count
            self.f = tk.LabelFrame(base_frame, width = 300, height = 125, bg = 'lightblue')

            if type == "input_output":
                self.f.place(relheight = frac,relwidth = 1,rely = frac*i,relx=0)
            else:
                self.f.place(relheight = 0.2,relwidth = frac,relx = frac*i,rely=0.5)
            
            if self.input > 5:
                frame_font = font.Font(size = 17 - self.input)
            else:
                frame_font = font.Font(size=12)


            self.wb = tk.Label(self.f,text = "Workbook : ", font = frame_font, bg = 'lightblue')
            self.wb.place(relx = 0.05, rely = 0.2)
            
            self.ws = tk.Label(self.f,text = "Worksheet : ", font = frame_font, bg = 'lightblue')
            self.ws.place(relx = 0.05, rely = 0.7)
                
            self.btn = tk.Button(self.f, text = 'Browse', font = frame_font, bg = 'lightblue')
            self.btn.place(relheight = 0.2, relwidth = 0.25, relx = 0.45, rely = 0.15)

            self.entry = tk.Entry(self.f, width = 50, font = frame_font, bg = 'lightgrey')
            self.entry.place(relheight = 0.2, relwidth = 0.25, relx = 0.45, rely = 0.7)
        

if __name__ == "__main__":
    root = user_interact_frames()
    root.mainloop()
