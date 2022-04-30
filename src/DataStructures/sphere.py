class Sphere:
  def __init__(self, faces, meridians, parallels):    
    self.faces = faces
    self.meridians = meridians
    self.parallels = parallels
    self.shapeSphere

  def shapeSphere(self):
    self.meridianAngle = 360 / self.meridians
    self.parallelAngle = 180 / self.parallels
    self.radius = 10

