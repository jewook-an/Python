import tkinter as tk

# tkinter 참고 : https://wikidocs.net/132610
s = "Life is short\nUse Python"

root = tk.Tk()
t = tk.Text(root, height=2, width=13)
t.insert(tk.END, s)
t.pack()
tk.mainloop()
