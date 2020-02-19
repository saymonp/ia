import neurolab as nl
import numpy as np
import pylab as pl

# criar dados de treinamento
x_treino = [[0, 0], [1, 0], [0, 1], [1, 1]]
y_treino = [[0], [1], [1], [0]]

net = nl.net.newff([[0, 1], [0, 1]], [3, 1])

# Treina a rede neural
erro = net.train(x_treino, y_treino, epochs=500, show=100, goal=0.002)
print("rede treinada")

# simula a rede neural (ativa a rede)
y_sim = net.sim(x_treino)

print("rede simulada")

pl.plot(erro)
pl.savefig("plot.png")

# plota os pontos de treinamento
for i in range(len(x_treino)):
    print(str(x_treino[i][0])+" xor "+str(x_treino[i][1]) +
          " ="+str(y_sim[i])+str(y_treino[i]))
