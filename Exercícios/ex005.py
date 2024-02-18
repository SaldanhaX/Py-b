#CRIE UM PROGRAMA QUE LEIA UM NÚMERO E MOSTRE SEU ANTECESSOR E SEU SUCESSOR:

num = int(input('Digite um número:'))
ant = num - 1
suc = num + 1
#print('Analisando seu número "{}", seu antecessor é {} e seu sucessor é {}.' .format(num, ant, suc))
#outra resolução vvv
print ('Analisando seu número "{}", seu antecessor é {} e seu sucessor é {}.' .format (num, (num - 1), (num + 1)))