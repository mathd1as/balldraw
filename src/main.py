from tkinter import *

window = Tk()
window.title('Computação gráfica: modelagem de cenas');

canvas = Canvas(window, width=200, height=200)
canvas.pack()

canvas.create_rectangle(25, 25, 130, 60, fill="red")
canvas.create_line(0, 100, 200, 50)


window.mainloop()