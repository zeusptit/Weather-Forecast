import tkinter as tk
from tkinter import ttk

def show_tab(tab_index):
    notebook.select(tab_index)

root = tk.Tk()
root.title("Hide Tab Bar and Use Buttons Example")
root.geometry("400x300")

# Tạo Notebook và ẩn thanh chuyển tab
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Tạo và thêm các tab vào Notebook
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

# Tạo nút (button) để chuyển đến tab 1
button_tab1 = tk.Button(root, text="Tab 1", command=lambda: show_tab(0))
button_tab1.pack(side='left')

# Tạo nút (button) để chuyển đến tab 2
button_tab2 = tk.Button(root, text="Tab 2", command=lambda: show_tab(1))
button_tab2.pack(side='left')

root.mainloop()
