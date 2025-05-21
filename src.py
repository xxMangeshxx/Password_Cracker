import itertools
import time
import string
import tkinter as tk
from tkinter import ttk

def bruteforce_attack(password):
    chars = string.printable.strip()
    attempts = 0
    for length in range(1, len(password) + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return (attempts, guess)
    return (attempts, None)

def on_submit():
    password = password_entry.get()
    start = time.time()
    attempts, guess = bruteforce_attack(password)
    end = time.time()
    
    if guess:
        result_message = f"Password cracked in {attempts} attempts.\nYour password is: {password}\nTime elapsed: {end - start:.2f} seconds."
    else:
        result_message = f"Password not cracked after {attempts} attempts.\nTime elapsed: {end - start:.2f} seconds."
    
    attempts_label.config(text=f"Attempts: {attempts}")
    time_label.config(text=f"Time Elapsed: {end - start:.2f} seconds")
    result_label.config(text=result_message)
    show_results()

def show_results():
    for widget in root.winfo_children():
        widget.pack_forget()
    
    results_frame.pack(fill="both", expand=True)

def show_welcome():
    for widget in root.winfo_children():
        widget.pack_forget()
    
    welcome_frame.pack(fill="both", expand=True)

# Create the main window
root = tk.Tk()
root.title("Password Cracker")
root.geometry("800x600")

# Style configuration
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 16), padding=10)
style.configure("TLabel", font=("Helvetica", 16), padding=10)

# Welcome Frame
welcome_frame = tk.Frame(root)
welcome_label = tk.Label(welcome_frame, text="Welcome to the Password Cracker", font=("Helvetica", 24))
welcome_label.pack(pady=20)

password_label = tk.Label(welcome_frame, text="Enter Password:", font=("Helvetica", 18))
password_label.pack(pady=10)
password_entry = tk.Entry(welcome_frame, show="*", font=("Helvetica", 18), width=30)
password_entry.pack(pady=10)

submit_button = ttk.Button(welcome_frame, text="Crack Password", command=on_submit)
submit_button.pack(pady=20)

# Results Frame
results_frame = tk.Frame(root)
result_label = tk.Label(results_frame, text="", font=("Helvetica", 18))
result_label.pack(pady=20)

attempts_label = tk.Label(results_frame, text="", font=("Helvetica", 18))
attempts_label.pack(pady=10)

time_label = tk.Label(results_frame, text="", font=("Helvetica", 18))
time_label.pack(pady=10)

back_button = ttk.Button(results_frame, text="Back to Welcome", command=show_welcome)
back_button.pack(pady=20)

# Show the welcome frame initially
show_welcome()

# Run the application
root.mainloop()
