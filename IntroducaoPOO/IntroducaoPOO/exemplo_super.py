class Pai():
    def __init__(self):
        print( "Construtor da classe pai " )


class Mae():
    def __init__(self):
        print( "Contrutor da clase Mãe" )

class Filha(Pai): #criando classe filha herdando do Pai
    def __init__(self):
         #Pai.__init__(self) #sempre vai imprimir o construtor da classe pai pois esta fixado
         super().__init__() #com o super ele imprime o construtor da classe base independente de qual seja
                            #a classe que a sub classe herdou


filha = Filha()
