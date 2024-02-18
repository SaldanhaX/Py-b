#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Informe a temperatura em Cº:'))
far = cel * 1.8 + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF' .format(cel,far))