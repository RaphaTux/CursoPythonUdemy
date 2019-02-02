from herancaClasseBase import Classe_base

class Classe_derivada1(Classe_base):
    def __init__(self,valor1,valor2):
        print( "Método __init__ da classe derivada1" )
        self.valor1 = valor1
        self.valor2 = valor2
        super().__init__(valor1,valor2)

    def imprimir (self,texto):
        print(texto)
