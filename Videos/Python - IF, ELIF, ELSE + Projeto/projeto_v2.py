# Jogo de adivinhação para o usuário descobrir qual é o número definido.

# Definindo o número que deverá ser acertado.
numero = 32

# Pedido para o usuário informar um número.
chute = int(input('Qual você acha que é o número? '))

# Verificando se o usuário acertou ou se chutou baixo ou alto.
if chute == numero:
  print('Parabéns, você acertou !!\n')
elif chute < numero:
  print('Você chutou baixo.\n')
else:
  print('Você chutou alto.\n')