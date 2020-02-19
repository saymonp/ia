import neurolab as nl
import numpy as np
import pylab as pl

# criar dados de treinamento
x_treino = np.linspace(-7, 7, 20)
y_treino = np.sin(x_treino) * 0.5
tam = len(x_treino)
# transforma de linnha para coluna
x_treino = x_treino.reshape(tam, 1)
y_treino = y_treino.reshape(tam, 1)

# cria rede neural com duas camadas inicializada aleatoriamente
net = nl.net.newff([[-7, 7]], [5, 1])

# Treina a rede neural
erro = net.train(x_treino, y_treino, epochs=500, show=100, goal=0.02)
print("rede treinada")

# simula a rede neural (ativa a rede)
y_sim = net.sim(x_treino)

x_teste = np.linspace(-7, 7, 200)
x_teste = x_teste.reshape(200, 1)

# simula a rede neural (ativa a rede)
y_teste = net.sim(x_teste)

print("rede simulada")

pl.subplot(211)
pl.plot(erro)

# plota os pontos de treinamento
pl.subplot(212)
pl.plot(x_treino, y_treino, '.', x_treino, y_sim, 'p', x_teste, y_teste, '-')
pl.show()
pl.savefig('plot.png')
