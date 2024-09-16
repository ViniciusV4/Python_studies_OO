from abc import ABC, abstractmethod

class ItemCardapio(ABC): # essa classe é abstrata, ou seja, não pode ser instanciada
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return f"{self._nome} - R$ {self._preco:.2f}"
    
    # isso aqui é um método abstrato, ou seja, ele não tem implementação, quem herdar essa classe vai ter que implementar
    @abstractmethod
    def aplicar_desconto(self):
        pass
    
    