""" Calculadora com while"""
 # solução do professor
while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Qual conta deseja fazer? ex: (+ - / *) : ')
    
    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
            print('Um ou ambos os números digitados são inválidos.')
            continue
    
    operadores_permitidos = '(+ - / *) '

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
         print('Digite apenas um operador')
         continue

    if operador == '+':
        resultado = int(numero_1) + int(numero_2)
        print(f'{numero_1} + {numero_2} = {resultado}')
    
    elif operador == '-':
        resultado = int(numero_1) - int(numero_2)
        print(f'{numero_1} - {numero_2} = {resultado}')
        
    elif operador == '/':
        resultado = float(numero_1) / float(numero_2)
        print(f'{numero_1} / {numero_2} = {resultado}')
        
    elif operador == '*':
        resultado = int(numero_1) * int(numero_2)
        print(f'{numero_1} * {numero_2} = {resultado}')

    sair = input('Quer sair? [s]im? ').lower().startswith('s')
        
    if sair is True:
            print()




"""
numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')
operador = input('Qual conta deseja fazer? ex: (+ - / *) : ')


while operador == '+':
    resultado = int(numero_1) + int(numero_2)
    print(f'{numero_1} + {numero_2} = {resultado}')
    break
while operador == '-':
    resultado = int(numero_1) - int(numero_2)
    print(f'{numero_1} - {numero_2} = {resultado}')
    break
while operador == '/':
    resultado = float(numero_1) / float(numero_2)
    print(f'{numero_1} / {numero_2} = {resultado}')
    break
while operador == '*':
    resultado = int(numero_1) * int(numero_2)
    print(f'{numero_1} * {numero_2} = {resultado}')
    break
"""