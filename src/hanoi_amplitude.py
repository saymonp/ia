import copy


class BuscaAmplitude:
    estadoSolucao = None

    def busca(self, estadoInicial, maxIteracoes):
        res = False
        passos = 0
        folhas = []
        folhas.append(estadoInicial)
        while((res == False)and (passos < maxIteracoes)):
            folhasNew = []
            for estado in folhas:
                for op in estado.getOperacoes():
                    filho = estado.novoEstado(op)
                    # print(filho.toString())
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


class EstadoQC:
    quebraCabeca = [[3, 2, 1], [], []]
    operacao = []
    pai = None
    filhos = []
    operacoes = []

    def novoEstado(self, op):
        res = copy.deepcopy(self)
        res.pai = self
        res.aplicaOperacao(op)
        return res

    def aplicaOperacao(self, op):
        self.quebraCabeca[op[1]].append(self.quebraCabeca[op[0]].pop())
        self.operacao = op

    def verificaObjetivo(self):
        return len(self.quebraCabeca[1]) == 3 or len(self.quebraCabeca[2]) == 3

    def toString(self):
        return str(self.quebraCabeca)

    def getOperacoes(self):
        ops = []
        for i1 in range(3):
            for i2 in range(3):
                if i1 != i2:
                    if len(self.quebraCabeca[i1]) > 0 and len(self.quebraCabeca[i2]) < 3:
                        if len(self.quebraCabeca[i2]) == 0:
                            ops.append([i1, i2])
                        else:
                            if self.quebraCabeca[i1][-1] < self.quebraCabeca[i2][-1]:
                                ops.append([i1, i2])
        return ops

    def getPai(self):
        return self.pai

    def getFilhos(self):
        return self.filhos

    def getOperacao(self):
        return self.operacao


# ===========================================================================
estadoIni = EstadoQC()
estadoIni.quebraCabeca = [[3, 2, 1], [], []]
busca = BuscaAmplitude()
busca.busca(estadoIni, 10)
solucao = busca.getEstadoSolucao()
print(("=================\n"))
res = busca.getOperacoesSolucao()
for op in res:
    print(op)
print(("=================\n"))
print(solucao.toString())
