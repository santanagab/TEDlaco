# TED: Condição + Laço
# Elabore um Jogo de Adivinhação, no qual o usuário deverá acertar o número escolhido pelo programa, entre 1 e 100. Regras:
# O programa deverá avisar quando o palpite estiver acima ou abaixo da resposta correta;
# Quando o usuário acertar a resposta, o programa deve informar quantas tentativas o usuário usou para alcançar o número correto.

from random import randint
computador = randint(1, 100)
print('Tente adivinhar o número!')
acerto = False
tentativa = 0
while not acerto:
    palpite = int(input('Qual número pensei? '))
    tentativa += 1     # contador dos palpites
    if palpite == computador:
        acerto = True
    else:
        if palpite < computador:
            print('Errou! O número que pensei é maior!')
        elif palpite > computador:
            print('Errou! O número que pensei é menor!')
print(f'Você acertou em {tentativa} tentativas!')