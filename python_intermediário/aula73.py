"""
Higher Order Function
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao,'Bom dia', 'Douglas')
)
print(
    executa(saudacao,'Bom dia', 'Toguro')
)


