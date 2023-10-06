from tkinter import filedialog
d = dict()
name = filedialog.askopenfilename(title="Choose File") #B
file = open(name, 'r', encoding='utf-8')

for line in file:
    line.strip()
    for c in line:
        c = c.lower()
        if c.isalpha():
            d[c] = d.get(c,0)+1

sorted_d = sorted(d.items())
print(sorted_d)
