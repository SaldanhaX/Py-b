#CONVERSOR DE MOEDAS

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real /4.92
euro = real / 5.25
iene = real / 0.034
print('Com R${:.2f} você pode comprar US${:.2f}, EU${:.2f} e Y${:.2f}'.format(real,dolar,euro,iene))