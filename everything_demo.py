import tkinter as tk
#backward code
def open_second_page():
    input_value = input_entry.get()
    second_page(input_value)

def second_page(input_value):
    second_window = tk.Toplevel(window)
    second_label = tk.Label(second_window, text=f"Input value from first page: {input_value}")
    second_label.pack()

# Create the main Tkinter window
window = tk.Tk()

# First Page
input_entry = tk.Entry(window)
input_entry.pack()
open_button = tk.Button(window, text="Open Second Page", command=open_second_page)
open_button.pack()

# Start the Tkinter event loop
window.mainloop()
