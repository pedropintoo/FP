# Exercise 5 on "How to think like a computer scientist", ch. 11.
from tkinter import filedialog
import turtle


t = turtle.Turtle()

with open(filedialog.askopenfilename(title="Choose File"),"r") as file:
    file = file.readlines()
    for line in file:
        if "UP" in line:
            t.up()
        elif "DOWN" in line:
            t.down()
        else:
            c = line.split()
            t.goto(int(c[0]),int(c[1]))
# Use t.up(), t.down() and t.goto(x, y)
# Put your code here


# wait
turtle.Screen().exitonclick()

