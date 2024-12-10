# import tkinter as tk
# from Admin import Admin

# def login():
#     username = username_entry.get()
#     password = password_entry.get()

#     if admin.login():
#         login_window.destroy()
#         main_menu()
#     else:
#         status_label.config(text="Incorrect username or password.")

# def main_menu():
#     # Implement your main menu GUI here
#     pass

# admin = Admin('admin','123')

# # Create the login window
# login_window = tk.Tk()
# login_window.title("Login")
# login_window.geometry("300x150")

# # Username label and entry
# username_label = tk.Label(login_window, text="Username:")
# username_label.pack()
# username_entry = tk.Entry(login_window)
# username_entry.pack()

# # Password label and entry
# password_label = tk.Label(login_window, text="Password:")
# password_label.pack()
# password_entry = tk.Entry(login_window, show="*")
# password_entry.pack()

# # Login button
# login_button = tk.Button(login_window, text="Login", command=login)
# login_button.pack()

# # Status label to display login status
# status_label = tk.Label(login_window, text="")
# status_label.pack()

# # Run the login window
# login_window.mainloop()
import tkinter as tk
from Admin import Admin

def login():
    username = username_entry.get()
    password = password_entry.get()

    if admin.login():
        login_window.destroy()
        main_menu()
    else:
        status_label.config(text="Incorrect username or password.", fg="red")

def main_menu():
    # Implement your main menu GUI here
    pass

admin = Admin('admin', '123')

# Create the login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")
login_window.resizable(False, False)
login_window.configure(background="white")

# Header label
header_label = tk.Label(login_window, text="Login", font=("Arial", 16), bg="white")
header_label.pack(pady=10)

# Username label and entry
username_label = tk.Label(login_window, text="Username:", font=("Arial", 12), bg="white")
username_label.pack()
username_entry = tk.Entry(login_window, font=("Arial", 12))
username_entry.pack()

# Password label and entry
password_label = tk.Label(login_window, text="Password:", font=("Arial", 12), bg="white")
password_label.pack()
password_entry = tk.Entry(login_window, show="*", font=("Arial", 12))
password_entry.pack()

# Login button
login_button = tk.Button(login_window, text="Login", font=("Arial", 12), command=login)
login_button.pack(pady=10)

# Status label to display login status
status_label = tk.Label(login_window, text="", font=("Arial", 12), bg="white")
status_label.pack()

# Set focus to username entry field
username_entry.focus()

# Run the login window
login_window.mainloop()
