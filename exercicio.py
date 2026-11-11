# Lista inicial de produtos: [ID, Nome, Preço]
produtos = [
    [1, "Caderno Universitário", 25.90],
    [2, "Caneta Esferográfica", 3.50],
    [3, "Mochila Escolar", 149.90],
    [4, "Estojo Simples", 18.00],
]

# 1. Imprimir os produtos
print("--- 1. LISTA INICIAL DE PRODUTOS ---")
for produto in produtos:
    print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2]:.2f}")

# 2. Localizar um produto pelo ID
id_busca = int(input("\n2. Digite o ID do produto que deseja localizar: "))
encontrado = False

for produto in produtos:
    if produto[0] == id_busca:
        print(
            f"Produto encontrado: {produto[1]} (Preço: R$ {produto[2]:.2f})"
        )
        encontrado = True
        break

if not encontrado:
    print("Produto não encontrado na lista.")

# 3. Remover um produto pelo ID
id_remover = int(input("\n3. Digite o ID do produto que deseja remover: "))
removido = False

for produto in produtos:
    if produto[0] == id_remover:
        produtos.remove(produto)
        print(f"Produto '{produto[1]}' removido com sucesso!")
        removido = True
        break

if not removido:
    print("ID não encontrado. Nenhum produto foi removido.")

# 4. Imprimir novamente a lista depois da remoção
print("\n--- 4. LISTA ATUALIZADA APÓS REMOÇÃO ---")
for produto in produtos:
    print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2]:.2f}")

# 5. Cadastrar um novo produto usando append()
print("\n--- 5. CADASTRAR NOVO PRODUTO ---")
novo_id = int(input("Digite o ID do novo produto: "))
novo_nome = input("Digite o nome do novo produto: ")
novo_preco = float(input("Digite o preço do novo produto: "))

produtos.append([novo_id, novo_nome, novo_preco])
print(f"Produto '{novo_nome}' cadastrado com sucesso!")

# 6. Alterar o preço de um produto pelo ID
print("\n--- 6. ALTERAR PREÇO DE UM PRODUTO ---")
id_alterar = int(
    input("Digite o ID do produto que deseja alterar o preço: ")
)
alterado = False

for produto in produtos:
    if produto[0] == id_alterar:
        novo_valor = float(input(f"Digite o novo preço para '{produto[1]}': "))
        produto[2] = novo_valor
        print("Preço atualizado com sucesso!")
        alterado = True
        break

if not alterado:
    print("ID não encontrado. Nenhum preço foi alterado.")

# Exibição final para conferir todas as mudanças
print("\n--- LISTA FINAL DE PRODUTOS ---")
for produto in produtos:
    print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2]:.2f}")
