from modelos.cardapio.item_cardapio import ItemCardapio

# aqui estamos importando a classe ItemCardapio do arquivo prato.py que está dentro da pasta cardapio, a famosa herança
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return f'{self._nome} - R$ {self._preco:.2f} - {self._descricao}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)
