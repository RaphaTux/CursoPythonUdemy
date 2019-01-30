#casas decimais e arredondamento
valor_unitario = 165.78
print( "%f" %valor_unitario)
print( "%.f" %valor_unitario)
print( "%.1f" %valor_unitario)
print( "%.2f" %valor_unitario)

#aparecendo o sinal de porcentagem
percent = 17.5
frase = 'a taxa de juros é de %.2f%%' % percent
print(frase)

#usando format
nome   = 'Jose da Silva'
idade  = 50
filhos = 3
frase = "{} tem {} anos de idade e tem {} filhos ".format(nome,idade,filhos)
print(frase)

#usando indice
frase = 'Olá .eu vou viajar de {2}'.format( 'bicilcleta','moto','trem','carro' )
print(frase)

#usuando f String
nome = "Messi"
print('o nome dele é {nome}')
