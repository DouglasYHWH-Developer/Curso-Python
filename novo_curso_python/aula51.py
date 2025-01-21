"""
Introdução ao desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome2)

name1, name2, name3 = ['Naruto', 'Sasuke', 'Kakashi']
print(name1, name2, name3)

# resto da lista
names1, *resto = ['Naruto', 'Sasuke', 'Kakashi']
print(names1, resto)

_, nms2, *_ = ['Naruto', 'Sasuke', 'Kakashi']
print(nms2)