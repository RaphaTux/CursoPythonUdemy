"""
  Crie um programa que solicite ao usuário que informe o valor de seu salário, o valor do salário mínimo e sua idade.
  Compare se o valor do salário é maior que dois salários mínimos E se a idade informada é maior que 18 usando operadores
  lógicos e relacionais. Imprima no final: "O resultado foi X", sendo que X será "True" ou "False".
"""

dSalario    = float( input( 'Informe seu dalario ' ))
sSalarioMin = float( input( 'Informe o valor do salario minimo ' ))
iIdade      = int(   input( 'Informe a sua idade ' ))
bCondicao   = dSalario > 2*sSalarioMin and iIdade > 18
print( 'O resultado foi ',bCondicao )