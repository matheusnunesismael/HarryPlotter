from tkinter import *
from models.Vertex import Vertex
from models.GeometricTransformation import GeometricTransformation as gt


window = Tk()
window.title('Computação gráfica: modelagem de cenas')

canvas = Canvas(window, width = 800, height = 600) #tamanho do cavnas
canvas.pack()


# for vertex in sphere.vertexes:
  # print(vertex.coordinatesXYZ())
  # gt.translation(vertex, Vertex(400, 300, 1))

VRP = Vertex(0, 0, 1)
focalPoint = Vertex(0, 0, 0)
viewUp = Vertex(0, 1, 0)
dp = gt.distanceTwoVertexes(VRP,focalPoint)


for edge in sphere.edges:
  canvas.create_line(edge.startVertex.coordinatesXY(), edge.endVertex.coordinatesXY())

for v in sphere.vertexes:
  print(v.coordinatesXYZ())

window.mainloop()