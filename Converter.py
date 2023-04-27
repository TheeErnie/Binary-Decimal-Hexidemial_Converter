import tkinter
from tkinter import *
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Unit Converter")
        self.geometry('{}x{}'.format(450, 250))
        self.resizable(width=False, height=False)

        #make grid
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.bind_class('Entry', '<Return>', self.button_callback)

        #input
        self.input_frame = customtkinter.CTkFrame(self)
        self.input_frame.grid(row=0, column=0, pady=8, sticky="s")
        self.input_frame.grid_columnconfigure(0, weight=3)
        self.input_frame.grid_columnconfigure(1, weight=1)

        self.button = customtkinter.CTkButton(master=self.input_frame, text="Convert", command=self.button_callback, width=60)
        self.button.grid(row=0, column=1, padx=8)
        self.entry = customtkinter.CTkEntry(master=self.input_frame)
       # self.entry.bind('<Return>', self.button_callback)
        self.entry.grid(row=0, column=0, padx=8, pady=8)


        #output
        self.converted_frame = customtkinter.CTkFrame(self)
        self.converted_frame.grid(row=1, column=0, padx=8, pady=8, sticky="n")
        self.converted_frame.grid_columnconfigure((0, 1), weight=1)
        
        self.conversion_fmt = customtkinter.CTkLabel(master=self.converted_frame, text="Converted Equivalent: ")
        self.conversion_fmt.grid(column=0, row=0, padx=8)
        self.conversion_val = customtkinter.CTkLabel(master=self.converted_frame, text="0000")
        self.conversion_val.place(relx=.5, rely=.5)
        self.conversion_val.grid(column=1, row=0, padx=8)


        #radio buttons
        self.rb1frame = customtkinter.CTkFrame(self)
        self.rb1frame.grid(row=0, column=1, rowspan=2, padx=8)
        self.radb_var = tkinter.IntVar(value=0)
        self.radb1 = customtkinter.CTkRadioButton(master=self.rb1frame, text="Decimal to Binary", variable= self.radb_var, value = 0)
        self.radb2 = customtkinter.CTkRadioButton(master=self.rb1frame, text="Binary to Decimal", variable= self.radb_var, value = 1)
        self.radb3 = customtkinter.CTkRadioButton(master=self.rb1frame, text="Decimal to Hexadecimal", variable= self.radb_var, value = 2)
        self.radb4 = customtkinter.CTkRadioButton(master=self.rb1frame, text="Hexadecimal to Decimal", variable= self.radb_var, value = 3)
        self.radb5 = customtkinter.CTkRadioButton(master=self.rb1frame, text="Binary to Hexadecimal", variable= self.radb_var, value = 4)
        self.radb6 = customtkinter.CTkRadioButton(master=self.rb1frame, text="Hexadecimal to Binary", variable= self.radb_var, value = 5)
        self.radb1.grid(row=0,column=1, pady=8, padx=8, sticky="w")
        self.radb2.grid(row=1,column=1, pady=8, padx=8, sticky="w")
        self.radb3.grid(row=2,column=1, pady=8, padx=8, sticky="w")
        self.radb4.grid(row=3,column=1, pady=8, padx=8, sticky="w")
        self.radb5.grid(row=4,column=1, pady=8, padx=8, sticky="w")
        self.radb6.grid(row=5,column=1, pady=8, padx=8, sticky="w")

    def dec2bi(self, userinput):
        if userinput == 0:
            tmpstr = '0'
        tmpstr = ''
        while userinput >= 1:
            if userinput % 2 == 0:
                tmpstr = '0' + tmpstr
            else :
                tmpstr = '1' + tmpstr
            userinput = userinput // 2
        return tmpstr        

    def bi2dec(self, userinput):
        tmpint = 0
        exponent = 0
        while userinput >= 1:
            if userinput % 10 == 1:
                tmpint = tmpint + pow(2, exponent)
            exponent = exponent + 1
            userinput = userinput // 10
        tmpstr = str(tmpint)

        return tmpstr

    def dec2hex(self, userinput):
        if userinput == 0:
            return '0'
        
        tmpstr = ''
        while(userinput >= 1):
            if(userinput % 16 < 10):
                tmpstr = str(userinput % 16) + tmpstr
            elif userinput % 16 == 10:
                tmpstr = 'A' + tmpstr
            elif userinput % 16 == 11:
                tmpstr = 'B' + tmpstr
            elif userinput % 16 == 12:
                tmpstr = 'C' + tmpstr
            elif userinput % 16 == 13:
                tmpstr = 'D' + tmpstr
            elif userinput % 16 == 14:
                tmpstr = 'E' + tmpstr
            elif userinput % 16 == 15:
                tmpstr = 'F' + tmpstr

            userinput = userinput // 16

        return tmpstr
    
    def hex2dec(self, userinput):
        if userinput == '0' or userinput == '00' or userinput == '000' or userinput == '0000':
            return userinput
        tmpint = 0
        exponent = 0
        userinput = userinput[::-1]
        for char in range(0, len(userinput)):
            multiplier = 0
            if userinput[char] == 'A' or userinput[char] == 'a':
                multiplier = 10
            elif userinput[char] == 'B' or userinput[char] == 'b':
                multiplier = 11
            elif userinput[char] == 'C' or userinput[char] == 'c':
                multiplier = 12
            elif userinput[char] == 'D' or userinput[char] == 'd':
                multiplier = 13
            elif userinput[char] == 'E' or userinput[char] == 'e':
                multiplier = 14
            elif userinput[char] == 'F' or userinput[char] == 'f':
                multiplier = 15
            else:
                multiplier = int(userinput[char])

            tmpint = tmpint + (multiplier * pow(16, exponent))
            exponent = exponent + 1

        return str(tmpint)


    def bi2hex(self, userinput):
        result = self.bi2dec(userinput)
        return self.dec2hex(int(result))

    def hex2bi(self, userinput):
        result = self.hex2dec(userinput)
        return self.dec2bi(int(result))

    def button_callback(self, event=None):
        whichbutton = self.radb_var.get()
        if whichbutton == 0: # dec2bi conversion
            result = self.dec2bi(int(self.entry.get()))
        elif whichbutton == 1:
            result = self.bi2dec(int(self.entry.get()))
        elif whichbutton == 2:
            result = self.dec2hex(int(self.entry.get()))
        elif whichbutton == 3:
            result = self.hex2dec(self.entry.get())
        elif whichbutton == 4:
            result = self.bi2hex(int(self.entry.get()))
        elif whichbutton == 5:
            result = self.hex2bi(self.entry.get())
        
        self.conversion_val.configure(text=result)



if __name__ == "__main__":
    app = App()
    app.mainloop()
