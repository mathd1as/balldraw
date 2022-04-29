class Edge:
  def __init__(self, startVertex, endVertex):
    self.startVertex = startVertex
    self.endVertex = endVertex

  def calculateM(self):
    self.m = ( self.endVertex.y - self.startVertex.y) / (self.endVertex.x - self.startVertex.x)
