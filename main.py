



def AssistirCompras(produtos, estoque):
    for produto in produtos:
        #checa se o produto esta presente em algum dos dicionarios de categoria 
        if produto["tipo"] == "saúde":
            print(estoque["tipo":"saúde"])
        elif produto["tipo"] == "higiene":
            print(estoque["tipo":"higiene"])
        elif produto["tipo"] == "limpeza":
            print(estoque["tipo":"limpeza"])
    return

def main():
    #cria lista de produtos
    disponiveis = [
        {"produto": "sabonete", "tipo": "higiene"},
        {"produto": "pasta de dente", "tipo": "higiene"},
        {"produto": "desodorante", "tipo": "higiene"},
        {"produto": "antibiotico", "tipo": "saúde"},
        {"produto": "detergente", "tipo": "limpeza"}
    ]
    carrinho = []
    #seleção de produto
    while(True):
        print("Digite seu produto: ")
        print(disponiveis["produto"])
        print("Aperte 0 para sair")
        escolha = input("Digite aqui: ")
        qntd = int(input("Quantos ? "))
        if escolha != "0":
            carrinho.push(escolha, qntd)
        else :
            print("Aqui está o seu carrinho, deseja adicionar mais algo ? ")
            opcao = input("1 - SIM. \n 0 - SAIR.")
            if opcao == "0":
                break
            else:
                continue
        
    produtos = list(map(lambda x: x[0], carrinho)) # pega o primeiro item de toda a lista de tuplas
    AssistirCompras(produtos)

    

if __name__ == "__main__":
    main()


