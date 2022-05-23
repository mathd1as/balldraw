from tkinter import *
from models.Vertex import Vertex
from models.Sphere import Sphere
from models.GeometricTransformation import GeometricTransformation as gt


window = Tk()
window.title('Computação gráfica: modelagem de cenas')

canvas = Canvas(window, width = 800, height = 600)
canvas.pack()

sphere = Sphere(100, 3, 1)

# for vertex in sphere.vertexes:
  # print(vertex.coordinatesXYZ())
  # gt.translation(vertex, Vertex(400, 300, 1))

VRP = Vertex(0, 0, 1)
focalPoint = Vertex(0, 0, 0)
viewUp = Vertex(0, 1, 0)

gt.calculateSRCVertexes(sphere.vertexes, VRP, focalPoint, viewUp)
gt.calculateSRTVertexes(sphere.vertexes, Vertex(-400, -300, 1), Vertex(400, 300, 1), Vertex(0, 0, 1), Vertex(800, 600, 1), 1)


for edge in sphere.edges:
  canvas.create_line(edge.startVertex.coordinatesXY(), edge.endVertex.coordinatesXY())
  # print(edge.startVertex.coordinates(), edge.endVertex.coordinates())

for v in sphere.vertexes:
  print(v.coordinatesXYZ())

window.mainloop()

