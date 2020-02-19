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
    quebraCabeca = [[' ', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
    operacao = ' '
    pai = None
    filhos = []
    operacoes = ['c', 'b', 'd', 'e']

    def novoEstado(self, op):
        res = copy.deepcopy(self)
        res.pai = self
        res.aplicaOperacao(op)
        return res

    def aplicaOperacao(self, op):
        i = 0
        j = 0
        self.operacao = op
        while((self.quebraCabeca[i][j] != ' ') and (i < 3)):
            j += 1
            if(j >= 3):
                i += 1
                j = 0
        if((op == 'c')and(i < 2)):
            self.quebraCabeca[i][j] = self.quebraCabeca[i+1][j]
            self.quebraCabeca[i+1][j] = ' '
        if((op == 'b')and(i > 0)):
            self.quebraCabeca[i][j] = self.quebraCabeca[i-1][j]
            self.quebraCabeca[i-1][j] = ' '
        if((op == 'd')and(j > 0)):
            self.quebraCabeca[i][j] = self.quebraCabeca[i][j-1]
            self.quebraCabeca[i][j-1] = ' '
        if((op == 'e')and(j < 2)):
            self.quebraCabeca[i][j] = self.quebraCabeca[i][j+1]
            self.quebraCabeca[i][j+1] = ' '

    def verificaObjetivo(self):
        return self.quebraCabeca[0][0] == ' ' and self.quebraCabeca[0][1] == '1' and self.quebraCabeca[0][2] == '2' \
            and self.quebraCabeca[1][0] == '3' and self.quebraCabeca[1][1] == '4' and self.quebraCabeca[1][2] == '5' \
            and self.quebraCabeca[2][0] == '6' and self.quebraCabeca[2][1] == '7' and self.quebraCabeca[2][2] == '8' \


    def toString(self):
        return "----\n" \
            + "|"+self.quebraCabeca[0][0] + self.quebraCabeca[0][1]+self.quebraCabeca[0][2]+"|\n"\
            + "|"+self.quebraCabeca[1][0] + self.quebraCabeca[1][1]+self.quebraCabeca[1][2]+"|\n"\
            + "|"+self.quebraCabeca[2][0] + self.quebraCabeca[2][1]+self.quebraCabeca[2][2]+"|\n"\
            + "----\n"

    def getOperacoes(self):
        return self.operacoes

    def getPai(self):
        return self.pai

    def getFilhos(self):
        return self.filhos

    def getOperacao(self):
        return self.operacao


# ===========================================================================
estadoIni = EstadoQC()
estadoIni.quebraCabeca = [['1', '4', '2'], ['3', '5', '8'], ['6', '7', ' ']]
busca = BuscaAmplitude()
busca.busca(estadoIni, 10)
solucao = busca.getEstadoSolucao()
print(("=================\n"))
res = busca.getOperacoesSolucao()
for op in res:
    print(op)
print(("=================\n"))
print(solucao.toString())
