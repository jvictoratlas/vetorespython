import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
      self.capacidade = capacidade
      self.ultima_posicao = -1
      self.valores = np.empty(self.capacidade, dtype=int) 
    

    def insere(self, valor):
      if self.ultima_posicao == self.capacidade - 1:
        print('Capacidade máxima atingida')
      else:
        self.ultima_posicao += 1
        self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
      for i in range(self.ultima_posicao + 1):
        if valor == self.valores[i]:
          return i
      return -1

    def imprime(self):
      if self.ultima_posicao == -1:
        print('O vetor está vazio')
      else:
        for i in range(self.ultima_posicao + 1):
          print(i, '-', self.valores[i])

    def excluir(self, valor):
      posicao = self.pesquisar(valor)
      if posicao == -1:
        return -1
      else:
        for i in range(posicao, self.ultima_posicao + 1):
          self.valores[i] = self.valores[i + 1]
          self.ultima_posicao -= 1

vetor = VetorNaoOrdenado(25)
vetor.insere(input('Insira um valor aqui '))
vetor.imprime()
vetor.excluir(35)
