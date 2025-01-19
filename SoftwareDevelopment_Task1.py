import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Handle the conversion
def convert_temperature():
    try:
        value = float(entry_temperature.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            fahrenheit = celsius_to_fahrenheit(value)
            kelvin = celsius_to_kelvin(value)
            result.set(f"Fahrenheit: {fahrenheit:.2f} °F\nKelvin: {kelvin:.2f} K")
        
        elif unit == "Fahrenheit":
            celsius = fahrenheit_to_celsius(value)
            kelvin = fahrenheit_to_kelvin(value)
            result.set(f"Celsius: {celsius:.2f} °C\nKelvin: {kelvin:.2f} K")
        
        elif unit == "Kelvin":
            celsius = kelvin_to_celsius(value)
            fahrenheit = kelvin_to_fahrenheit(value)
            result.set(f"Celsius: {celsius:.2f} °C\nFahrenheit: {fahrenheit:.2f} °F")
        
        else:
            messagebox.showerror("Error", "Please select a valid unit.")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric temperature.")

# GUI setup
root = tk.Tk()
root.title("Temperature Converter")

# Input section
frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=0, column=0, padx=10, pady=10)

ttk.Label(frame_input, text="Temperature:").grid(row=0, column=0, padx=5, pady=5)
entry_temperature = ttk.Entry(frame_input, width=20)
entry_temperature.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_input, text="Unit:").grid(row=1, column=0, padx=5, pady=5)
combo_unit = ttk.Combobox(frame_input, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_unit.grid(row=1, column=1, padx=5, pady=5)
combo_unit.set("Select Unit")

# Convert button
button_convert = ttk.Button(frame_input, text="Convert", command=convert_temperature)
button_convert.grid(row=2, column=0, columnspan=2, pady=10)

# Output section
frame_output = ttk.Frame(root, padding="10")
frame_output.grid(row=1, column=0, padx=10, pady=10)

ttk.Label(frame_output, text="Converted Values:").grid(row=0, column=0, padx=5, pady=5)
result = tk.StringVar()
label_result = ttk.Label(frame_output, textvariable=result, background="white", relief="solid", width=40)
label_result.grid(row=1, column=0, padx=5, pady=5)

# Run the application
root.mainloop()