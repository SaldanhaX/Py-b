#CONVERSOR DE MEDIDAS
#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O CONVERTA EM CENTÍMETROS E MILÍMETROS

metros = float(input('Digite os metros a serem convertidos:'))
cm = metros * 100
ml = metros * 1000

print('A medida de {}m corresponde a {:.0f}cm e a {:.0f}mm' .format(metros,cm,ml))