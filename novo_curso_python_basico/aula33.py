"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')
numero_int = int(numero)
e_inteiro = True

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {numero_int} é {par_impar_texto}')
else:
    print('Você não digititou um número inteiro')
"""
if numero_int % 2 == 0 and e_inteiro:
    print('número par')
elif numero_int % 2 != 0 and e_inteiro:
    print('número ímpar')
elif numero == float(numero):
    print('Não é um número inteiro')
else:
    print('Digite um número')
    """
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Quantas horas? ')

try:
    hora = int(hora)

    if hora <= 11:
        print('Bom dia')
    elif hora <= 17:
        print('Boa tarde')
    elif hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor digite apenas números inteiros')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
primeiro_nome = input('Digite seu primeiro nome: ')

if len(primeiro_nome) <= 4:
    print('Seu nome é muito curto')
elif len(primeiro_nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')






