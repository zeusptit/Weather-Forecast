import tkinter as tk
from tkinter import ttk

def toggle_details():
    global expanded  # Khai báo biến expanded như là biến toàn cục
    if not expanded:
        expand_button.config(text="▲")
        info_label.config(text="Thông tin cơ bản\nChi tiết 1\nChi tiết 2\nChi tiết 3")
    else:
        expand_button.config(text="▼")
        info_label.config(text="Thông tin cơ bản")
    expanded = not expanded

root = tk.Tk()
root.title("Expandable Box Example")
root.geometry("400x100")

# Tạo frame chứa thông tin ban đầu
info_frame = ttk.Frame(root)
info_frame.pack(fill='both', expand=True)

info_label = tk.Label(info_frame, text="Thông tin cơ bản")
info_label.pack()

# Tạo nút mở rộng
expand_button = tk.Button(info_frame, text="▼", command=toggle_details)
expand_button.pack()

expanded = False  # Khai báo biến expanded

root.mainloop()
