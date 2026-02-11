import calendar
import tkinter as tk

c = calendar.TextCalendar()
m = c.formatmonth(2025, 1)

root = tk.Tk()
t = tk.Text(root, height=10, width=30)
t.insert(tk.END, m)
t.pack()
tk.mainloop()
