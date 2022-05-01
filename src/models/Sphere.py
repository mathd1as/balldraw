from .Vertex import Vertex
from .Edge import Edge
from .GeometricTransformation import GeometricTransformation
class Sphere:
  def __init__(self, radius, meridians, parallels, canvas):    
    self.canvas = canvas

    self.meridians = meridians
    self.parallels = parallels
    self.radius = radius
    self.Edges = []
    self.Vertexes = []

    self.shapeSphere()

  def shapeSphere(self):
    self.meridianAngle = 360 / self.meridians
    self.parallelAngle = 180 / (self.parallels + 1)

    startVertex = Vertex(0, 0, 0)
    endVertex = Vertex(0, self.radius, 0)

    # radiosEdge = Edge(startVertex, endVertex)
    lastvertex = endVertex
    self.Vertexes.append(lastvertex)
    
    for n in range(self.parallels):
      rotationVertex = GeometricTransformation.rotation(endVertex, -self.parallelAngle, 'z')
      self.Edges.append(Edge(lastvertex, rotationVertex))
      lastvertex = rotationVertex
      self.Vertexes.append(lastvertex)

    # for t in self.Edges:
      # print(t.coordinates())