from functools import reduce

ESTOQUE = [
    {"id": "1", "produto": "sabonete", "tipo": "higiene", "preco": 3.50, "disponivel": True},
    {"id": "2", "produto": "pasta de dente", "tipo": "higiene", "preco": 5.00, "disponivel": True},
    {"id": "3", "produto": "desodorante", "tipo": "higiene", "preco": 12.00, "disponivel": True},
    {"id": "4", "produto": "antibiotico", "tipo": "saúde", "preco": 45.00, "disponivel": True},
    {"id": "5", "produto": "vitamina c", "tipo": "saúde", "preco": 20.00, "disponivel": True},
    {"id": "6", "produto": "detergente", "tipo": "limpeza", "preco": 2.50, "disponivel": True},
    {"id": "7", "produto": "desinfetante", "tipo": "limpeza", "preco": 8.00, "disponivel": False}
]

def calcular_subtotal(item):
    return item['preco'] * item['quantidade']

def obter_produto_por_id(id_produto, estoque):
    resultados = list(filter(lambda p: p['id'] == id_produto, estoque))
    return resultados[0] if resultados else None

def recomendar_por_categoria(item_carrinho, estoque):
    categoria = item_carrinho['tipo']
    nome_produto = item_carrinho['produto']
    
    recomendacoes = list(filter(
        lambda p: p['tipo'] == categoria and p['produto'] != nome_produto and p['disponivel'], 
        estoque
    ))
    
    return recomendacoes[0]['produto'] if recomendacoes else "Sem recomendação"

def processar_carrinho(carrinho_bruto, estoque):
    carrinho_enriquecido = list(map(
        lambda item: {**obter_produto_por_id(item['id'], estoque), "quantidade": item['quantidade']},
        carrinho_bruto
    ))

    carrinho_valido = list(filter(
        lambda item: item['disponivel'] and item['quantidade'] > 0, 
        carrinho_enriquecido
    ))

    recomendacoes = list(set(map(
        lambda item: recomendar_por_categoria(item, estoque), 
        carrinho_valido
    )))

    total_compra = reduce(
        lambda acumulador, item: acumulador + calcular_subtotal(item), 
        carrinho_valido, 
        0.0
    )

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
        
    qntd_str = input(f"Quantos itens de {produto_valido['produto'].title()}? ")
    qntd = int(qntd_str) if qntd_str.isdigit() else 0
    
    novo_carrinho = carrinho_atual + [{"id": escolha, "quantidade": qntd}]
    
    return coletar_carrinho_recursivo(estoque, novo_carrinho)

def main():
    while(1):    
        print("Bem-vindo ao Sistema Funcional de Compras!")
        
        carrinho_bruto = coletar_carrinho_recursivo(ESTOQUE)
        
        if not carrinho_bruto:
            print("\nCarrinho vazio. Encerrando sistema.")
            return

        carrinho_valido, recomendacoes, total = processar_carrinho(carrinho_bruto, ESTOQUE)
        
        print("\n===============================")
        print("      RESUMO DA COMPRA")
        print("===============================")
        
        linhas_resumo = map(lambda item: f"{item['quantidade']}x {item['produto'].title()} - Subtotal: R$ {calcular_subtotal(item):.2f}", carrinho_valido)
        print("\n".join(linhas_resumo))
        
        print(f"\nTOTAL A PAGAR: R$ {total:.2f}")
        
        print("\n--- RECOMENDAÇÕES ---")
        recomendacoes_validas = filter(lambda r: r != "Sem recomendação", recomendacoes)
        linhas_recomendacao = map(lambda r: f"- {r.title()}", recomendacoes_validas)
        texto_recomendacoes = "\n".join(linhas_recomendacao)
        
        print(texto_recomendacoes if texto_recomendacoes else "Sem recomendações no momento.")

if __name__ == "__main__":
    main()