class Edge:
  def __init__(self, canvas, vertexA, vertexB):
    self.canvas = canvas
    self.vertexA = vertexA
    self.vertexB = vertexB
  
  def createLine(self):
    self.canvas.create_line(self.vertexA.x, self.vertexA.y, self.vertexB.x, self.vertexB.y)
