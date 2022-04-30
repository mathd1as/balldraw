from tkinter import *
from DataStructures.vertex import Vertex
# from DataStructures.edge import Edge
from DataStructures.sphere import Sphere
from BaseOperations.baseOperations import BaseOperation


window = Tk()
window.title('Computação gráfica: modelagem de cenas');

canvas = Canvas(window, width=800, height=600)
canvas.pack()

sphere = Sphere(100, 8, 7, canvas)

# print(sphere.Vertexes)

for vertex in sphere.Vertexes:
    BaseOperation.translation(vertex, Vertex(400, 300, 0))

for edge in sphere.Edges:
  canvas.create_line(edge.startVertex.coordinates(), edge.endVertex.coordinates())
  print(edge.startVertex.coordinates(), edge.endVertex.coordinates())

window.mainloop()

