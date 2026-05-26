# Simulação de Carrinho de Compras 

Um sistema interativo de carrinho de compras para loja virtual, executado via terminal. Este projeto foi desenvolvido em **Python** e tem como foco a aplicação prática de conceitos de **programação funcional**.
---

##  Funcionalidades

* **Catálogo Interativo:** Exibe a lista de produtos com IDs, nomes formatados e preços.
* **Controle de Estoque:** Valida a entrada do usuário em tempo real, impedindo a adição de produtos com IDs inválidos ou que estejam marcados como indisponíveis (`disponivel: False`).
* **Sistema de Recomendações:** Analisa as categorias dos produtos adicionados ao carrinho e sugere itens relacionados, filtrando automaticamente opções que o usuário já escolheu comprar.
* **Resumo de Compras:** Gera um extrato detalhado contendo a quantidade de cada item, o subtotal e o valor total final da compra.
* **Fluxo Recursivo:** A interação contínua com o usuário para adicionar múltiplos itens é controlada inteiramente por recursividade, sem o uso de laços `while` ou `for`.

---

##  Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 3.x
* **Paradigma Funcional:**
  * Uso intensivo de **funções lambda** (anônimas).
  * **`map`**: Para transformação de dados (ex: formatação de strings e extração de propriedades).
  * **`filter`**: Para buscas e validações (ex: encontrar produtos por ID e verificar disponibilidade).
  * **`reduce`** (da biblioteca `functools`): Para agregação de dados (ex: cálculo do valor total e achatamento de listas de recomendações).

---

##  Como Executar

1. Certifique-se de ter o **Python 3.x** instalado no seu ambiente.
2. Clone o repositório ou faça o download do arquivo `.py` (ex: `carrinho.py`).
3. Abra o terminal e navegue até o diretório do arquivo.
4. Execute o script com o comando:

   ```bash
   python carrinho.py
