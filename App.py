import tkinter as tk
from tkinter import colorchooser
import time

# إنشاء النافذة
root = tk.Tk()
root.title("Digital Clock Pro")
root.geometry("800x400")

# حالة الثيم
is_dark = True

# ====== Functions ======

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    root.after(200, update_time)

def change_color():
    color = colorchooser.askcolor()[1]
    if color:
        time_label.config(fg=color)
        date_label.config(fg=color)

def toggle_theme():
    global is_dark

    if is_dark:
        # Light Mode
        root.configure(bg="white")
        time_label.config(bg="white", fg="black")
        date_label.config(bg="white", fg="black")
        btn_color.config(bg="#ddd", fg="black")
        btn_theme.config(text="🌙 Dark Mode")
        is_dark = False
    else:
        # Dark Mode
        root.configure(bg="black")
        time_label.config(bg="black", fg="cyan")
        date_label.config(bg="black", fg="white")
        btn_color.config(bg="gray", fg="white")
        btn_theme.config(text="☀️ Light Mode")
        is_dark = True

# ====== UI Elements ======

time_label = tk.Label(root,font=("Orbitron", 80, "bold"))
time_label.pack(pady=20)

date_label = tk.Label(root,font=("Arial", 20))
date_label.pack()

btn_color = tk.Button(root,text="🎨 Change Color",command=change_color,font=("Arial", 14))
btn_color.pack(pady=10)

btn_theme = tk.Button(root,text="☀️ Light Mode",command=toggle_theme,font=("Arial", 14))
btn_theme.pack(pady=10)

# تشغيل الساعة
toggle_theme()  # يبدأ بـ Dark Mode
update_time()

# تشغيل البرنامج
root.mainloop()