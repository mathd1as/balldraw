import re
from .Vertex import Vertex
from .Edge import Edge
from .Face import Face
from .GeometricTransformation import GeometricTransformation
class Sphere:
  def __init__(self, radius, meridians, parallels):    
    self.meridians = meridians
    self.parallels = parallels
    self.radius = radius
    self.faces = []
    self.edges = []
    self.vertexes = []

    self.shapeSphere()

  def shapeSphere(self):
    self.meridianAngle = 360 / self.meridians
    self.parallelAngle = 180 / (self.parallels + 1)
    radiusVertex = Vertex(0, self.radius, 0)

    meridianVertexes = self.createMeridian(radiusVertex)
    meridiansList = []
    
    for i in range(self.meridians):
      meridiansList.append(self.rotateMeridianVertexes(meridianVertexes))

    self.createTopFaces(Vertex(0, self.radius, 0), meridiansList)
    self.createSquareFaces(meridiansList)
    self.createBottonFaces(Vertex(0,-self.radius,0), meridiansList)
    
    for meridian in meridiansList:
      self.vertexes.extend(meridian)

  def createMeridian(self, radiusVertex):
    vertexesArray = []

    for n in range(self.parallels):
      rotationVertex = GeometricTransformation.rotation(radiusVertex, -self.parallelAngle, 'z')
      vertexesArray.append(rotationVertex)

    return vertexesArray
  
  def rotateMeridianVertexes(self, vetexesArray):
    rotatedMeridiansVertexes = []

    for vertex in vetexesArray:
      rotationVertex = GeometricTransformation.rotation(vertex, self.meridianAngle, 'y')
      rotatedMeridiansVertexes.append(rotationVertex)
      
    return rotatedMeridiansVertexes

  # recives a vertex matriz, each line is a meridian
  def createSquareFaces(self, meridiansArray):
    for i in range(self.meridians - 1):
      for j in range(self.parallels - 1):
        edgeList = []

        edgeList.append(Edge(meridiansArray[i][j], meridiansArray[i+1][j]))
        edgeList.append(Edge(meridiansArray[i+1][j], meridiansArray[i+1][j+1]))
        edgeList.append(Edge(meridiansArray[i+1][j+1], meridiansArray[i][j+1]))
        edgeList.append(Edge(meridiansArray[i+1][j+1], meridiansArray[i+1][j+1]))        
        self.faces.append(Face(edgeList))
        self.edges.append(edgeList[0])
        self.edges.append(edgeList[1])

    lastid = self.meridians-1
    for i in range(self.parallels-1):
      edgeList = []
      edgeList.append(Edge(meridiansArray[lastid][i], meridiansArray[0][i]))
      edgeList.append(Edge(meridiansArray[0][i], meridiansArray[0][i+1]))
      edgeList.append(Edge(meridiansArray[0][i+1], meridiansArray[lastid][i+1]))
      edgeList.append(Edge(meridiansArray[0][i+1], meridiansArray[0][i+1]))        
      self.faces.append(Face(edgeList))
      self.edges.append(edgeList[0])
      self.edges.append(edgeList[1])

  def createTopFaces(self, vertex, meridiansArray):
    for i in range(self.meridians - 1):
      edgeList = []

      edgeList.append(Edge(meridiansArray[i][0], meridiansArray[i + 1][0]))
      edgeList.append(Edge(meridiansArray[i+1][0], vertex))
      edgeList.append(Edge(vertex, meridiansArray[i][0]))
      
      self.faces.append(Face(edgeList))
      self.edges.append(edgeList[1])
      self.edges.append(edgeList[2])
    
    edgeList = []
    lastid = self.meridians -1
    edgeList.append(Edge(meridiansArray[lastid][0], meridiansArray[0][0]))
    edgeList.append(Edge(meridiansArray[0][0], vertex))
    edgeList.append(Edge(vertex, meridiansArray[lastid][0]))
    self.faces.append(Face(edgeList))
    self.edges.append(edgeList[1])
    self.edges.append(edgeList[2])
    
    self.vertexes.append(vertex)

  def createBottonFaces(self, vertex, meridiansArray):
      lastVertex = self.parallels-1
      for i in range(self.meridians - 1):
          edgeList = []

          edgeList.append(Edge(meridiansArray[i][lastVertex], meridiansArray[i + 1][lastVertex]))
          edgeList.append(Edge(meridiansArray[i+1][lastVertex], vertex))
          edgeList.append(Edge(vertex, meridiansArray[i][lastVertex]))

          self.faces.append(Face(edgeList))
          self.edges.extend(edgeList)
    
      edgeList = []
      lastid = self.meridians -1
      edgeList.append(Edge(meridiansArray[lastid][lastVertex], meridiansArray[0][lastVertex]))
      edgeList.append(Edge(meridiansArray[0][lastVertex], vertex))
      edgeList.append(Edge(vertex, meridiansArray[lastid][lastVertex]))

      self.faces.append(Face(edgeList))
      self.edges.extend(edgeList)
      self.vertexes.append(vertex)
