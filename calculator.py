import tkinter as tk
import math


# Function to handle button click
def button_click(value):
    current = entry.get()  # Get the current input in the entry widget
    entry.delete(0, tk.END)  # Clear the entry widget
    entry.insert(0, current + value)  # Insert the new value


# Function to calculate the result
def calculate():
    try:
        expression = entry.get()
        # Replace '^' with '**' for exponentiation
        expression = expression.replace('^', '**')
        # Replace '√' with math.sqrt function for square root
        expression = expression.replace('√', 'math.sqrt')

        result = eval(expression)  # Use eval to evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))  # Display the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")  # Handle any error

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")  # Set the window size

# Set dark theme colors
root.configure(bg="#2c3e50")

# Create the entry widget
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="#34495e",
                 fg="#ecf0f1")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Adjust padding and make entry expand

# Create the calculator buttons with dark theme
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("√", 5, 0), ("^", 5, 1), ("(", 5, 2), (")", 5, 3)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate, bg="#3498db",
                           fg="white")
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                           command=lambda t=text: button_click(t), bg="#34495e", fg="#ecf0f1")
    button.grid(row=row, column=col, padx=5, pady=5)  # Ensure buttons have no gaps

# AC (All Clear) button
ac_button = tk.Button(root, text="AC", width=5, height=2, font=("Arial", 18), command=clear, bg="#e74c3c", fg="white")
ac_button.grid(row=6, column=3, padx=5, pady=5)
root.mainloop()
