'''
  Operação ternária(condicional de uma linha)
  <valor> if <condicional> else <outro valor>
'''
#condicao = 10 == 10
#variavel = 'valor' if condicao else 'Outro valor'
#print(variavel)
digito = 9
#novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)