"""
Repetições
while(enquanto)
Executa uma ação enquantio uma condição for verdadeira
Loop infito -> Qaundo um códifo não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}.')

    if nome == 'sair':
        break

print('acabou')