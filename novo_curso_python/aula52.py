"""
Tipo tupla - Uma lista imutável
"""
nomes = 'Maria', 'Helena', 'Luiz' #tuplas são listas sem colchetes
print(nomes[0])

#convertendo lista em tuplas
nome = ['Maria', 'Helena', 'Luiz']
nomeTupla = tuple(nome)
print(nomeTupla)

#Convertendo uma tupla em lista
nome = list(nomeTupla)
print(nome)
"""
Uma tupla ( tuple ) em Python é uma sequência imutável de valores de 
qualquer tipo. Para criar uma tupla, lista-se uma sequência de valores 
separados por vírgulas e, opcionalmente, entre parênteses. 
Tuplas são úteis para representar registros (mas sem atribuir nomes aos campos).
"""