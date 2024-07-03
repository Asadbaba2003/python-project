import tkinter as tk


def draw_point(canvas, point, color="black", size=2):
    x, y = point
    canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline=color)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Draw Point Example")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    draw_point(canvas, (100, 100), color="red", size=5)

    root.mainloop()
