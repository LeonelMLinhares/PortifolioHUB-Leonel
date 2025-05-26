import random
import time
import os
from enum import Enum


class Opcoes(Enum):
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3
    SPOCK = 4
    LAGARTO = 5


class Resultado(Enum):
    VITORIA = 1
    DERROTA = 2
    EMPATE = 3


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_placar(vitorias, derrotas, empates):
    print("\n" + "=" * 40)
    print(f" PLACAR: Você {vitorias} x {derrotas} Computador (Empates: {empates}) ")
    print("=" * 40 + "\n")


def animacao_contagem():
    print("Jo...")
    time.sleep(0.7)
    print("Ken...")
    time.sleep(0.7)
    print("Pô!")
    time.sleep(0.5)


def mostrar_opcoes():
    print("\nEscolha uma opção:")
    for opcao in Opcoes:
        print(f"{opcao.value} - {opcao.name.capitalize()}")
    print("0 - Sair do jogo")


def obter_escolha_jogador():
    while True:
        try:
            escolha = int(input("\nSua escolha: "))
            if escolha == 0:
                return None
            if any(escolha == opcao.value for opcao in Opcoes):
                return Opcoes(escolha)
            print(f"Opção inválida. Escolha um número entre 1 e {len(Opcoes)} ou 0 para sair.")
        except ValueError:
            print("Por favor, digite um número válido.")


def obter_escolha_computador():
    return random.choice(list(Opcoes))


def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return Resultado.EMPATE

    regras = {
        Opcoes.PEDRA: [Opcoes.TESOURA, Opcoes.LAGARTO],
        Opcoes.PAPEL: [Opcoes.PEDRA, Opcoes.SPOCK],
        Opcoes.TESOURA: [Opcoes.PAPEL, Opcoes.LAGARTO],
        Opcoes.SPOCK: [Opcoes.TESOURA, Opcoes.PEDRA],
        Opcoes.LAGARTO: [Opcoes.SPOCK, Opcoes.PAPEL]
    }

    return Resultado.VITORIA if computador in regras[jogador] else Resultado.DERROTA


def mostrar_resultado(jogador, computador, resultado):
    print(f"\nVocê escolheu: {jogador.name.capitalize()}")
    print(f"Computador escolheu: {computador.name.capitalize()}")

    time.sleep(1)

    if resultado == Resultado.EMPATE:
        print("\n>>> EMPATE! <<<")
    elif resultado == Resultado.VITORIA:
        print(f"\n>>> VOCÊ GANHOU! {jogador.name.capitalize()} vence {computador.name.capitalize()} <<<")
    else:
        print(f"\n>>> VOCÊ PERDEU! {computador.name.capitalize()} vence {jogador.name.capitalize()} <<<")


def jokenpo_avancado():
    limpar_tela()
    print("=" * 40)
    print(" BEM-VINDO AO JOKENPÔ AVANÇADO! ".center(40))
    print("=" * 40)
    print(" Regras:".center(40))
    print(" Pedra quebra Tesoura e esmaga Lagarto")
    print(" Papel cobre Pedra e refuta Spock")
    print(" Tesoura corta Papel e decapita Lagarto")
    print(" Spock vaporiza Pedra e quebra Tesoura")
    print(" Lagarto come Papel e envenena Spock")
    print("=" * 40)

    vitorias = 0
    derrotas = 0
    empates = 0

    while True:
        mostrar_placar(vitorias, derrotas, empates)
        mostrar_opcoes()

        jogador = obter_escolha_jogador()
        if jogador is None:
            break

        computador = obter_escolha_computador()

        limpar_tela()
        animacao_contagem()

        resultado = determinar_vencedor(jogador, computador)
        mostrar_resultado(jogador, computador, resultado)

        if resultado == Resultado.VITORIA:
            vitorias += 1
        elif resultado == Resultado.DERROTA:
            derrotas += 1
        else:
            empates += 1

        time.sleep(2)
        limpar_tela()

    mostrar_placar(vitorias, derrotas, empates)
    print("Obrigado por jogar! Até mais!")


if __name__ == "__main__":
    jokenpo_avancado()