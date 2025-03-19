"""
    Introdução às funções (deg) em Python
    Funções são trechos de código usados para replicar
determinada ação ao longo do seu código.
    Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
    Por padrão, funções em Python retornam none(nada)
"""

def imprimir():
    print('Várias')

imprimir() #Várias

def soma(a,b):
    print(a + b)

soma(10, 5) #15

def saudacao(name):
    print(f'Olá {name}')

saudacao('Douglas')
