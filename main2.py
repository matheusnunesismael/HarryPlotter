from tkinter import *
from models.L import L
from models.Vertex import Vertex
from models.GeometricTransformation import GeometricTransformation as gt

window = Tk()
window.title('Computação gráfica: modelagem de cenas')

canvas = Canvas(window, width=800, height=600)  # tamanho do cavnas
canvas.pack()


test = L()

# test.rotation()

VRP = Vertex(0, 0, 1)
focalPoint = Vertex(0, 0, 0)
viewUp = Vertex(0, 1, 0)
dp = gt.distanceTwoVertexes(VRP, focalPoint)
gt.calculateSRCVertexes(test.vertexes, VRP, focalPoint, viewUp)
gt.calculateSRTVertexes(test.vertexes, Vertex(1, 0, 1),
                        Vertex(300, 300, 1), Vertex(0, 0, 1), Vertex(800, 600, 1), dp)

for edge in test.edges:
    # print(edge.startVertex.getXY())

    canvas.create_line(edge.startVertex.getXY(),
                       edge.endVertex.getXY(), fill="red")
    # print(edge.startVertex.getXY(), edge.endVertex.getXY())


window.mainloop()
