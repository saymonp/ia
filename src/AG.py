import numpy as np
import pylab as pl
import random
import copy


class AG:
    pop = []

    def gera_pop_ini(self, quant):
        self.pop = []
        for range(quant):
            gen = []
            for i in range(6):
                gen.append(random.randint(0, 9))
            self.pop.append(gen)

    def torneio(self, quant):
        apt_max = -1000000.0
        sel = None
        for i in range(quant):
            idx = random.randint(0, len(self.pop)-1)
            apt = self.aptidao(self.pop[idx])
            if apt > apt_max:
                apt_max = apt
                sel = idx
        return sel

    def selecao(self, quant, tam_torneio):
        nova_pop = []
        for i in range(quant):
            sel = self.torneio(tam_torneio)
            nova_pop.append(copy.deepcopy(self.pop[sel]))
            del(self.pop[sel])
        return nova_pop

    def cruzamento(self, pai, mae):
        ponto = random.randint(1, len(mae)-2)
        filho = []
        if random.random() > 0.5:
            filho[0:ponto] = mae[0:ponto]
            filho[ponto:] = pai[ponto:]
        else:
            filho[0:ponto] = pai[0:ponto]
            filho[ponto:] = mae[ponto:]
        return filho

    def mutacao(self, gen, taxa_mutacao):
        for i in range(len(gen)):
            if random.random() < taxa_mutacao:
                gen[i] = random.randint(0, 9)
        return gen

    def reproducao(self, genitores, tam_pop, taxa_mutacao):
        self.pop = []
        for i in range(tam_pop):
            pai = random.randint(0, len(genitores)-1)
            mae = random.randint(0, len(genitores)-1)
            filho = self.cruzamento(genitores[pai], genitores[mae])
            filho = self.mutacao(filho, taxa_mutacao)
            self.pop.append(filho)

    def funcao_objetivo(self, x):
        return x*x+2*x-3

    def fenotipo(self, gen):
        ex = 1.0
        fen = 0.0
        for g in gen:
            fen += float(g)*10**ex
            ex = ex-1.0
        return fen

    def aptidao(self, gen):
        x = self.fenotipo(gen)
        return -abs(self.funcao_objetivo(x))


ag = AG()
tam_pop = 1000
quant_selecao = 100
quant_geracoes = 50
taxa_mutacao = 0.05
tam_torneio = 4
erro = []
ag.gera_pop_ini(tam_pop)
for ger in range(quant_geracoes):
    genitores = ag.selecao(quant_selecao, tam_torneio)
    ag.reproducao(genitores, tam_pop, taxa_mutacao)
    melhor = ag.selecao(1, tam_pop)
    y = ag.funcao_objetivo(ag.fenotipo(melhor[0]))
    erro.append(abs(y))


x = np.linspace(-5, 5, 100)
y = ag.funcao_objetivo(x)

pl.subplot(211)
x2 = []
x2.append(ag.fenotipo(melhor[0]))
x2 = np.array(x2)
y2 = ag.funcao_objetivo(x2)
gr = pl.plot(x, y, '-', x2, y2, 'p')
pl.axhline(0)
pl.subplot(212)
pl.plot(np.array(erro))
pl.show()
pl.savefig('plot.png')
print("AG executado!")
print("erro "+str(erro[-1]))
