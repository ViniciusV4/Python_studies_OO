import os
from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


bebida_suco = Bebida('Suco de Laranja', 5.0, '300ml')
bebida_suco.aplicar_desconto()
prato_feijoada = Prato('Feijoada', 25.0, 'Feijoada completa com arroz, farofa e couve.')
prato_feijoada.aplicar_desconto()

restaurante_da_esquina = Restaurante('Da Esquina', 'Bar')
restaurante_da_esquina.alternar_ativacao()
restaurante_da_esquina.receber_avaliacao('João', 5)
restaurante_da_esquina.adicionar_item_cardapio(bebida_suco)
restaurante_da_esquina.adicionar_item_cardapio(prato_feijoada)

def main():
    os.system('cls')
    print('---------------------------')
    print('Bem-vindo ao Sabor Express!')
    print('---------------------------\n')
  
    restaurante_da_esquina.exibir_cardapio

if __name__ == "__main__":
    main()