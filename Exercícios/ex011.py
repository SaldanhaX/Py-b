#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
#tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Qual a largura da sua parede?'))
altura = float(input('Qual a altura da sua parede?'))
area = largura * altura
tinta = area / 2

print('Sua parede tem uma dimensão de {}mx{}m e sua área é de {:.2f}m²,.\nSendo assim, para pintar esta parede você vai precisar de {}L de tinta.' .format(largura,altura,area,tinta))
