def funcao_externa():

    b = 20
    a = 80

    print( f'Imprimeindo "b" em funcao_externa:{b}')
    print( f'Imprimindo "a" em função_externa: {a}')
    def funcao_interna():

        c = 30
        b = 25
        a = 70

        print(f"imprimindo 'C' em funcao_interna:{c}")
        print(f"imprimindo 'b' em funcaoInterna: {b}")
        print(f"Imprimindo 'a' em funcaçãoInterna:{a}")

    funcao_interna()
    print(f'Imprimindo "b" de novo em funcao_externa:{b}')

a = 10

print( f"Imprimindo 'a' no escopo global:{a}")

funcao_externa()
print(f"imprimindo 'a' de novo no escopo global:{a}")