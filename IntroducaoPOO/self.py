class Quadrado():
    lados = 8
    def area(self): #self é referencia a uma instância
        return self.lados ** 2


quadrado = Quadrado() #Instancia da classe
print( quadrado.area()) #64('lados' foi encontrado na clase)
print(Quadrado.area(quadrado)) #64( equivalente a quadrade.area()) somente uma forma diferente de acessar os atributos
quadrado.lados = 10
print(quadrado.area()) #100 ('lados' foi encontrado na instancia )