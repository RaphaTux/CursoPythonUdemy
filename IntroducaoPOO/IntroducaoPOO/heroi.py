class Heroi:

  #classe de herois

  """

  #Atributos
  voa = False
  possui_arma = False
  lanca_teia = False
  frase_comum = ""

  #metodos
  def falar(self):
      print(self.frase_comum)

  def detalhar(self):
    if self.voa:
        print( "O heroi voa." )
    if self.possui_arma:
        print( "O heroi possui uma arma" )
    if self.lanca_teia:
        print( "O heroi Lança teia" )

"""
  def __init__ (self,nome,voa,possui_arma,lanca_teia,frase_comum):

     print( "Executando init...")
     self.nome = nome
     self.voa = voa
     self.possui_arma = possui_arma
     self.lanca_teia = lanca_teia
     self.frase_comum = frase_comum

  def falar (self):

    if self.frase_comum:
      print(self.frase_comum)
    else:
      print( "O heroi não possui frase comum" )

  def detalhar(self):

    self.nome

    if self.voa:
      print("O heroi voa")
    else:
      print( "O heroi não voa")

    if self.possui_arma:
      print( "O heroi possui arma")
    else:
      print( "O heroi não possui arma " )

    if self.lanca_teia:
      print( "O heroi lanca teia " )
    else:
      print( "O heroi não lança teia " )
