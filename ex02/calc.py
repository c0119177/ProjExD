import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm

from numpy import insert

BUTTON = [
    ["9", "8", "7"],
    ["6", "5", "4"],
    ["3", "2", "1"],
    ['0']
    ]
class Calculater(object):
    def __init__(self, calc = None):
        calc.title("calculator")

        calc_frame = ttk.Frame(calc, width=300, height=50)
        calc_frame.propagate(False)
        calc_frame.pack(side=tk.TOP, pady=20)
        button_frame = ttk.Frame(calc, width=300, height=400)
        button_frame.propagate(False)
        button_frame.pack(side=tk.BOTTOM)

        self.calc_entry = tk.Entry(calc_frame, font=("Times New Roman",20))
        self.calc_entry.pack(anchor=tk.E)

        for y, row in enumerate(BUTTON, 1):
                for x, num in enumerate(row):
                    button = tk.Button(button_frame, text = num, font = ("Times New Roman", 30), width = 4, height = 2)
                    button.grid(row = y, column = x)
                    button.bind("<Button-1>", self.button_click)
                    button.bind("<Enter>", self.enter_bg)
                    button.bind("<Leave>", self.leave_bg)

    def button_click(self, event):
        click = event.widget["text"]
        self.calc_entry.insert(tk.END, click)
#        tkm.showinfo(click, click)

    def enter_bg(self,event):
        enter = event.widget["bg"] = "#F5F5F5"
    def leave_bg(self,event):
        leave = event.widget["bg"] = "SystemButtonFace"

def main():
    calc = tk.Tk()
    calc.resizable(width=False, height=False)
    Calculater(calc)
    calc.mainloop()

if __name__ == "__main__":
    main()