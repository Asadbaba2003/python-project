import tkinter as tk

def create_gradient(canvas, color1, color2, width, height):
    steps = 100
    for i in range(steps):
        ratio = i / steps
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_rectangle(0, i * (height / steps), width, (i + 1) * (height / steps), outline="", fill=color)

root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)

sky_blue = (135, 206, 235)
black = (0, 0, 0)

create_gradient(canvas, sky_blue, black, 400, 300)

frame = tk.Frame(root, bg='white', padx=10, pady=10)
frame.place(relx=0.5, rely=0.5, anchor='center')

name_label = tk.Label(frame, text="Name", bg='white')
name_label.grid(row=0, column=0, pady=(0, 5), sticky='e')
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, pady=(0, 5))

roll_label = tk.Label(frame, text="Roll No", bg='white')
roll_label.grid(row=1, column=0, pady=(0, 5), sticky='e')
roll_entry = tk.Entry(frame)
roll_entry.grid(row=1, column=1, pady=(0, 5))

dept_label = tk.Label(frame, text="Department", bg='white')
dept_label.grid(row=2, column=0, pady=(0, 5), sticky='e')
dept_entry = tk.Entry(frame)
dept_entry.grid(row=2, column=1, pady=(0, 5))

submit_button = tk.Button(frame, text="Submit")
submit_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

root.mainloop()