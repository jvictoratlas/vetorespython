import numpy as np 

class VetorNaoOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade 
    self.ultima_posicao = -1 

    self.valores = np.empty(self.capacidade, dtype=int) 

    def imprime(self):
      if self.ultima_posicao == -1: 
        print("O vetor está vazio")
      else: 
        for i in range(self.ultima_posicao + 1):
          print(i, ' - ',self.valores[i]) 

    def insere(self, valor): 
      if self.ultima_posicao == self.capacidade - 1:
        print("Capacidde máxima atingida")
      else:
        self.ultima_posicao += 1 
        self.valores[self.ulima_posicao] = valor 

    def pesquisar(self, valor):
      for i in range(self.ultima_posicao + 1):
       if valor == self.valores[i]:
         return i 
       return -1 

  def excluir(self, valor): 
  #AQUI EU CHAMO A FUNÇÃO PESQUISAR 
   posicao = self.pesquisar(valor)
   if posicao == -1:
    return -1 
   else:
    for i in range(posicao, self.ultimsa_posicao):
      self.valores[i] = self.valores[i + 1]
      self.ultima_posicao -= 1

      vetor = VetorNaoOrdenado(5)
      vetor.imprime()
      vetor.insere(2)      
      valor.insere(input("Digite um valor a ser inserido no vetor"))

      vetor.imprime()
      vetor.insere(3)
      vetor.insere(5)
      vetor.insere(8)
      vetor.insere(1)

      vetor.imprime()
      vetor,insere(7)

      vetor.imprime()

      vetor.pesquisar(8)

      vetor.pesquisar(9)

      vetor.pesquisar(3)

      vetor.ultima_posicao 

      vetor.imprime()

      vetor.valoresexcluir(5)

      vetor.imprime()