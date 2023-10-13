from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Weather App")
root.geometry("830x615+360+120")
root.configure(bg="#D8D6D6", border=1)
root.resizable(False, False)

# Tạo đối tượng Notebook để chứa các tab
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Tạo tab 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1)

# Tạo nội dung cho tab 1
# label1 = Label(tab1, text='This is Tab 1')
# label1.pack()

# Tạo tab 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2)

# Tạo nội dung cho tab 2
# label2 = Label(tab2, text='This is Tab 2')
# label2.pack()

root.mainloop()
