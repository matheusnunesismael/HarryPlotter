from models.Vertex import Vertex
from models.Edge import Edge
from models.GeometricTransformation import GeometricTransformation
import pandas as pd
import math


class L:
    def __init__(self):
        self.vertexes = []

        file = pd.read_csv('./letters.csv', ',')

        # print(file, len(file))

        for i in range(len(file) - 1):
            # print(file['x'][i])
            self.vertexes.append(Vertex(file['x'][i], file['y'][i], 1))

        self.edges = []

        print(len(self.vertexes))

        first = self.vertexes[0]
        firstIndex = 0

        print(first.y)

        for i, point in enumerate(self.vertexes):
            if i == len(self.vertexes) - 1:
                self.edges.append(Edge(point, first))
            elif point != first and i > firstIndex+10 and math.sqrt(math.pow(point.x - first.x, 2)+math.pow(point.y - first.y, 2)) < math.sqrt(math.pow(point.x - self.vertexes[i+1].x, 2)+math.pow(point.y - self.vertexes[i+1].x, 2)):
                print("TESTE")
                self.edges.append(Edge(point, first))
                first = self.vertexes[i+1]
                firstIndex = i+1
            # if i == len(self.vertexes) - 1:
            #   # self.edges.append(Edge(self.vertexes[i], ))
            #   print(self.vertexes[-1], self.vertexes[0])
            #   self.edges.append(Edge(self.vertexes[-1], self.vertexes[0]))
                # pass
            else:
                self.edges.append(Edge(self.vertexes[i], self.vertexes[i+1]))
