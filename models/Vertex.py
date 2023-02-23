class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getXY(self):
        return self.x, self.y

    def getY(self):
        return self.y

    def getX(self):
        return self.x

    def getZ(self):
        return self.z

    def getXYZ(self):
        return self.x, self.y, self.z
