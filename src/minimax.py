import copy
import math


class Estado:
    jogo = None

    def __init__(self):
        self.jogo = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def calc_pontos(self):
        pontos = 0
        for i in range(3):
            if self.jogo[i][0] == "X" and self.jogo[i][1] == "X" and self.jogo[i][2] == "X":
                pontos += 10
            if self.jogo[i][0] == "O" and self.jogo[i][1] == "O" and self.jogo[i][2] == "O":
                pontos -= 10
        for i in range(3):
            if self.jogo[0][i] == "X" and self.jogo[1][i] == "X" and self.jogo[2][i] == "X":
                pontos += 10
            if self.jogo[0][i] == "O" and self.jogo[1][i] == "O" and self.jogo[2][i] == "O":
                pontos -= 10
        if self.jogo[0][0] == "X" and self.jogo[1][1] == "X" and self.jogo[2][2] == "X":
            pontos += 10
        if self.jogo[0][2] == "X" and self.jogo[1][1] == "X" and self.jogo[2][0] == "X":
            pontos += 10
        if self.jogo[0][0] == "O" and self.jogo[1][1] == "O" and self.jogo[2][2] == "O":
            pontos -= 10
        if self.jogo[0][2] == "O" and self.jogo[1][1] == "O" and self.jogo[2][0] == "O":
            pontos -= 10
        return pontos

    def get_operacoes(self):
        ops = []
        for i in range(3):
            for j in range(3):
                if self.jogo[i][j] == " ":
                    ops.append([i, j])
        return ops

    def novo_estado(self, op, jogada):
        novo = copy.deepcopy(self)
        novo.jogo[op[0]][op[1]] = jogada
        return novo

# ======================================================


class Minimax():
    nivel = 0
    nivel_max = 10

    def maximiza(self, estado):
        self.nivel += 1
        ops = estado.get_operacoes()
        pontos = estado.calc_pontos()
        if (self.nivel > self.nivel_max) or (len(ops) == 0) or (pontos == 10) or (pontos == -10):
            self.nivel -= 1
            return [pontos, self]
        else:
            maximo = -1000
            estado_max = None
            for op in ops:
                novo_estado = estado.novo_estado(op, "X")
                [p, estado_min] = self.minimiza(novo_estado)
                if p > maximo:
                    maximo = p
                    estado_max = novo_estado
            self.nivel -= 1
            return [maximo, estado_max]

    def minimiza(self, estado):
        self.nivel += 1
        ops = estado.get_operacoes()
        pontos = estado.calc_pontos()
        if (self.nivel > self.nivel_max) or (len(ops) == 0) or (pontos == 10) or (pontos == -10):
            self.nivel -= 1
            return [pontos, self]
        else:
            minimo = 1000
            estado_min = None
            for op in ops:
                novo_estado = estado.novo_estado(op, "O")
                [p, estado_min] = self.maximiza(novo_estado)
                if p < minimo:
                    minimo = p
                    estado_min = novo_estado
            self.nivel -= 1
            return [minimo, estado_min]


estado_ini = Estado()
estado_ini.jogo = [[" ", " ", " "], [" ", "X", "O"], ["O", " ", "X"]]
minimax = Minimax()
[p, estado] = minimax.maximiza(estado_ini)
print(p)
print(estado.jogo)
