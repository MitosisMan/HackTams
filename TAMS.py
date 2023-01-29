import tkinter as tk
from tkinter import filedialog

def select_file():
    filepath = filedialog.askdirectory()
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

time_label = tk.Label(root, text="Select Directory")
time_label.grid(row=0, column=0)

select_file_button = tk.Button(root, text="Select File", command=select_file)
select_file_button.grid(row=0,column=1)

time_label = tk.Label(root, text="Time")
time_label.grid(row=1, column=0)

yearsInput = tk.Entry(root)
yearsInput.grid(row=1, column=1)

yearsLabel = tk.Label(root, text="years")
yearsLabel.grid(row=1, column=2)

monthsInput = tk.Entry(root)
monthsInput.grid(row=2, column=1)

monthsLabel = tk.Label(root, text="months")
monthsLabel.grid(row=2, column=2)

weeksInput = tk.Entry(root)
weeksInput.grid(row=3, column=1)

weeksLabel = tk.Label(root, text="weeks")
weeksLabel.grid(row=3, column=2)

daysInput = tk.Entry(root)
daysInput.grid(row=4, column=1)

daysLabel = tk.Label(root, text="days")
daysLabel.grid(row=4, column=2)

hoursInput = tk.Entry(root)
hoursInput.grid(row=5, column=1)

hoursLabel = tk.Label(root, text="hours")
hoursLabel.grid(row=5, column=2)

minutesInput = tk.Entry(root)
minutesInput.grid(row=6, column=1)

minutesLabel = tk.Label(root, text="minutes")
minutesLabel.grid(row=6, column=2)

button = tk.Button(root, text="Submit", command=on_button_click)
button.grid(row=7,column=2)

# dropdown2 = tk.OptionMenu(root, var2, "Option A", "Option B", "Option C")
# dropdown2.pack()







# hours_label = tk.Label(root, text="hours")
# hours_label.grid(row=0, column=2)

# minutes_input = tk.Entry(root)
# minutes_input.grid(row=0, column=3)

# minutes_label = tk.Label(root, text="minutes")
# minutes_label.grid(row=0, column=4)

root.mainloop()
