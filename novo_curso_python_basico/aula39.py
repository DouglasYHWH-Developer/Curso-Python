"""
Iterando strings com while
"""
#       012345678910    
nome = 'Luiz Otávio' #Iteráveis


contador = 0
novo_nome = ''
while contador < len(nome):
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1

novo_nome += '*'
print(novo_nome)