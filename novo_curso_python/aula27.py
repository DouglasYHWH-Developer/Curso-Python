"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i - inicio
f - fatiamento
p - passo
[::] - 
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])# de 0 à 9 de forma invertida.
print(len(variavel))
print(variavel[0:9:1])
print(variavel[0:9:2])