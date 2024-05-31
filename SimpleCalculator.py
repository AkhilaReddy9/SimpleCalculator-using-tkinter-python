import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("400x600")

        self.equation = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the equation
        entry = tk.Entry(self, textvariable=self.equation, font=("Arial", 20), bd=10, insertwidth=2, width=20, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Creating buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('.', 4, 0), ('0', 4, 1), ('^', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('sqrt', 5, 1), ('M+', 5, 2), ('=', 5, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == 'C':
            self.equation.set("")
        elif char == '=':
            try:
                result = str(eval(self.equation.get()))
                self.equation.set(result)
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
            except Exception:
                messagebox.showerror("Error", "Invalid input")
        elif char == 'sqrt':
            try:
                result = str(math.sqrt(float(self.equation.get())))
                self.equation.set(result)
            except Exception:
                messagebox.showerror("Error", "Invalid input")
        elif char == '^':
            self.equation.set(self.equation.get() + '**')
        elif char == 'M+':
            self.memory = self.equation.get()
        else:
            current_equation = self.equation.get()
            new_equation = current_equation + str(char)
            self.equation.set(new_equation)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
