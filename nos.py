class Canaria:

    def __init__(self,conteudo):

        self.conteudo = conteudo
        self.filhos = []

    def colocar_filho(self,x):
        self.filhos.append(x)

    def retornar_filho(self,i):
        return self.filhos[i]

    def tamanho_filhos(self):
        return len(self.filhos)

class binaria:

    def __init__(self,conteudo,filhos=0,irmao=0):

        self.conteudo = conteudo
        self.filhos = filhos
        self.irmao = irmao

    def voltar_conteudo(self):
        return self.conteudo

    def voltar_filhos(self):
        return self.filhos

    def voltar_irmao(self):
        return self.irmao

    def printar_irmao(self):
        print(self.irmao)
