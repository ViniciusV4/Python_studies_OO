# 2 - Para imprimir a frase utilizando variáveis, temos algumas abordagens possíveis:
# Criação das Variáveis
nome = 'Lais'
idade = 24

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))

# 3 - Para imprimir a palavra ‘ALURA’ com cada letra em cada linha com a função print utilizando o parâmetro sep para especificar o separador entre os argumentos da seguinte forma:

print('A','L','U','R','A',sep='\n')

# 4 - Para imprimir o valor de pi arredondado, temos algumas possíveis abordagens:

pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))