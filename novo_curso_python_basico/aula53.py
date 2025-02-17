"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

#lista_enumerada = enumerate(lista) #aqui ele esgota a lista
#print(next(lista_enumerada))

#lista_enumerada = list(enumerate(lista))
#print(lista_enumerada)

#for item in list(enumerate(lista)): #se colocar o enumerate dentro do for, a lista não é esgotada
#    print(item)

#for item in enumerate(lista): 
#   indicie, nome = item
#   print(indicie, nome)
   
for indicie, nome in enumerate(lista): #outra opção de desempacotamento
   print(indicie, nome)