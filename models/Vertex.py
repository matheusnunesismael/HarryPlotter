class Vertex:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y 
    self.z = z
  
  def coordinatesXY(self):
    return self.x, self.y

  def coordinatesY(self):
    return self.y

  def coordinatesX(self):
    return self.x

  def coordinatesZ(self):
    return self.z

  def coordinatesXYZ(self):
    return self.x,self.y, self.z