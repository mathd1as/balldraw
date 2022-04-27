from tkinter import *
from DataStructures.vertex import Vertex
from DataStructures.edge import Edge


window = Tk()
window.title('Computação gráfica: modelagem de cenas');

canvas = Canvas(window, width=200, height=200)
canvas.pack()

vertexA = Vertex(1, 1, 1)
vertexB = Vertex(10, 1, 10)

edge = Edge(canvas, vertexA, vertexB)
edge.createLine()

# canvas.create_rectangle(25, 25, 130, 60, fill="red")
# canvas.create_line(0, 100, 200, 100)


window.mainloop()

