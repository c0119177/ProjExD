import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm

from numpy import insert

BUTTON = [
    ["%", "", "C", "←"],
    ["1/x", "x^2", "√x", "÷"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="]
    ]

SYMBOL = ["+", "-", "*", "÷"]
class Calculater(object):
    def __init__(self, calc = None):
        calc.title("calculator")

        calc_frame = ttk.Frame(calc, width = 300, height = 100)
        calc_frame.propagate(False)
        calc_frame.pack(side = tk.TOP, pady = 20)
        button_frame = ttk.Frame(calc, width = 300, height = 400)
        button_frame.propagate(False)
        button_frame.pack(side = tk.BOTTOM)

        self.calc_entry = ttk.Entry(calc_frame, font = ("Times New Roman", 40), justify = tk.RIGHT)
        self.calc_entry.pack()

        for y, row in enumerate(BUTTON, 1):
                for x, num in enumerate(row):
                    button = tk.Button(button_frame, text = num, font = ("Times New Roman", 30), width = 4, height = 1)
                    button.grid(row = y, column = x)
                    button.bind("<Button-1>", self.button_click)
                    button.bind("<Enter>", self.enter_bg)
                    button.bind("<Leave>", self.leave_bg)

    def button_click(self, event):
        click = event.widget["text"]
        if click == "=":
            if self.calc_entry in SYMBOL:
                self.calc_entry = self.calc_entry[:-1]
            res = "=" + str(eval(self.calc_entry.get()))
            self.calc_entry.delete(0, tk.END)
            self.calc_entry.insert(tk.END, res)
        elif click == "C":
            self.calc_entry.delete(0, tk.END)
        elif click == "←":
            self.calc_entry.delete(0 or len(tk.END), len(tk.END) + 1)
        elif click in SYMBOL:
            self.calc_entry.insert(tk.END, click)
        else:
            self.calc_entry.insert(tk.END, click)
#        tkm.showinfo(click, click)

    def enter_bg(self, event):
        event.widget["bg"] = "#F5F5F5"

    def leave_bg(self, event):
        event.widget["bg"] = "SystemButtonFace"

def main():
    calc = tk.Tk()
    Calculater(calc)
    calc.mainloop()

if __name__ == "__main__":
    main()