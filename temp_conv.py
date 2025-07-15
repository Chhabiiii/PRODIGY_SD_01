import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        t = float(entry_temp.get())
        o = unit_var.get().upper()

        if o == "F":
            c = (t - 32) * (5 / 9)
            k = c + 273.15
            result.set(f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")
        elif o == "K":
            c = t - 273.15
            f = (c * 9 / 5) + 32
            result.set(f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")
        elif o == "C":
            f = (t * 9 / 5) + 32
            k = t + 273.15
            result.set(f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")
        else:
            messagebox.showerror("Invalid Unit", "Please enter F, K, or C.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric temperature value.")

root = tk.Tk()
root.title("Temperature Converter")

tk.Label(root, text="Enter Temperature Value:").grid(row=0, column=0, padx=10, pady=5)
entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Unit (F/K/C):").grid(row=1, column=0, padx=10, pady=5)
unit_var = tk.StringVar()
entry_unit = tk.Entry(root, textvariable=unit_var)
entry_unit.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Convert", command=convert_temperature).grid(row=2, columnspan=2, pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, justify="left",).grid(row=3, columnspan=2, pady=10)

root.mainloop()
    
