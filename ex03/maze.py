import tkinter as tk
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
    global cx, cy, mx, my, roop
    if key == "Up" and maze_bg[my-1][mx] == 0: my -= 1
    if key == "Down" and maze_bg[my+1][mx] == 0: my += 1
    if key == "Left" and maze_bg[my][mx-1] == 0: mx -= 1
    if key == "Right" and maze_bg[my][mx+1] == 0: mx += 1
    cx, cy = mx * 50 + 25, my * 50 + 25
    canvas.coords("tori1", cx, cy)
    if cx == 1375 and cy ==775:
        maze.after_cancel(roop)
        roop = None
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

    tori = Image.open("../fig/0.png").resize((25, 25))
    tori = ImageTk.PhotoImage(tori)
    mx, my = 1, 1
    cx, cy = mx * 50 + 25, my * 50 + 25
    canvas.create_image(cx, cy, image = tori, tag = "tori1")

    key = ""
    maze.bind("<KeyPress>", key_Down)
    maze.bind("<KeyRelease>", key_Up)

    main_proc()

    maze.mainloop()