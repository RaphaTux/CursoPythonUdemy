class Veiculo :
    def __init__(self,qtd_rodas,motor):
        self.qtd_rodas = qtd_rodas
        self.motor = motor

    def ligar(self):
        if self.motor:
            print("Ligou")
        else:
            print("não tem motor")

    def desligar(self):
        if self.motor:
            print("  Desligou ")
        else:
            print("  Não tem motor")

    def andar(self):
        print("  O veiculo comecou a andar ")

    def parar(self):
        print("   O veiculo parou ")