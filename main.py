import os
import random
import locale
from time import sleep

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

linha1 = ['_', '|', '_', '|', '_']
linha2 = ["_", "|", "_", "|", "_"]
linha3 = [" ", "|", " ", "|", " "]
jogadas = []
ganhou = False
jaganhou = ""


def menu():
    print('Digite 1 Para: 1 Jogador')
    print('Digite 2 Para: 2 Jogadores')
    print('Digite 3 Para: Sair')
    opc = input('Digite uma opção: ')
    return opc


def imagem_jogo():
    print("")
    print(f'{linha1[0]}{linha1[1]}{linha1[2]}{linha1[3]}{linha1[4]}')
    print(f'{linha2[0]}{linha2[1]}{linha2[2]}{linha2[3]}{linha2[4]}')
    print(f'{linha3[0]}{linha3[1]}{linha3[2]}{linha3[3]}{linha3[4]}')


def func_ganhou():
    global ganhou
    if linha1[0] == "x" and linha1[2] == "x" and linha1[4] == "x":
        ganhou = True
        return "x"
    elif linha2[0] == "x" and linha2[2] == "x" and linha2[4] == "x":
        ganhou = True
        return "x"
    elif linha3[0] == "x" and linha3[2] == "x" and linha3[4] == "x":
        ganhou = True
        return "x"
    elif linha1[0] == "x" and linha2[0] == "x" and linha3[0] == "x":
        ganhou = True
        return "x"
    elif linha1[2] == "x" and linha2[2] == "x" and linha3[2] == "x":
        ganhou = True
        return "x"
    elif linha1[4] == "x" and linha2[4] == "x" and linha3[4] == "x":
        ganhou = True
        return "x"
    elif linha1[0] == "x" and linha2[2] == "x" and linha3[4] == "x":
        ganhou = True
        return "x"
    elif linha1[4] == "x" and linha2[2] == "x" and linha3[0] == "x":
        ganhou = True
        return "x"
    elif linha1[0] == "o" and linha1[2] == "o" and linha1[4] == "o":
        ganhou = True
        return "o"
    elif linha2[0] == "o" and linha2[2] == "o" and linha2[4] == "o":
        ganhou = True
        return "o"
    elif linha3[0] == "o" and linha3[2] == "o" and linha3[4] == "o":
        ganhou = True
        return "o"
    elif linha1[0] == "o" and linha2[0] == "o" and linha3[0] == "o":
        ganhou = True
        return "o"
    elif linha1[2] == "o" and linha2[2] == "o" and linha3[2] == "o":
        ganhou = True
        return "o"
    elif linha1[4] == "o" and linha2[4] == "o" and linha3[4] == "o":
        ganhou = True
        return "o"
    elif linha1[0] == "o" and linha2[2] == "o" and linha3[4] == "o":
        ganhou = True
        return "o"
    elif linha1[4] == "o" and linha2[2] == "o" and linha3[0] == "o":
        ganhou = True
        return "o"


def jogador_1():
    jogada = int(input('Digite uma posição de de 1 a 9 para marcar: '))
    if jogada in jogadas:
        while jogada in jogadas:
            jogada = int(input('Posição já marcada, digite uma posição de 1 a 9 para marcar: '))
    jogadas.append(jogada)
    if jogada <= 3:
        if jogada == 1:
            linha1[0] = "x"
        elif jogada == 2:
            linha1[2] = "x"
        elif jogada == 3:
            linha1[4] = "x"
    if jogada <= 6:
        if jogada == 4:
            linha2[0] = "x"
        elif jogada == 5:
            linha2[2] = "x"
        elif jogada == 6:
            linha2[4] = "x"
    if jogada <= 9:
        if jogada == 7:
            linha3[0] = "x"
        elif jogada == 8:
            linha3[2] = "x"
        elif jogada == 9:
            linha3[4] = "x"


def jogador_maquina():
    jogada = random.randint(1, 9)
    if jogada in jogadas:
        while jogada in jogadas:
            jogada = random.randint(1, 9)
    jogadas.append(jogada)
    if jogada <= 3:
        if jogada == 1:
            linha1[0] = "o"
        elif jogada == 2:
            linha1[2] = "o"
        elif jogada == 3:
            linha1[4] = "o"
    if jogada <= 6:
        if jogada == 4:
            linha2[0] = "o"
        elif jogada == 5:
            linha2[2] = "o"
        elif jogada == 6:
            linha2[4] = "o"
    if jogada <= 9:
        if jogada == 7:
            linha3[0] = "o"
        elif jogada == 8:
            linha3[2] = "o"
        elif jogada == 9:
            linha3[4] = "o"


def mensagem():
    os.system('cls') or None
    if jaganhou == 'x':
        print('Parabéns! Você Ganhou.')
        sleep(1)
        exit()

    elif jaganhou == 'o':
        print('Você perdeu! Tente outra vez.')
        sleep(1)
        exit()


def um_jogador():
    os.system('cls') or None
    global ganhou
    jogador1 = random.randint(0, 10)
    maquina = random.randint(0, 10)
    imagem_jogo()
    print("")
    jogador1_comeca = False
    tamanho_jogadas = len(jogadas)
    if jogador1 > maquina:
        jogador1_comeca = True
        while ganhou is False:
            global jaganhou
            jogador_1()
            imagem_jogo()
            sleep(2)
            jaganhou = func_ganhou()
            if jaganhou != "":
                mensagem()
            jogador_maquina()
            imagem_jogo()
            sleep(2)
            jaganhou = func_ganhou()
            if jaganhou != "":
                mensagem()
    else:
        while ganhou is False:
            jogador_maquina()
            imagem_jogo()
            sleep(2)
            jaganhou = func_ganhou()
            if jaganhou != "":
                mensagem()
            jogador_1()
            imagem_jogo()
            sleep(2)
            jaganhou = func_ganhou()
            if jaganhou != "":
                mensagem()


um_jogador()

#  _|_|_
#  _|x|_
#  _|_|_
