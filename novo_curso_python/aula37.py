"""
Repetições
while(enquanto)
Executa uma ação enquantio uma condição for verdadeira
Loop infito -> Qaundo um códifo não tem fim
"""
contador = 0

while contador < 10:
    print(contador)
    contador = contador + 1

    if contador == 4:
        break
    
#while False: #nunca vai ser executado
#    print('EITA') 

print( 'Acabou')

