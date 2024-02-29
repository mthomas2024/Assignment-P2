#Mason Thomas
#Assignment P2
#GUI Dev

import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

#Goobal holders
imageFile = None

#Create Window
root = Tk()
root.title("Payroll Every Two Weeks")
root.geometry("650x500")

#Display Instructions
title = Label(text = "Payroll Calculator")
title.place(relx=.8, rely=.1, anchor=CENTER)
subTitle = Label(text = "Payroll\n Calculation")
subTitle.place(relx=.8, rely=.4, anchor=CENTER)

#Picture Frame
pic = ttk.Frame(root, width=400,height=260)
pic.grid(column=0,row=0)
pic.configure(borderwidth="2")
pic.configure(relief="groove")


class TaxCalculatorApp:
    def __init__(self, master):
        global imageFile
        
        imageFile = "payroll.png"

        frame = pic
        img = Image.open(imageFile)
        photo = ImageTk.PhotoImage(img.resize((400,260)))
        lblImage = ttk.Label(frame, image = photo)
        lblImage.image = photo
        lblImage.place(relx=.5,rely=.5,anchor=CENTER)

        self.label_grossPay = tk.Label(master, text="Enter Gross Pay:")
        self.label_grossPay.place(relx=.3, rely=.6, anchor=CENTER)

        self.label_fica = tk.Label(master, text="FICA:")
        self.label_fica.place(relx=.3, rely=.8, anchor=CENTER)

        self.label_federal = tk.Label(master, text="Federal Tax:")
        self.label_federal.place(relx=.5, rely=.8, anchor=CENTER)

        self.label_state = tk.Label(master, text="State Tax:")
        self.label_state.place(relx=.7, rely=.8, anchor=CENTER)

        self.label_net = tk.Label(master, text="Net Paycheck Income:")
        self.label_net.place(relx=.5, rely=.9, anchor=CENTER)

        self.strIncome = tk.Entry(master)
        self.strIncome.place(relx=.7, rely=.6, anchor=CENTER)

        self.button_clear = tk.Button(master, text="Clear", command=self.clear)
        self.button_clear.place(relx=.3, rely=.7, anchor=CENTER)

        self.button_compute = tk.Button(master, text="Compute Taxes", command=self.compute_taxes)
        self.button_compute.place(relx=.5, rely=.7, anchor=CENTER)

        self.button_exit = tk.Button(master, text="Exit", command=exit)
        self.button_exit.place(relx=.7, rely=.7, anchor=CENTER)


    def clear(self):
        self.strIncome.delete(0, tk.END)
        self.label_fica.config(text="FICA:")
        self.label_federal.config(text="Federal Tax:")
        self.label_state.config(text="State Tax:")
        self.label_net.config(text="Net Paycheck Income:")

    def compute_taxes(self):
        try:
            decIncome = float(self.strIncome.get())
            decFica = decIncome * 0.0765
            decFederal = decIncome * 0.22
            decState = decIncome * 0.04
            decNet = decIncome - (decFica + decFederal + decState)

            self.label_fica.config(text="FICA: ${:.2f}".format(decFica))
            self.label_federal.config(text="Federal Tax: ${:.2f}".format(decFederal))
            self.label_state.config(text="State Tax: ${:.2f}".format(decState))
            self.label_net.config(text="Net Paycheck Income: ${:.2f}".format(decNet))
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid income.")
            


app = TaxCalculatorApp(root)
root.mainloop()
