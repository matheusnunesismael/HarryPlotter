from models.Vertex import Vertex
from models.Edge import Edge
from models.GeometricTransformation import GeometricTransformation as gt
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

        # Essa variável é usada para armazenar o primeiro ponto de cada polígono (internou externo)
        first = self.vertexes[0]
        # Variável responsável por armazenar o índice do primeiro ponto de cada polígono
        firstIndex = 0
        for i, point in enumerate(self.vertexes):
            # se for o ultimo elemento precisa ligar ele com o primeiro ponto do polígono (pra fechar)
            if i == len(self.vertexes) - 1:
                self.edges.append(Edge(point, first))
            else:
                print(f'Point: {point.x} , {point.y}')
                print(f'Fisrt: {first.x} , {first.y}')
                print(
                    f'Next Point: {self.vertexes[i+1].x} , {self.vertexes[i+1].y}')

                print(
                    f'Euclidean distance point and first: {gt.euclideanDistance(point.x, point.y, first.x, first.y)}')
                print(
                    f'Euclidean distance point and next element: {gt.euclideanDistance(point.x, point.y, self.vertexes[i+1].x, self.vertexes[i+1].y)}\n\n')
                if point != first and gt.euclideanDistance(point.x, point.y, first.x, first.y) < gt.euclideanDistance(point.x, point.y, self.vertexes[i+1].x, self.vertexes[i+1].y) and abs(gt.euclideanDistance(point.x, point.y, first.x, first.y) - gt.euclideanDistance(point.x, point.y, self.vertexes[i+1].x, self.vertexes[i+1].y)) > 10:
                    print('Entrou aqui')
                    self.edges.append(Edge(point, first))
                    first = self.vertexes[i+1]
                    firstIndex = i+1
                else:
                    self.edges.append(
                        Edge(self.vertexes[i], self.vertexes[i+1]))
