import time
import random

class Tabuleiro(object):
    def __init__(self, n):
        self.rainha = Rainhas(n)
        self.colisoes = 0
        self.tamanho = n

    def resolver(self):
        if (self.ataques() >0):


            self.ordena()
            self.harmonizar()
            self.zeroAtq()
            if (self.ataques() >0):
                self.HC()

    def vizinhos(self):
        vizinho=[]
        for i in range(10):
            x=self
            vizinho.append(x)
            vizinho[i].ordenaC()
            vizinho[i].troca(vizinho[i].tamanho-1,random.randint(0,vizinho[i].tamanho-2))
            vizinho[i].ataques()
        return vizinho



    def HC(self):
        while True:
            vizinho = self.vizinhos()
            self.ordenaC()
            vizinho.sort(key=lambda r: r.colisoes)
            if(vizinho[0].colisoes<1):
                return

    def imprimir(self):
        stri = ""
        fh = open(str(self.tamanho) + "-queen.txt", "w")
        self.rainha.sort(key=lambda r: r.coluna)
        stri += "" + str(self.tamanho) + "\n"
        fh.write(stri)
        for i in range(len(self.rainha)-1):
            stri=""
            for j in self.rainha:
                if(j.linha==i):
                    stri+="1 "
                else:
                    stri+= "0 "
            stri+="\n"
            fh.write(stri)
        fh.close()

    def ataques(self):
        self.rainha.sort(key=lambda r: r.d1)
        k = 2
        rara = self.rainha[1]
        for i in (self.rainha):
            if i.d1 == rara.d1:
                i.atq = 1
                rara.atq = 1
            if k == len(self.rainha): break
            rara = self.rainha[k]
            k += 1
        self.rainha.sort(key=lambda r: r.d2)
        k = 2
        rara = self.rainha[1]
        for i in (self.rainha):

            if i.d2 == rara.d2:
                i.atq = 1
                rara.atq = 1

            if k == len(self.rainha): break
            rara = self.rainha[k]

            k += 1

        self.colisoes = 0
        for i in (self.rainha):
            self.colisoes += i.atq
        return self.colisoes

    def troca(self, i, j):  # cuidado esse metodo n atualiza os ataques!
        i = int(i)
        j = int(j)
        aux = self.rainha[i].coluna
        self.rainha[i].coluna = self.rainha[j].coluna
        self.rainha[j].coluna = aux

        self.rainha[i].d1 = self.rainha[i].coluna + self.rainha[i].linha + 1
        self.rainha[j].d1 = self.rainha[j].coluna + self.rainha[j].linha + 1

        self.rainha[i].d2 = -self.rainha[i].coluna + self.rainha[i].linha + 1
        self.rainha[j].d2 = -self.rainha[j].coluna + self.rainha[j].linha + 1

    def zeroAtq(self):
        for i in (self.rainha):
            i.atq = 0

    def ordena(self):
        self.rainha.sort(key=lambda r: r.coluna)
    def ordenaC(self):
        self.rainha.sort(key=lambda r: r.atq)

    def harmonizar(self):
        i = len(self.rainha)
        p = int(i / 2)
        while (p + 1 < i):
            self.troca(p, p + 1)
            p += 2
        if i % 2 == 1:
            self.ordena()
            self.troca(0, len(self.rainha) - 1)


class rainha(object):
    def __init__(self, l, c):
        self.linha = l
        self.coluna = c
        self.d1 = l + c + 1
        self.d2 = l - c + 1
        self.atq = 0

    def atualizaL(self, l):
        self.linha = l
        self.d1 = l + self.coluna
        self.d2 = l - self.coluna

    def atualizaC(self, c):
        self.coluna = c
        self.d1 = self.linha + c
        self.d2 = self.linha - c


def Rainhas(n):
    a = []
    j = 1
    for i in range(n):

        if (i < n):
            if j >= n:
                j = 0
            if (i == 0):
                a.append(rainha(j, i))
                j += 2
            else:
                a.append(rainha(j, i))
                j += 2

    return a


n = 20
start = time.time()
Tab = Tabuleiro(n)
print(n)
print("Colisões igual a")
Tab.resolver()
print(Tab.colisoes)
print(str((time.time() - start)) + " s")

# i = 0
#
# print("\n")
# while i < n:
#     print(Tab.rainha[i].atq)
#     i += 1
