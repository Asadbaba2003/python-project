from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector


def save_data():
    try:
        # Establish database connection
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password='asad23',
            database="customerdata"
        )

        # Create a cursor
        my_cur = conn.cursor()

        # Validate input data
        if not username_entry.get() or not email_entry.get() or not password_entry.get():
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Insert data into the database
        query = "INSERT INTO studentreg (username, email, password) VALUES (%s, %s, %s);"
        data = (username_entry.get(), email_entry.get(), password_entry.get())
        my_cur.execute(query, data)

        # Commit changes and close connection
        conn.commit()
        conn.close()

        # Clear entry fields after successful data entry
        username_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)

        messagebox.showinfo("Success", "Data saved successfully!")

    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error connecting to the database: {e}")


# Create main window
window = Tk()
window.title("User Registration")

# Set background image
background = ImageTk.PhotoImage(file='download.jpeg')
b_label = Label(window, image=background)
b_label.grid()

# Create a frame
frame = Frame(window)
frame.place(x=600, y=100)

# Labels and Entry widgets
username_label = Label(frame, text="Username", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
username_label.grid(row=0, column=0, padx=10, pady=5)

username_entry = Entry(frame, width=30)
username_entry.grid(row=0, column=1)

email_label = Label(frame, text="Email", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
email_label.grid(row=1, column=0)
email_entry = Entry(frame, width=30)
email_entry.grid(row=1, column=1)

password_label = Label(frame, text="Password", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
password_label.grid(row=2, column=0, padx=10, pady=5)
password_entry = Entry(frame, width=30, show='')  # Show '' for password
password_entry.grid(row=2, column=1)

# Button to save data
save_button = Button(frame, text="Save Data", command=save_data)
save_button.grid(row=3, columnspan=2, pady=10)

# Run the main loop
window.mainloop()