#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Qual é o preço do produto? R$'))
desc = valor - (valor * 5 / 100)
print('O produto que custava R${:.2f}, aplicando a promoção de 5%, passa a custar R${:.2f}' .format(valor, desc))