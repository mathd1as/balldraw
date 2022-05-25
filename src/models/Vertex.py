class Vertex:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y 
    self.z = z
  
  def coordinatesXY(self):
    return self.x,self.y

  def coordinatesXYZ(self):
    return self.x,self.y, self.z
  
