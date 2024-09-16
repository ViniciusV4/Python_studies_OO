import os
from modelos.avaliacao import Avaliacao 
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante e suas características."""
    
    restaurantes = []
    
    # Metódo construtor do Python
    def __init__(self, nome, categoria):
        
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False # com esse "_" estamos dizendo que o atributo é privado
        self._avaliacoes = [] # Lista de avaliações
        self._cardapio = [] # Lista de itens do cardápio
        Restaurante.restaurantes.append(self) # Adiciona o objeto a lista de restaurantes
        
    # Esse metódo é usado para imprimir como string o objeto    
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}' 
    
    # Metódo de classe
    @classmethod
    def listar_restaurantes(cls): # cls é uma convenção para referenciar a classe
        
        """Exibe uma lista formatada de todos os restaurantes."""
         
        print(f'{'Nome do restaurante'.ljust(30)}  {'Categoria'.ljust(33)}  {'    Status'.ljust(33)} {'     Media'.ljust(33)}')
        for restaurante in cls.restaurantes:
            print(f'Nome: {restaurante._nome.ljust(25)} | Categoria: {restaurante._categoria.ljust(25)} | Ativo: {restaurante.ativo.ljust(25)} | Média: {restaurante.media_avaliacoes}')
    
    
    @property
    def ativo(self):
        return "Ativo" if self._ativo else "Inativo"
    
    # Esse metodo é usado para os objetos da classe, ou seja, os objetos instanciados. Por isso não tem o @classmethod
    def alternar_ativacao(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        
        if nota < 0 or nota > 5:
            print(f'\nA nota do cliente {cliente} não foi registrada.')
            print('A nota deve ser entre 0 e 5\n')
        else:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao) 
        
    
    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacoes:
            return "Sem avaliações"
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_de_avaliacoes = len(self._avaliacoes)
        
        media = round(soma_das_notas / quantidade_de_avaliacoes, 1)
         
        return media
    
        
    def adicionar_item_cardapio(self, item):
        """Adiciona um item ao cardápio do restaurante."""
        
        # Verifica se o item é uma instância de ItemCardapio
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
           
    @property
    def exibir_cardapio(self):
        """Exibe o cardápio do restaurante."""
        print(f'Cardápio do restaurante {self._nome}:\n') 
        
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_tamanho'):
                mensagem = f'{i} - Nome: {item._nome} | Preço: R$ {item._preco:.2f} | Tamanho: {item._tamanho}'
                print(mensagem)
            else:
                mensagem = f'{i} - Nome: {item._nome} | Preço: R$ {item._preco:.2f} | Descrição: {item._descricao}'
                print(mensagem)
     
