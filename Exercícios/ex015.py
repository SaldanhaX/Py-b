#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = float(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos Km você rodou? '))
total = (dia * 60) + (km * 0.15)
print('O valor total a pagar é de R${:.2f}' .format(total))