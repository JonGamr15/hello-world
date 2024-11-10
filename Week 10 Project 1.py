import tkinter as tk
from tkinter import messagebox


def calculate_tax():
    try:
        income = float(income_entry.get())
        tax_rate = float(tax_rate_entry.get())
        tax = income * (tax_rate / 100)
        tax_result.set(f"Calculated Tax: ${tax:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for income and tax rate.")


window = tk.Tk()
window.title("Tax Calculator")


income_label = tk.Label(window, text="Income ($):")
income_label.grid(row=0, column=0, padx=10, pady=10)
income_entry = tk.Entry(window)
income_entry.grid(row=0, column=1, padx=10, pady=10)


tax_rate_label = tk.Label(window, text="Tax Rate (%):")
tax_rate_label.grid(row=1, column=0, padx=10, pady=10)
tax_rate_entry = tk.Entry(window)
tax_rate_entry.grid(row=1, column=1, padx=10, pady=10)


calculate_button = tk.Button(window, text="Calculate", command=calculate_tax)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


tax_result = tk.StringVar()
tax_result_label = tk.Label(window, textvariable=tax_result)
tax_result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


window.mainloop()
