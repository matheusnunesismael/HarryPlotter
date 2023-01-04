from models.Vertex import Vertex
from models.Edge import Edge

class L:
    def __init__ (self):
        self.a = Vertex(-2.5, 3.5, 1)
        self.b = Vertex(-2.5, -3.5, 1)
        self.c = Vertex(2.5, -3.5, 1)
        self.d = Vertex(2.5, -2.5, 1)
        self.e = Vertex(-1.5, -2.5, 1)
        self.f = Vertex(-1.5, 3.5, 1)

        self.ab = Edge(self.a, self.b)
        self.bc = Edge(self.b, self.c)
        self.cd = Edge(self.c, self.d)
        self.de = Edge(self.d, self.e)
        self.ef = Edge(self.e, self.f)
        self.fa = Edge(self.f, self.a)

        self.vertexes = [self.a, self.b, self.c, self.d, self.e, self.f]
        self.edges = [self.ab, self.bc, self.cd, self.de, self.ef, self.fa]
        
