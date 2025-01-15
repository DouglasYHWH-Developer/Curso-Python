"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

#      +01234
#      -54321
string = 'ABCDE' # 5 caracteres cadeia de caracteres
#print(bool(lista)) # false
#print(lista, type(lista))

#         0     1         2         3    4
#        -5    -4        -3        -2   -1  
lista = [123, True, 'Luiz Otávio', 1.2, []]#lista = [] list vazia/ string vazia
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
"""
lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])
lista.append('Douglas') 
nome = lista.pop()
lista.append(1233)
del lista[-1]
lista.insert(0, 66)
#lista.clear()
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista.extend(lista_b)
print(lista_c) # não vai retornar nada, apenas criar a extensão

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() #copiou a lista 'a' para lista 'b'

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)