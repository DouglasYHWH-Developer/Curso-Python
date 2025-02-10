'''
    Desempacotamento em chamadas
de métodos e funções
'''
string = 'ABCD'
lista = [ 'Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

#p, b, *_, u = lista
#print(p, u)
for nome in lista:
    print(nome, end =' ')

print(*lista)
print(*string)