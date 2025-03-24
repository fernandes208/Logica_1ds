# Solicitar o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Classificar o produto e informar a prateleira correspondente
if preco <= 100:
    print("Este produto é de baixo custo e deve ser guardado na prateleira correspondente.")
elif 101 <= preco <= 500:
    print("Este produto é de médio custo e deve ser guardado na prateleira correspondente.")
else:
    print("Este produto é de alto custo e deve ser guardado na prateleira correspondente.")
