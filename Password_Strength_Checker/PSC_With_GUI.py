import re
import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_password_strength(password):
    # Define strength criteria
    criteria = {
        "length": len(password) >= 12,  # Minimum length of 12 characters
        "uppercase": bool(re.search(r"[A-Z]", password)),  # At least one uppercase letter
        "lowercase": bool(re.search(r"[a-z]", password)),  # At least one lowercase letter
        "digit": bool(re.search(r"\d", password)),  # At least one digit
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),  # At least one special character
        "common": not (password.lower() in common_passwords)  # Not a common password
    }

    # Check if all criteria are met
    if all(criteria.values()):
        return "Strong password!"
    else:
        weak_reasons = [key for key, value in criteria.items() if not value]
        return f"Weak password! Missing criteria: {', '.join(weak_reasons)}"

# List of common passwords for comparison
common_passwords = {
    "password", "123456", "123456789", "qwerty", "abc123", "letmein", "welcome"
}

# Function to evaluate the password entered by the user
def evaluate_password():
    password = password_entry.get()
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength", result)

# Set up the GUI
root = tk.Tk()
root.title("Password Strength Checker")

# Label for password entry
tk.Label(root, text="Enter your password:").pack(pady=10)

# Entry field for password input
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=10)

# Button to check password strength
check_button = tk.Button(root, text="Check Strength", command=evaluate_password)
check_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
