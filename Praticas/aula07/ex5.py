from tkinter import filedialog

name = filedialog.askopenfilename(title="Choose File") #B
file = open(name, 'r', encoding='utf-8')


