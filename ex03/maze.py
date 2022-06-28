import tkinter as tk
import maze_maker as mm

def key_Down(event):
    global key
    key = event.keysym

def key_Up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up" and maze_bg[my-1][mx] == 0: my -= 1
    if key == "Down" and maze_bg[my+1][mx] == 0: my += 1
    if key == "Left" and maze_bg[my][mx-1] == 0: mx -= 1
    if key == "Right" and maze_bg[my][mx+1] == 0: mx += 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    canvas.coords("tori1", cx, cy)
    maze.after(75, main_proc)

if __name__ == "__main__":
    maze = tk.Tk()
    maze.title("迷えるこうかとん")

    canvas = tk.Canvas(maze, width = 1500, height = 900, bg = "black")
    canvas.pack()

    maze_bg = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_bg)

    tori1 = tk.PhotoImage(file = "../fig/9.png")
    mx, my = 1, 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    canvas.create_image(cx, cy, image = tori1, tag = "tori1")

    key = ""
    maze.bind("<KeyPress>", key_Down)
    maze.bind("<KeyRelease>", key_Up)

    main_proc()

    maze.mainloop()