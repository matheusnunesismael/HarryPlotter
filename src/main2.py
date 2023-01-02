from tkinter import *
from models.L import L
from models.Vertex import Vertex


window = Tk()
window.title('Computação gráfica: modelagem de cenas')

canvas = Canvas(window, width = 10, height = 10) #tamanho do cavnas
canvas.pack()


test = L()
for edge in test.edges:
  print(edge.startVertex.coordinatesXY())
  
  # canvas.create_line(edge.startVertex.coordinatesXY(), edge.endVertex.coordinatesXY())
  # print(edge.startVertex.coordinatesXY(), edge.endVertex.coordinatesXY())

canvas.create_line(100,200,200,35, fill="green", width=5)

window.mainloop()