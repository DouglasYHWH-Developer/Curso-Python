primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'Primeiro valor {primeiro_valor} é maior que segundo valor {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'Segundo valor {segundo_valor} é maior que primeiro valor {primeiro_valor}')
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor} valores iguais {segundo_valor}')
else:
    print('Digite um número')