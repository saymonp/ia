import copy


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
            for op in folha_escolhida.getOperacoes():
                nova_folha = folha_escolhida.novoEstado(op)
                self.quant_estados += 1
                print(nova_folha.toString())
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

    def calc_custo(self):
        custo = 0
        estado = self
        while(estado.getPai() != None):
            custo += 1
            estado = estado.getPai()
        return custo

    def calc_h(self):
        h = 0
        for i in range(3):
            for j in range(3):
                if(self.quebraCabeca[i][j] == '1'):
                    h += abs(i-0)+abs(j-1)
                if(self.quebraCabeca[i][j] == '2'):
                    h += abs(i-0)+abs(j-2)
                if(self.quebraCabeca[i][j] == '3'):
                    h += abs(i-1)+abs(j-0)
                if(self.quebraCabeca[i][j] == '4'):
                    h += abs(i-1)+abs(j-1)
                if(self.quebraCabeca[i][j] == '5'):
                    h += abs(i-1)+abs(j-2)
                if(self.quebraCabeca[i][j] == '6'):
                    h += abs(i-2)+abs(j-0)
                if(self.quebraCabeca[i][j] == '7'):
                    h += abs(i-2)+abs(j-1)
                if(self.quebraCabeca[i][j] == '8'):
                    h += abs(i-2)+abs(j-2)
        return h

    def calc_f(self):
        return self.calc_custo()+self.calc_h()


# ===========================================================================
estadoIni = EstadoQC()
estadoIni.quebraCabeca = [['1', '4', '2'], ['3', '5', '8'], ['6', '7', ' ']]
busca = BuscaAEstrela()
busca.busca(estadoIni, 1000)
solucao = busca.getEstadoSolucao()
print(("=================\n"))
res = busca.getOperacoesSolucao()
for op in res:
    print(op)
print(("=================\n"))
print(solucao.toString())
print("quant_estados: "+str(busca.quant_estados))
