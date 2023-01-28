import tkinter as tk
from tkinter import filedialog

def select_file():
    filepath = filedialog.askopenfilename()
    print(filepath)



def on_button_click():
    print(var1.get(), var2.get())

root = tk.Tk()
root.title("UI Example")

options = {"Option 1": 1, "Option 2": 2, "Option 3": 3}

root.geometry("500x300")

var1 = tk.StringVar(value="File Directory")
var2 = tk.StringVar(value="Time")

# dropdown1 = tk.OptionMenu(root, var1, *options)
# dropdown1.pack()



select_file_button = tk.Button(root, text="Select File", command=select_file)
select_file_button.grid(row=1,column=2)

# dropdown2 = tk.OptionMenu(root, var2, "Option A", "Option B", "Option C")
# dropdown2.pack()

button = tk.Button(root, text="Submit", command=on_button_click)
button.grid(row=7,column=2)

time_label = tk.Label(root, text="TIME")
time_label.grid(row=1, column=0)

hours_input = tk.Entry(root)
hours_input.grid(row=0, column=1)

hours_label = tk.Label(root, text="hours")
hours_label.grid(row=0, column=2)

minutes_input = tk.Entry(root)
minutes_input.grid(row=0, column=3)

minutes_label = tk.Label(root, text="minutes")
minutes_label.grid(row=0, column=4)

root.mainloop()
