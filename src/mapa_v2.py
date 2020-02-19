import copy
import math


class BuscaAEstrela:
    estadoSolucao = None
    quant_estados = 0

    def busca(self, estadoInicial, maxIteracoes):
        self.quant_estados = 0
        folhas = [estadoInicial]
        passos = 0
        while(passos < maxIteracoes):
            passos += 1
            menor_f = 10000000
            folha_escolhida = None

            for folha in folhas:
                f = folha.calc_f()
                if(f < menor_f):
                    menor_f = f
                    folha_escolhida = folha
                    # print(folha_escolhida.toString())

            for op in folha_escolhida.getOperacoes():
                nova_folha = folha_escolhida.novoEstado(op)
                self.quant_estados += 1
                if nova_folha.verificaObjetivo():
                    self.estadoSolucao = nova_folha
                    return True
                folhas.append(nova_folha)
            folhas.remove(folha_escolhida)
        return False

    def getOperacoesSolucao(self):
        res = []
        estado = self.estadoSolucao
        while(estado != None):
            res.append(estado.getOperacao())
            estado = estado.getPai()
            res.reverse()
        return res

    def getEstadoSolucao(self):
        return self.estadoSolucao


# ======================================================


class BuscaAmplitude:
    estadoSolucao = None
    quant_estados = 0

    def busca(self, estadoInicial, maxIteracoes):
        self.quant_estados = 0
        res = False
        passos = 0
        folhas = []
        folhas.append(estadoInicial)
        while((res == False)and (passos < maxIteracoes)):
            folhasNew = []
            for estado in folhas:
                for op in estado.getOperacoes():
                    filho = estado.novoEstado(op)
                    self.quant_estados += 1
                    if filho.verificaObjetivo():
                        self.estadoSolucao = filho
                        return True
                    else:
                        folhasNew.append(filho)
            folhas = folhasNew
            passos += 1
        return res

    def getOperacoesSolucao(self):
        res = []
        estado = self.estadoSolucao
        while(estado != None):
            res.append(estado.getOperacao())
            estado = estado.getPai()
            res.reverse()
        return res

    def getEstadoSolucao(self):
        return self.estadoSolucao

# ===========================================================================


class Mapa:
    mapa = [[]]
    saida = [0, 0]

    def criaMapa(self, tamx, tamy, saida):
        self.mapa = []
        for iy in range(tamy):
            self.mapa.append([])
            for ix in range(tamx):
                self.mapa[iy].append(".")
        self.mapa[saida[1]][saida[0]] = "S"
        self.saida = saida

    def criaParede(self, xini, yini, xfim, yfim):
        for ix in range(xini, xfim+1):
            for iy in range(yini, yfim+1):
                self.mapa[iy][ix] = "#"

    def toString(self):
        res = ""
        for iy in range(len(self.mapa)):
            for ix in range(len(self.mapa[0])):
                res = res+self.mapa[len(self.mapa)-iy-1][ix]
            res = res+"\n"
        return res


# ===========================================================================
class EstadoRobo:
    mapa = None
    operacao = None
    pai = None
    posicao = [0, 0]

    def novoEstado(self, op):
        novo = EstadoRobo()
        novo.mapa = self.mapa
        novo.pai = self
        novo.posicao = [0, 0]
        novo.posicao[0] = self.posicao[0]
        novo.posicao[1] = self.posicao[1]

        novo.aplicaOperacao(op)

        return novo

    def aplicaOperacao(self, op):
        self.posicao[0] += op[0]
        self.posicao[1] += op[1]
        self.operacao = op
        self.mapa.mapa[self.posicao[1]][self.posicao[0]] = "+"

    def verificaObjetivo(self):
        return (self.posicao[0] == self.mapa.saida[0])and(self.posicao[1] == self.mapa.saida[1])

    def toString(self):
        return self.mapa.toString()

    def getOperacoes(self):
        ops = []
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                p = [self.posicao[0]+ix, self.posicao[1]+iy]
                if (ix != 0 or iy != 0):
                    if p[0] >= 0 and p[0] < len(self.mapa.mapa[0]) and p[1] >= 0 and p[1] < len(self.mapa.mapa):
                        if self.mapa.mapa[p[1]][p[0]] == "." or self.mapa.mapa[p[1]][p[0]] == "S":
                            ops.append([ix, iy])

        return ops

    def getPai(self):
        return self.pai

    def getOperacao(self):
        return self.operacao

    def calc_custo(self):
        custo = 0
        estado = self
        while(estado.getPai() != None):
            if estado.operacao[0] != 0 and estado.operacao[1] != 0:
                custo += 1.414
            else:
                custo += 1.0
            estado = estado.getPai()
        return custo

    def calc_h(self):
        x = self.mapa.saida[0]-self.posicao[0]
        y = self.mapa.saida[1]-self.posicao[1]
        return math.sqrt(x*x+y*y)

    def calc_f(self):
        return self.calc_custo()+self.calc_h()


# ===========================================================================
mapa = Mapa()
mapa.criaMapa(30, 20, [29, 19])
mapa.criaParede(0, 3, 19, 3)
mapa.criaParede(10, 12, 29, 12)
# print(mapa.toString())

estadoIni = EstadoRobo()
estadoIni.posicao = [0, 0]
estadoIni.mapa = mapa
print(estadoIni.toString())
busca = BuscaAEstrela()
busca.busca(estadoIni, 1000)
solucao = busca.getEstadoSolucao()
estado = solucao
while(estado != None):
    estado.mapa.mapa[estado.posicao[1]][estado.posicao[0]] = "*"
    estado = estado.getPai()
solucao.mapa.mapa[solucao.mapa.saida[1]][solucao.mapa.saida[0]] = "S"
print(("=================\n"))
res = busca.getOperacoesSolucao()
for op in res:
    print(op)
print(("=================\n"))
print(solucao.toString())
print("quant_estados: "+str(busca.quant_estados))
