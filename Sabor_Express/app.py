import os

restaurantes = [{'nome':'pizza', 'categoria':'italiana', 'ativo':True}, {'nome':'hamburguer', 'categoria':'americana', 'ativo':True}, {'nome':'japones', 'categoria':'japonesa', 'ativo':True}]

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) * 2)
    print(linha)
    print(f'    {texto}')
    print(linha)
    
def voltar_menu_principal():
    input('Pressione qualquer tecla para voltar para o menu principal.')
    main()

def exbindo_nome_programa():
    # fonte: https://fsymbols.com/generators/
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """)

def exbir_opcoes():
    print('Escolha uma opção:\n')
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando aplicação.')
    
    voltar_menu_principal()
    
def cadastrar_restaurante():
    exibir_subtitulo('Cadastrando restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante:\n ')
    categoria_restaurante = input('Digite a categoria do restaurante:\n ')
    
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
    
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n') 
    
    voltar_menu_principal()
    
def listar_restaurante():
    exibir_subtitulo('Listando restaurante')
    
    i = 0
    for restaurante in restaurantes:
        i += 1
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = 'ativo' if restaurante['ativo'] else 'inativo'
        print(f'Restaurante número {i}: \n Nome: {nome_restaurante}\n Categoria: {categoria_restaurante}\n Status: {status_restaurante}\n')
        

    voltar_menu_principal()
    
def altera_estado_restaurante():
    exibir_subtitulo('Ativando restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar:\n ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(f'O restaurante {nome_restaurante} foi ativado com sucesso!\n' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!\n')
            
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.\n')
    
    voltar_menu_principal()
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
                
            case 2:
                print(f'Opção escolhida: {opcao_escolhida}')
                listar_restaurante()
                
            case 3:
                print(f'Opção escolhida: {opcao_escolhida}')
                altera_estado_restaurante()
                print('Ativando restaurante')
                
            case 4:
                print(f'Opção escolhida: {opcao_escolhida}')
                print('Saindo')
                
            case _:
                finalizar_app()
                
    except ValueError as e:
        exibir_subtitulo('Opção inválida. Tente novamente.')
        print(f'Erro: {e}')
        escolher_opcao()
    
def main():
    exbindo_nome_programa()
    exbir_opcoes()
    escolher_opcao()
        
    
if __name__ == '__main__':
    main()