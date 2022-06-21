import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm

BUTTON = [
    ["9", "8", "7"],
    ["6", "5", "4"],
    ["3", "2", "1"],
    ['0']
    ]
class Calculater(object):
    def __init__(self, calc = None):
        
        self.calc_str = "0"

        calc.title("calculator")
        calc.geometry("300x600")

        calc_frame = ttk.Frame(calc, width=300, height=50) # 計算式と結果用のFrame
        calc_frame.propagate(False) # サイズが固定される
        calc_frame.pack(side=tk.TOP, pady=20) # 余白の設定
        button_frame = ttk.Frame(calc, width=300, height=400) # 計算ボタン用のFrame
        button_frame.propagate(False) # サイズが固定される
        button_frame.pack(side=tk.BOTTOM)

        self.calc_var = tk.StringVar()
#        calc_label = tk.Label(calc_frame, textvariable=self.calc_var, font=("Times New Roman",20))
#        calc_label.pack(anchor=tk.E)
        calc_ent = ttk.Entry(calc_frame, textvariable = self.calc_var, font=("Times New Roman",40))
        calc_ent.pack(anchor = tk.E)

        for y, row in enumerate(BUTTON, 1):
                for x, num in enumerate(row):
                    button = tk.Button(button_frame, text = num, font = ("Times New Roman", 30), width = 4, height = 2)
                    button.grid(row = y, column = x)
                    button.bind("<Button-1>", self.button_click)

    def button_click(self, event):
        click = event.widget["text"]
        self.calc_var += click
        self.calc_var.set(click)
#        tkm.showinfo(click, click)


def main():
    calc = tk.Tk()
    calc.resizable(width=False, height=False)
    Calculater(calc)
    calc.mainloop()

if __name__ == "__main__":
    main()