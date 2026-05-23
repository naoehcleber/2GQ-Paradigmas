


#carrinho eh passado como uma lista de tuplas
def SepararProdutos (carrinho):
    total_itens = sum(len(t) for t in carrinho)
    
    produtos = list(map(lambda x: x[0], carrinho)) # pega o primeiro item de toda a lista de tuplas

def AssistirCompras(produtos):
    for produto in produtos:
        #checa se o produto esta presente em algum dos dicionarios de categoria 
        if produto["tipo"] == "saúde":
            pass
        elif produto["tipo"] == "higiene":
            pass
        elif produto["tipo"] == "limpeza":
            pass
    return

def main():
    #cria lista de produtos
    
    #seleção de produto

    

if __name__ == "__main__":
    main()


