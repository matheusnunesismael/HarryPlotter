class Vertex:
  def __init__(self, x, y):
    self.x = x
    self.y = y 
  
  def coordinatesXY(self):
    return self.x, self.y

  def coordinatesY(self):
    return self.y

  def coordinatesX(self):
    return self.x

  # def coordinatesXYZ(self):
  #   return self.x,self.y, self.z