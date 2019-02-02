from pessoa_fisica import Pessoa_fisica
from pessoa_juridica import Pessoa_juridica

pf = Pessoa_fisica( "012.231.597-16","fulano",40 )
pj = Pessoa_juridica("01.111.111/0001-88","Loja teste",5)

print(pf.nome)
print(pf.cpf)
print(pf.idade)