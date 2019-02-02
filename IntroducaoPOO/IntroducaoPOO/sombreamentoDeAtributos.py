class Ponto():
    x = 25
    y = 75

#insanciando um objeto
p = Ponto()

print(p.x)
print(p.y)

p.x = 12
print(p.x) #acessando o atributo do objeto P
print(Ponto.x) #Acessando atributo da classe

del p.x
print(p.x)

p.z = 10

#print(Ponto.z)q
