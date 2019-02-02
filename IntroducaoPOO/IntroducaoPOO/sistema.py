from IntroducaoPOO.IntroducaoPOO.heroi import Heroi

"""
#Objeto homem aranha
homem_aranha = Heroi() #instanciando objeto homem aranha
homem_aranha.lanca_teia = True #acessando uma propriedade do objeto
print(homem_aranha.voa) #imprimindo a propriedade de uma objeto
print(homem_aranha.lanca_teia)

#objeto he_man
he_man = Heroi()
he_man.possui_arma = True
he_man.lanca_teia  = False
he_man.voa         = False
he_man.frase_comum = "Eu tenho a força" #setando um valor para a propriedade
he_man.falar() #executando metodo falar importado de Heroi

arqueiro_verde = Heroi()
arqueiro_verde.possui_arma = True
arqueiro_verde.detalhar()
"""

# Heroi(nome,voa,possui_arma,lanca_teia,frase_comum)
homem_aranha = Heroi("Homem aranha",False,False,True,"")
print(homem_aranha.nome)
print(homem_aranha.voa)
print(homem_aranha.lanca_teia)
homem_aranha.detalhar()

he_man = Heroi("He-man",False,True,False,"Eu tenho a força!")
print(he_man.nome)
he_man.frase_comum = "Eu tenho a força !"
he_man.falar()
he_man.detalhar()
