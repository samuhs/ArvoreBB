from arvoreBusca import *

class ArvoreBB:

    def __init__(self):
        self.Node= []

    def criar_arvore(self):

        adicionar = Node(5)
        self.Node.append(adicionar) #INDEX 0

        adicionar = Node(8)
        self.Node.append(adicionar) #INDEX 1
        self.Node[0].inserir_direita(1)

        adicionar = Node(3) #INDEX 2
        self.Node.append(adicionar)
        self.Node[0].inserir_esquerda(2)

        adicionar = Node(9) #INDEX 3
        self.Node.append(adicionar)
        self.Node[1].inserir_direita(3)

        adicionar = Node(6) #INDEX 4
        self.Node.append(adicionar)
        self.Node[1].inserir_esquerda(4)

        adicionar = Node(4) #INDEX 5
        self.Node.append(adicionar)
        self.Node[2].inserir_direita(5)

        adicionar = Node(1) #INDEX 6
        self.Node.append(adicionar)
        self.Node[2].inserir_esquerda(6)

        adicionar = Node(9) #INDEX 7
        self.Node.append(adicionar)

        adicionar = Node(7) #INDEX 8
        self.Node.append(adicionar)
        self.Node[4].inserir_direita(8)

    def inserir_chave(self):
