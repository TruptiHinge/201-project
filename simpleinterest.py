
import tkinter as tk
from tkinter import Label, Entry, Button, LabelFrame

def calculate_interest():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    result = round((p * r * t) / 100, 2)
    result_label.config(text="The interest is: $" + str(result))

root = tk.Tk()
root.geometry("400x300")
root.title("Interest Calculator")

root.config(bg="#F0F0F0")

heading_label = Label(root, text="Interest Calculator", font=("Arial", 16))
heading_label.place(x=120, y=10)

principal_label = Label(root, text="Principal:")
principal_label.place(x=40, y=60)

principal_entry = Entry(root)
principal_entry.place(x=120, y=60)

rate_label = Label(root, text="Rate of Interest:")
rate_label.place(x=40, y=100)

rate_entry = Entry(root)
rate_entry.place(x=160, y=100)

time_label = Label(root, text="Time:")
time_label.place(x=40, y=140)

time_entry = Entry(root)
time_entry.place(x=120, y=140)

calculate_button = Button(root, text="Calculate", command=calculate_interest)
calculate_button.place(x=150, y=180)

result_frame = LabelFrame(root, text="Result", padx=10, pady=10)
result_frame.place(x=100, y=220)

result_label = Label(result_frame, text="[]")
result_label.pack()


root.mainloop()
