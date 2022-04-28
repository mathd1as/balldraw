from tkinter import *
from DataStructures.vertex import Vertex
from DataStructures.edge import Edge


window = Tk()
window.title('Computação gráfica: modelagem de cenas');

canvas = Canvas(window, width=200, height=200)
canvas.pack()

vertexA = Vertex(1, 1, 1)
vertexB = Vertex(100, 100, 10)

# edge = Edge(canvas, vertexA, vertexB)

# canvas.create_rectangle(25, 25, 130, 60)
canvas.create_line(vertexA.x, vertexA.y, vertexB.x, vertexB.y)


window.mainloop()

