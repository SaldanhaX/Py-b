#ENCONTRO O DOBRO, TRIPLO E RAIZ DE UM NÚMERO

n = int(input('Digite um número:'))
print('O dobro de {} vale {},' .format(n, (n**2)))
print('o triplo de {} vale {}, \ne a raiz quadrada de {} vale {:.2f}.' .format(n,(n**3), n, (n**(1/2))))