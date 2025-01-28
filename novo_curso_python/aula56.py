"""
split e join com list e str
split - divide a uma string
join - une uma string
strip() -  retira os espaços
rstrip() -  retira os espaços da direita
lstrip() -  retira os espaços da esquerda
"""
frase = '   Olha só que   ,   coisa interessante'
lista_frase_crua = frase.split(',')

lista_frase = []
for i, frase in enumerate(lista_frase_crua):
    lista_frase.append(lista_frase_crua[i].strip())

print(lista_frase_crua)
print(lista_frase )

frases_unidas = '-'.join(lista_frase)
print(frases_unidas)