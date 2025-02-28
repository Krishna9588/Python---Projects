import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x400")
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display area
        result_entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        result_entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/', '4', '5', '6', '*',
            '1', '2', '3', '-', '0', '.', '=', '+' ]

        row, col = 1, 0
        for button in buttons:
            if button == "=":
                tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18), command=self.calculate).grid(row=row, column=col, columnspan=2, sticky="nsew")
                col += 2
            else:
                tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda button=button: self.on_button_click(button)).grid(row=row, column=col)
                col += 1
                if col > 3:
                    col = 0
                    row += 1

    def on_button_click(self, char):
        current_text = self.result_var.get()
        self.result_var.set(current_text + str(char))

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
