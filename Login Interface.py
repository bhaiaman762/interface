import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Animated Login Interface")
root.geometry("400x300")
root.config(bg="#1e1e2f")

# Global variables for animation
text_opacity = 0
animation_direction = 1

# Function to animate welcome text
def animate_text():
    global text_opacity, animation_direction
    # Reverse direction if needed
    if text_opacity >= 1:
        animation_direction = -0.05
    elif text_opacity <= 0:
        animation_direction = 0.05
    text_opacity += animation_direction

    # Set new color based on opacity
    hex_opacity = hex(int(text_opacity * 255))[2:].zfill(2)
    welcome_label.config(fg=f"#ffffff{hex_opacity}")
    root.after(50, animate_text)

# Function to handle login logic
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome back, admin!")
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

# Welcome label
welcome_label = tk.Label(root, text="Welcome to BioSmart City",
                         font=("Helvetica", 16, "bold"),
                         fg="#ffffff", bg="#1e1e2f")
welcome_label.pack(pady=20)

# Username field
tk.Label(root, text="Username", fg="white", bg="#1e1e2f").pack()
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

# Password field
tk.Label(root, text="Password", fg="white", bg="#1e1e2f").pack()
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=login, bg="#00adb5", fg="white", width=15)
login_button.pack(pady=20)

# Start animation
animate_text()

# Run the GUI loop
root.mainloop()
