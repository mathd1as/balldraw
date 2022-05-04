from .Vertex import Vertex
from .Edge import Edge
from .Face import Face
from .GeometricTransformation import GeometricTransformation
class Sphere:
  def __init__(self, radius, meridians, parallels):    
    self.meridians = meridians
    self.parallels = parallels
    self.radius = radius
    self.edges = []
    self.vertexes = []
    self.faces = []

    self.shapeSphere()

  def shapeSphere(self):
    self.meridianAngle = 360 / self.meridians
    self.parallelAngle = 180 / (self.parallels + 1)
    radiusVertex = Vertex(0, self.radius, 0)

    meridian = self.createMeridian(radiusVertex)
    meridiansArray = []

    meridiansArray.append(meridian)
    for i in range(self.meridians):
      meridiansArray.append(self.rotationMeridiansVertexes(meridian))
    

  def createMeridian(self, radiusVertex):
    vertexesArray = []

    for n in range(self.parallels):
      rotationVertex = GeometricTransformation.rotation(radiusVertex, -self.parallelAngle, 'z')
      vertexesArray.append(rotationVertex)

    return vertexesArray
  
  def rotationMeridiansVertexes(self, vetexesArray):
    rotatedMeridiansVertexes = []

    for vertex in vetexesArray:
      rotationVertex = GeometricTransformation.rotation(vertex, self.meridianAngle, 'y')
      rotatedMeridiansVertexes.append(rotationVertex)
  
  def createSquareFaces(self, meridiansArray):
    for i in range(self.meridians - 1):
      for j in range(self.parallels - 1):
        edgeList = []

        edgeList.append(Edge(meridiansArray[i], meridiansArray[j]))
        edgeList.append(Edge(meridiansArray[j], meridiansArray[j + 1]))
        edgeList.append(Edge(meridiansArray[j + 1], meridiansArray[i + 1]))
        edgeList.append(Edge(meridiansArray[i + 1], meridiansArray[i]))

      self.faces.append(Face(edgeList))
      self.edges.append(edgeList[0])
      self.edges.append(edgeList[1])

  def createTriangleFaces(self, vertex, meridiansArray):
    for i in range(self.meridians - 1):
      edgeList = []

      edgeList.append(Edge(meridiansArray[i], meridiansArray[i + 1]))
      edgeList.append(Edge(meridiansArray[i], vertex))
      edgeList.append(Edge(vertex, meridiansArray[i + 1]))

