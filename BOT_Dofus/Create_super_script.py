from tkinter import filedialog
import tkinter as tk


print(' ')
print(' ')
for i in range(4):
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    print(path)
print('final')