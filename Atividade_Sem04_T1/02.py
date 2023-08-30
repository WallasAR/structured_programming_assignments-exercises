#  02. Escreva um programa de leia o preço de um produto e mostre na tela o valor com 10% de desconto arredondado para duas casas decimais.

price = float(input("Digite o preço do produto: R$ "))

desc = price * 0.90

print(f"Com desconto de 10% o produto passa a ser R$ {desc:.2f}")