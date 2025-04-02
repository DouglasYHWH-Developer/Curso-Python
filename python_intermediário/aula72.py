# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

mult_1 = mult(2, 2, 2, 2)
print(mult_1)

# Crie uma função que fala se o número é par ou ímpar
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    par = numero % 2 == 0
    if par:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    

print(par_impar(3))
print(par_impar(36))
print(par_impar(7))
