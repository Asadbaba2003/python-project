from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

def saveData():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saad1234",
            database="customerdata"
        )

        mycursor = conn.cursor()
        sql = "INSERT INTO studentreg (username, email, password) VALUES (%s, %s, %s)"

        # Get values from the entry widgets
        username_value = usernameEntry.get()
        email_value = emailEntry.get()
        password_value = passwordEntry.get()

        # Execute the SQL query with the values
        mycursor.execute(sql, (username_value, email_value, password_value))

        conn.commit()
        messagebox.showinfo("Success", "Data saved successfully")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()

# Create the main window
window = Tk()
window.title("Student Registration")
window.geometry("300x200")

# Set up the background image (commented out if not needed)
#background = ImageTk.PhotoImage(file='.venv/.jpg')
#blabel = Label(window, image=background)
#blabel.grid()

# Create a frame for other widgets
frame = Frame(window)
frame.place(x=50, y=50)

# Create labels and entry widgets
usernameLabel = Label(frame, text="Username", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
usernameLabel.grid(row=0, column=0, padx=10, pady=5)

usernameEntry = Entry(frame, width=30)
usernameEntry.grid(row=0, column=1)

emailLabel = Label(frame, text="Email", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
emailLabel.grid(row=1, column=0)

emailEntry = Entry(frame, width=30)
emailEntry.grid(row=1, column=1)

passwordLabel = Label(frame, text="Password", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
passwordLabel.grid(row=2, column=0, padx=10, pady=5)

passwordEntry = Entry(frame, width=30, show='*')
passwordEntry.grid(row=2, column=1)

submitButton = Button(frame, text="Submit", command=saveData)
submitButton.grid(row=3, column=0, columnspan=2)

# Start the Tkinter event loop
window.mainloop()