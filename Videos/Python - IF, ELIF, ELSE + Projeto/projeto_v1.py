# Jogo de adivinhação para o usuário descobrir qual é o número definido.

# Definindo o número que deverá ser acertado.
numero = 32

# Pedido para o usuário informar um número.
chute = int(input('Qual você acha que é o número? '))

# Verificando se o usuário acertou.
if chute == numero:
  print('Parabéns, você acertou !!\n')
else:
  print('Que pena, você errou!\n')