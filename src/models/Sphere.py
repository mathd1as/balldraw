from .Vertex import Vertex
from .Edge import Edge
from .GeometricTransformation import GeometricTransformation
class Sphere:
  def __init__(self, radius, meridians, parallels):    
    self.meridians = meridians
    self.parallels = parallels
    self.radius = radius
    self.edges = []
    self.vertexes = []

    self.shapeSphere()

  def shapeSphere(self):
    self.meridianAngle = 360 / self.meridians
    self.parallelAngle = 180 / (self.parallels + 1)
    endVertex = Vertex(0, self.radius, 0)
    lastVertex = endVertex
    self.vertexes.append(lastVertex)
    
    for n in range(self.parallels):
      rotationVertex = GeometricTransformation.rotation(endVertex, -self.parallelAngle, 'z')
      self.edges.append(Edge(lastVertex, rotationVertex))
      lastVertex = rotationVertex
      self.vertexes.append(lastVertex)
