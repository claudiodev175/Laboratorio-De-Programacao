# 1. Criar uma lista vazia
lista_compras = []

# 2. Adicionar os itens à lista de compras
lista_compras.append("arroz")
lista_compras.append("feijão")
lista_compras.append("macarrão")

# 3. João percebe que esqueceu de adicionar um item. Coloque-o na segunda posição
lista_compras.insert(1, "leite")

# 4. Exibir a lista de compras completa e mostrar o terceiro item
print("Lista de compras completa:", lista_compras)
print("Terceiro item da lista:", lista_compras[2])

# 5. João decide que não precisa mais comprar um item (vamos remover "feijão")
lista_compras.remove("feijão")

# 6. Ele também decide retirar o último item da lista
lista_compras.pop()

# 7. Substituir o primeiro item da lista por "abacate"
lista_compras[0] = "abacate"

# 8. Mostrar a lista atualizada e exibir cada item individualmente
print("\nLista atualizada:")
for item in lista_compras:
    print("Item:", item)

# 9. Organizar a lista em ordem alfabética
lista_compras.sort()
print("\nLista em ordem alfabética:", lista_compras)
