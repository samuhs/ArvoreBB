class Node:
    def __init__(self,chave):
        self.chave=chave
        self.pai=None
        self.conteudo=None
        self.Direita=None
        self.Esquerda=None
    def adicionar_conteudo(self,x):
        self.conteudo = x
    def printar_conteudo(self):
        x= str(self.chave)
        print(self.conteudo+" da chave "+x)
        print("\t Direita:",self.Direita," Esquerda: ",self.Esquerda)
    def inserir_direita(self,x):
        self.Direita = x
    def inserir_esquerda(self,x):
        self.Esquerda = x
    def inserir_pai(self,x):
        self.pai = x
    def retornar_pai(self):
        return self.pai
    def retornar_chave(self):
        return self.chave
    def retornar_direita(self):
        return self.Direita
    def retornar_esquerda(self):
        return self.Esquerda
    def zerar_node(self):
        self.chave = None
