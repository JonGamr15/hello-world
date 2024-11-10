import tkinter as tk
from tkinter import messagebox

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5 / 9
        celsius_var.set(f"{celsius:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for Fahrenheit.")

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9 / 5) + 32
        fahrenheit_var.set(f"{fahrenheit:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for Celsius.")

window = tk.Tk()
window.title("Temperature Converter")


fahrenheit_var = tk.StringVar(value="32.0")
celsius_var = tk.StringVar(value="0.0")


fahrenheit_label = tk.Label(window, text="Fahrenheit:")
fahrenheit_label.grid(row=0, column=0, padx=10, pady=5)
celsius_label = tk.Label(window, text="Celsius:")
celsius_label.grid(row=0, column=1, padx=10, pady=5)

fahrenheit_entry = tk.Entry(window, textvariable=fahrenheit_var)
fahrenheit_entry.grid(row=1, column=0, padx=10, pady=5)
celsius_entry = tk.Entry(window, textvariable=celsius_var)
celsius_entry.grid(row=1, column=1, padx=10, pady=5)


to_celsius_button = tk.Button(window, text=">>>>", command=fahrenheit_to_celsius)
to_celsius_button.grid(row=2, column=0, padx=10, pady=10)

to_fahrenheit_button = tk.Button(window, text="<<<<", command=celsius_to_fahrenheit)
to_fahrenheit_button.grid(row=2, column=1, padx=10, pady=10)


window.mainloop()
