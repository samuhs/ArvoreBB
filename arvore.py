from nos import *

class arvore:

    def __init__(self):
        self.arvore= []
        self.arvore_canaria=[]
        self.count =1

    def montar_arvore(self):

        nos=binaria('A','B',0)
        self.arvore.append(nos)

        nos=binaria('B','H','C')
        self.arvore.append(nos)

        nos=binaria('C',0,'D')
        self.arvore.append(nos)

        nos=binaria('D',0,'E')
        self.arvore.append(nos)

        nos=binaria('E','K','F')
        self.arvore.append(nos)

        nos=binaria('F',0,'G')
        self.arvore.append(nos)

        nos=binaria('G','M')
        self.arvore.append(nos)

        nos=binaria('H','N','I')
        self.arvore.append(nos)

        nos=binaria('I',0,'J')
        self.arvore.append(nos)

        nos=binaria('J')
        self.arvore.append(nos)

        nos=binaria('K','P','L')
        self.arvore.append(nos)

        nos=binaria('L','Q')
        self.arvore.append(nos)

        nos=binaria('M')
        self.arvore.append(nos)

        nos=binaria('N',0,'O')
        self.arvore.append(nos)

        nos=binaria('O')
        self.arvore.append(nos)

        nos=binaria('P')
        self.arvore.append(nos)

        nos=binaria('Q')
        self.arvore.append(nos)

    def montar_canaria(self):
        self.montar_arvore()
        j=0
        for i in range(len(self.arvore)):
            self.arvore[i].printar_irmao
        #while i != len(self.arvore):
        pai=self.arvore[i].voltar_conteudo()
        self.arvore_canaria.append(Canaria(pai))
        if pai == self.arvore[i].voltar_conteudo():
            if (self.arvore[i].voltar_filhos()) == 1:
                self.arvore_canaria.colocar_filho(self.arvore[i].voltar_filhos())
                procurar_irmao(self.arvore[i].voltar_filhos())
        self.arvore_canaria[i].printar_filhos()


    def procura_irmao(self,irmao):

        for i in len(self.arvore)-1:
            if irmao == self.arvore[i].voltar_conteudo():
                if len(self.arvore[i].irmao) == 1:
                    self.arvore_canaria.colocar_filho(self.arvore[i].irmao)
                    irmao = self.arvore[i].irmao
                    i=0

a=arvore()
a.montar_canaria()
