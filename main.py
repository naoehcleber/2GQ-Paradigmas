from functools import reduce

ESTOQUE = [
    {"id": "1", "produto": "sabonete", "tipo": "higiene", "preco": 3.50, "disponivel": True},
    {"id": "2", "produto": "pasta de dente", "tipo": "higiene", "preco": 5.00, "disponivel": True},
    {"id": "3", "produto": "desodorante", "tipo": "higiene", "preco": 12.00, "disponivel": True},
    {"id": "4", "produto": "carregador", "tipo": "eletrônico", "preco": 45.00, "disponivel": True},
    {"id": "5", "produto": "mouse sem fio", "tipo": "eletrônico", "preco": 120.00, "disponivel": True},
    {"id": "6", "produto": "detergente", "tipo": "limpeza", "preco": 2.50, "disponivel": True},
    {"id": "7", "produto": "desinfetante", "tipo": "limpeza", "preco": 8.00, "disponivel": False}
]

def calcular_subtotal(item):
    return item['preco'] * item['quantidade']

def obter_produto_por_id(id_produto, estoque):
    resultados = list(filter(lambda p: p['id'] == id_produto, estoque))
    if resultados:
        return resultados[0]
    else: 
        return None

def recomendar_por_categoria(item_carrinho, estoque, carrinho_valido):
    categoria = item_carrinho['tipo']
    
    ids_no_carrinho = list(map(lambda item: item['id'], carrinho_valido))
    
    recomendacoes = list(filter(lambda p: p['tipo'] == categoria and p['id'] not in ids_no_carrinho and p['disponivel'], estoque))
    
    if recomendacoes:
        return list(map(lambda p: p['produto'], recomendacoes))
    else:
        return ["Nao ha mais itens para recomendar"]

def processar_carrinho(carrinho_bruto, estoque):
    carrinho_enriquecido = list(map(lambda item: {**obter_produto_por_id(item['id'], estoque), "quantidade": item['quantidade']}, carrinho_bruto))

    carrinho_valido = list(filter(lambda item: item['disponivel'] and item['quantidade'] > 0, carrinho_enriquecido))

    listas_recomendacoes = map(lambda item: recomendar_por_categoria(item, estoque, carrinho_valido), carrinho_valido)
    recomendacoes = list(set(reduce(lambda acc, lista: acc + lista, listas_recomendacoes, [])))

    total_compra = reduce(lambda acumulador, item: acumulador + calcular_subtotal(item), carrinho_valido, 0.0)

    return carrinho_valido, recomendacoes, total_compra

def formatar_menu(estoque):
    linhas = map(lambda p: f"[{p['id']}] {p['produto'].title()} (R$ {p['preco']:.2f})", estoque)
    return "\n".join(linhas)

def coletar_carrinho_recursivo(estoque, carrinho_atual=None):
    if carrinho_atual is None:
        carrinho_atual = []
        
    print("\n--- PRODUTOS DISPONÍVEIS ---")
    print(formatar_menu(estoque))
    print("[0] Finalizar compra")
    
    escolha = input("\nDigite o ID do produto: ")
    
    if escolha == "0":
        return carrinho_atual
        
    produto_valido = obter_produto_por_id(escolha, estoque)
    
    if not produto_valido:
        print("Produto inválido. Tente novamente.")
        return coletar_carrinho_recursivo(estoque, carrinho_atual)
        
    if not produto_valido['disponivel']:
        print("Produto indisponivel")
        return coletar_carrinho_recursivo(estoque, carrinho_atual)
        
    qntd_str = input(f"Quantos itens de {produto_valido['produto'].title()}? ")
    if qntd_str.isdigit():
        qntd = int(qntd_str)
    else: 
        qntd = 0
    
    novo_carrinho = carrinho_atual + [{"id": escolha, "quantidade": qntd}]
    
    return coletar_carrinho_recursivo(estoque, novo_carrinho)

def main():
    print("Bem-vindo ao carrinho de Compras!")
    
    carrinho_bruto = coletar_carrinho_recursivo(ESTOQUE)
    
    if not carrinho_bruto:
        print("\nCarrinho vazio. Encerrando sistema.")
        return

    carrinho_valido, recomendacoes, total = processar_carrinho(carrinho_bruto, ESTOQUE)
    
    print("\n===============================")
    print("       RESUMO DA COMPRA")
    print("===============================")
    
    linhas_resumo = map(lambda item: f"{item['quantidade']}x {item['produto'].title()} - Subtotal: R$ {calcular_subtotal(item):.2f}", carrinho_valido)
    print("\n".join(linhas_resumo))
    
    print("\n--- RECOMENDAÇÕES ---")
    linhas_recomendacao = map(
        lambda r: f"- {r.title()}" 
        if r != "nao ha mais itens para recomendar" 
        else r, recomendacoes)
    texto_recomendacoes = "\n".join(linhas_recomendacao)

    if texto_recomendacoes:
        print(texto_recomendacoes)

    print(f"\nTOTAL A PAGAR: R$ {total:.2f}")

if __name__ == "__main__":
    main()