"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

#cpf = '74682489070'
#cpf = '746.824.890-70'\
#   .replace('.','')\
#   .replace(' ','')\
#   .replace('-','')
#print(cpf)

import random

nove_digitos = ''

for i in range(9):
 nove_digitos += str(random.randint(0,9))

indice_1 = 10

resultado_indice_1 = 0
for digito in nove_digitos:
   resultado_indice_1 += int(digito) * indice_1
   indice_1 -= 1
digito_1 = (resultado_indice_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1 )
indice_2 = 11

resultado_indicie_2 = 0
for digito in dez_digitos:
   resultado_indicie_2 += int(digito) * indice_2
   indice_2 -= 1
digito_2 = (resultado_indicie_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 10 else 0

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'
print(novo_cpf)

