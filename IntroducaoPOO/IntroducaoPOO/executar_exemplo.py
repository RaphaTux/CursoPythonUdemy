from carro import Carro
from bicicleta import Bicicleta


bike = Bicicleta(2)

print(bike.motor)
print(bike.possui_guidao)
print(bike.qtd_rodas)
bike.ligar()
bike.andar()
bike.empinar()
bike.parar()
bike.desligar()

carro =  Carro(4)
carro.qtd_rodas

