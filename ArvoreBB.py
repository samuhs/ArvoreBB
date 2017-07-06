from arvoreBusca import *

class ArvoreBB:

    def __init__(self):
        self.Node= []

    def criar_arvore(self):

        adicionar = Node(5)
        self.Node.append(adicionar) #INDEX 0
        self.Node[0].inserir_direita(1)
        self.Node[0].inserir_esquerda(2)
        self.Node[0].adicionar_conteudo('Node 0')

        adicionar = Node(8)
        self.Node.append(adicionar) #INDEX 1
        self.Node[1].inserir_direita(3)
        self.Node[1].inserir_esquerda(4)
        self.Node[1].adicionar_conteudo('Node 1')
        self.Node[1].inserir_pai(0)

        adicionar = Node(3) #INDEX 2
        self.Node.append(adicionar)
        self.Node[2].inserir_direita(5)
        self.Node[2].inserir_esquerda(6)
        self.Node[2].adicionar_conteudo('Node 2')
        self.Node[2].inserir_pai(0)

        adicionar = Node(9) #INDEX 3
        self.Node.append(adicionar)
        self.Node[3].adicionar_conteudo('Node 3')
        self.Node[3].inserir_pai(1)

        adicionar = Node(6) #INDEX 4
        self.Node.append(adicionar)
        self.Node[4].inserir_direita(7)
        self.Node[4].adicionar_conteudo('Node 4')
        self.Node[4].inserir_pai(1)

        adicionar = Node(4) #INDEX 5
        self.Node.append(adicionar)
        self.Node[5].adicionar_conteudo('Node 5')
        self.Node[5].inserir_pai(2)

        adicionar = Node(1) #INDEX 6
        self.Node.append(adicionar)
        self.Node[6].adicionar_conteudo('Node 6')
        self.Node[6].inserir_pai(2)

        adicionar = Node(7) #INDEX 7
        self.Node.append(adicionar)
        self.Node[7].adicionar_conteudo('Node 7')
        self.Node[7].inserir_pai(4)


    def buscar_chave(self,x):
        y = None
        index =0
        while y!=x:
            if index == None:
                break
            elif  x == self.Node[index].retornar_chave():
                y = self.Node[index].retornar_chave()
            elif x >self.Node[index].retornar_chave():
                if self.Node[index].retornar_direita() == None:
                    break
                index= self.Node[index].retornar_direita()
                print('Direita :',index)
            elif x < self.Node[index].retornar_chave():
                if self.Node[index].retornar_esquerda() == None:
                    break
                index = self.Node[index].retornar_esquerda()
                print('Esquerda :',index)
        return index #BASTA PRINTAR O NODE[INDEX].CONTEUDO

    def inserir_chave(self,x,index):
        adicionar = Node(x)
        self.Node.append(adicionar)
        if x < self.Node[index].retornar_chave():
            self.Node[index].inserir_esquerda(len(self.Node)-1)
        else:
            self.Node[index].inserir_direita(len(self.Node)-1)

        self.Node[len(self.Node)-1].adicionar_conteudo('Novo Node')
        self.Node[len(self.Node)-1].printar_conteudo()

    def maior_valor(self,index):
        while self.Node[index].retornar_direita != None:
            index = self.Node[index].retornar_direita()
            if self.Node[index].retornar_direita() == None:
                break
        return index

    def menor_valor(self,index):
        while self.Node[index].retornar_esquerda != None:
            index = self.Node[index].retornar_esquerda()
            if self.Node[index].retornar_esquerda() == None:
                break
        return index

    def remover_chave(self,x):

        index=self.buscar_chave(x)
        pai = self.Node[index].retornar_pai()
        newNode=self.verificar(index)
        print(pai)

        if pai == None:
            j=self.Node[index].retornar_direita()
            y=self.Node[index].retornar_esquerda()
            newNode=self.verificar(j)
            self.remover_chave_galho(newNode)
            self.Node[newNode].inserir_direita(j)
            self.Node[newNode].inserir_esquerda(y)
            self.Node[index].zerar_node()

        elif newNode == index:
            if self.Node[index].retornar_chave() < pai:
                self.Node[pai].inserir_esquerda(None)
                self.Node[index].zerar_node()
            else:
                self.Node[pai].inserir_direita(None)
                self.Node[index].zerar_node()
        else:
            if self.Node[index].retornar_chave() < pai:
                self.Node[pai].inserir_esquerda(newNode)
                self.remover_chave_galho(newNode)
                self.Node[newNode].inserir_pai(pai)
                self.Node[index].zerar_node()
            else:
                self.Node[pai].inserir_direita(newNode)
                self.remover_chave_galho(newNode)
                self.Node[newNode].inserir_pai(pai)
                self.Node[index].zerar_node()

    def remover_chave_galho(self,newNode):
        z=self.Node[newNode].retornar_direita()
        newNodePai=self.Node[newNode].retornar_pai()
        if z != None:
            newNodePai=self.Node[newNode].retornar_pai()
            self.Node[newNodePai].inserir_esquerda(z)
            self.Node[z].inserir_pai(newNodePai)
        else:
            self.Node[newNodePai].inserir_esquerda(None)


    def verificar(self,index):
        right= self.Node[index].retornar_direita()
        left= self.Node[index].retornar_esquerda()
        if right == None and left == None:
            return index
        else:
            if right == None and left != None:
                return self.Node[left].retornar_chave()
            elif right != None and left == None:
                return self.Node[right].retornar_chave()
            elif right != None and left != None:
                return self.menor_valor(index)

    def printar_arvore(self):
        for i in range(len(self.Node)):
            if self.Node[i].retornar_chave() != None:
                self.Node[i].printar_conteudo()
a = ArvoreBB()
a.criar_arvore()
a.printar_arvore()
a.remover_chave(5)
a.printar_arvore()
#a.maior_valor(0)
#a.menor_valor(1)
#index = a.buscar_chave(8)
#a.inserir_chave(12,index)
