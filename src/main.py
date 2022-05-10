from tkinter import *
from models.Vertex import Vertex
from models.Sphere import Sphere
from models.GeometricTransformation import GeometricTransformation


window = Tk()
window.title('Computação gráfica: modelagem de cenas')

canvas = Canvas(window, width = 800, height = 600)
canvas.pack()

sphere = Sphere(100, 8, 7)

# for vertex in sphere.vertexes:
#     GeometricTransformation.translation(vertex, Vertex(400, 300, 1))

VRP = Vertex(0, 0, 400)
focalPoint = Vertex(0, 0, 0)
viewUp = Vertex(0, 1, 0)

for edge in sphere.edges:
  canvas.create_line(edge.startVertex.coordinates(), edge.endVertex.coordinates())
  # print(edge.startVertex.coordinates(), edge.endVertex.coordinates())

window.mainloop()

