import platform
import os
import random

tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
coordenadas_validas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
P1 = "X"
P2 = "O"


def limpar_tela():
    comando = "cls" if platform.system() == "Windows" else "clear"
    os.system(comando)


def mostrar_tabuleiro():
    print("\n" + "-" * 27)
    print("       JOGO DA VELHA")
    print("         por Línnek")
    print("-" * 27)
    print("\n")
    print("     A   B   C")
    for i, linha in enumerate(tabuleiro):
        linha_formatada = " | ".join(linha)
        print(f"  {i + 1}  {linha_formatada}")
        if i < 2:
            print("    ---+---+---")
    print("\n")


def reiniciar_tabuleiro():
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro)):
            tabuleiro[linha][coluna] = " "


def verificar_vaga(coordenada):
    if "A" in coordenada:
        if "1" in coordenada:
            if tabuleiro[0][0] == " ":
                return True
            else:
                return False
        elif "2" in coordenada:
            if tabuleiro[1][0] == " ":
                return True
            else:
                return False
        elif "3" in coordenada:
            if tabuleiro[2][0] == " ":
                return True
            else:
                return False
    elif "B" in coordenada:
        if "1" in coordenada:
            if tabuleiro[0][1] == " ":
                return True
            else:
                return False
        elif "2" in coordenada:
            if tabuleiro[1][1] == " ":
                return True
            else:
                return False
        elif tabuleiro[2][1] == " ":
            return True
        else:
            return False
    else:
        if "1" in coordenada:
            if tabuleiro[0][2] == " ":
                return True
            else:
                return False
        elif "2" in coordenada:
            if tabuleiro[1][2] == " ":
                return True
            else:
                return False
        elif tabuleiro[2][2] == " ":
            return True
        else:
            return False


def registrar_jogada(coordenada, simbolo):
    if "A" in coordenada:
        if "1" in coordenada:
            tabuleiro[0][0] = simbolo
        elif "2" in coordenada:
            tabuleiro[1][0] = simbolo
        else:
            tabuleiro[2][0] = simbolo
    elif "B" in coordenada:
        if "1" in coordenada:
            tabuleiro[0][1] = simbolo
        elif "2" in coordenada:
            tabuleiro[1][1] = simbolo
        else:
            tabuleiro[2][1] = simbolo
    else:
        if "1" in coordenada:
            tabuleiro[0][2] = simbolo
        elif "2" in coordenada:
            tabuleiro[1][2] = simbolo
        else:
            tabuleiro[2][2] = simbolo
    return


def verificar_vencedor(simbolo):
    if (
        tabuleiro[0][0] == simbolo
        and tabuleiro[0][1] == simbolo
        and tabuleiro[0][2] == simbolo
        or tabuleiro[1][0] == simbolo
        and tabuleiro[1][1] == simbolo
        and tabuleiro[1][2] == simbolo
        or tabuleiro[2][0] == simbolo
        and tabuleiro[2][1] == simbolo
        and tabuleiro[2][2] == simbolo
        or tabuleiro[0][0] == simbolo
        and tabuleiro[1][0] == simbolo
        and tabuleiro[2][0] == simbolo
        or tabuleiro[0][1] == simbolo
        and tabuleiro[1][1] == simbolo
        and tabuleiro[2][1] == simbolo
        or tabuleiro[0][2] == simbolo
        and tabuleiro[1][2] == simbolo
        and tabuleiro[2][2] == simbolo
        or tabuleiro[0][0] == simbolo
        and tabuleiro[1][1] == simbolo
        and tabuleiro[2][2] == simbolo
        or tabuleiro[0][2] == simbolo
        and tabuleiro[1][1] == simbolo
        and tabuleiro[2][0] == simbolo
    ):
        return True
    return False


def verificar_empate():
    preenchidos = 0
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] in ["X", "O"]:
                preenchidos += 1
    return preenchidos == 9


def obter_jogada(simbolo):
    while True:
        resposta = input(
            f"🎮 Jogador {simbolo}, digite uma coordenada (ex: B2): "
        ).upper()
        limpar_tela()
        if resposta in coordenadas_validas:
            return resposta
        else:
            limpar_tela()
            mostrar_tabuleiro()
            print("⚠️ Entrada inválida! Digite uma coordenada " "como A1, B2, etc")


def computador():
    while True:
        escolha = random.choice(coordenadas_validas)
        if verificar_vaga(escolha):
            registrar_jogada(escolha, P2)
            return


def jogar_partida():
    vez = 0
    while True:
        if vez == 1:
            simbolo_atual = P2
            vez = 0
        elif vez == 0:
            simbolo_atual = P1
            vez = 1
        jogada_escolhida = obter_jogada(simbolo_atual)
        if verificar_vaga(jogada_escolhida):
            registrar_jogada(jogada_escolhida, simbolo_atual)
            limpar_tela()
            mostrar_tabuleiro()
        if verificar_vencedor(simbolo_atual):
            limpar_tela()
            mostrar_tabuleiro()
            print(f"🎉 Jogador {simbolo_atual} venceu o jogo!\n")
            reiniciar_tabuleiro()
            break
        if verificar_empate():
            limpar_tela()
            mostrar_tabuleiro()
            print("🤝 Deu velha! O tabuleiro está cheio.\n")
            reiniciar_tabuleiro()
            break


def jogar_partida_vs_computador():
    vez = 0
    while True:
        if vez == 0:
            simbolo_atual = P1
        else:
            simbolo_atual = P2
        if vez == 0:
            jogada_escolhida = obter_jogada(simbolo_atual)
            if verificar_vaga(jogada_escolhida):
                registrar_jogada(jogada_escolhida, simbolo_atual)
                limpar_tela()
                mostrar_tabuleiro()
                vez = 1
        else:
            computador()
            limpar_tela()
            mostrar_tabuleiro()
            vez = 0
        if verificar_vencedor(simbolo_atual):
            limpar_tela()
            mostrar_tabuleiro()
            print(f"🎉 Jogador {simbolo_atual} venceu o jogo!\n")
            reiniciar_tabuleiro()
            break
        if verificar_empate():
            limpar_tela()
            mostrar_tabuleiro()
            print("🤝 Deu velha! O tabuleiro está cheio.\n")
            reiniciar_tabuleiro()
            break


def menu_principal():
    mostrar_tabuleiro()
    while True:
        print("🎮 MENU PRINCIPAL")
        print("1 - Jogar contra outro jogador")
        print("2 - Modo contra IA (Fácil)")
        print("3 - Sair\n")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            limpar_tela()
            mostrar_tabuleiro()
            jogar_partida()
        elif escolha == "2":
            limpar_tela()
            mostrar_tabuleiro()
            jogar_partida_vs_computador()
        elif escolha == "3":
            limpar_tela()
            mostrar_tabuleiro()
            print("👋 Valeu por jogar! Até a próxima.\n")
            break
        else:
            limpar_tela()
            mostrar_tabuleiro()
            print("❌ Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu_principal()
