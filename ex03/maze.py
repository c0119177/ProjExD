import tkinter as tk

from matplotlib import image
import maze_maker as mm
from PIL import Image, ImageTk
import tkinter.messagebox as tkm

roop = None

def key_Down(event):
    global key
    key = event.keysym

def key_Up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my, roop, tori
    if key == "Up" and maze_bg[my-1][mx] == 0:
        my -= 1
        canvas.itemconfig(i, image = tori[3])
    if key == "Down" and maze_bg[my+1][mx] == 0:
        my += 1
        canvas.itemconfig(i, image = tori[2])
    if key == "Left" and maze_bg[my][mx-1] == 0:
        mx -= 1
        canvas.itemconfig(i, image = tori[0])
    if key == "Right" and maze_bg[my][mx+1] == 0:
        mx += 1
        canvas.itemconfig(i, image = tori[1])
    cx, cy = mx * 50 + 25, my * 50 + 25
    canvas.coords("tori0", cx, cy)
    if cx == 1375 and cy ==775:
        maze.after_cancel(roop)
        roop = None
        canvas.itemconfig(i, image = tori[4])
        tkm.showinfo("ゴールしました", "Congratulations‼")
        return
    roop = maze.after(75, main_proc)

if __name__ == "__main__":
    maze = tk.Tk()
    maze.title("迷えるこうかとん")

    canvas = tk.Canvas(maze, width = 1450, height = 900, bg = "black")
    canvas.pack()

    maze_bg = mm.make_maze(29, 17)
    mm.show_maze(canvas, maze_bg)

    canvas.create_rectangle(50, 50, 100, 100, fill="orange")
    canvas.create_rectangle(1350, 750, 1400, 800, fill="blue")

    tori = []
    tori0 = Image.open("../fig/0.png").resize((25, 25))
    tori1 = Image.open("../fig/2.png").resize((25, 25))
    tori2 = Image.open("../fig/3.png").resize((25, 25))
    tori3 = Image.open("../fig/6.png").resize((25, 25))
    tori4 = Image.open("../fig/9.png").resize((25, 25))
    tori.append(ImageTk.PhotoImage(tori0))
    tori.append(ImageTk.PhotoImage(tori1))
    tori.append(ImageTk.PhotoImage(tori2))
    tori.append(ImageTk.PhotoImage(tori3))
    tori.append(ImageTk.PhotoImage(tori4))
    
    mx, my = 1, 1
    cx, cy = mx * 50 + 25, my * 50 + 25
    i = canvas.create_image(cx, cy, image = tori[0], tag = "tori0")

    key = ""
    maze.bind("<KeyPress>", key_Down)
    maze.bind("<KeyRelease>", key_Up)

    main_proc()

    maze.mainloop()