import random

# Função pro Dealer dar as cartas;
def darCartas(Rodada, cartas):
    carta = random.choice(cartas)
    Rodada.append(carta)
    cartas.remove(carta)

# Calcular a mão do player e do Dealer;
def totaldeCartas(Rodada):
    total = 0
    fcarta = ['J', 'K', 'Q']
    for carta in Rodada:
        if isinstance(carta, int):
            total += carta
        elif carta in fcarta:
            total += 10
        elif carta == 'A':
            if total + 11 > 21:
                total += 1
            else:
                total += 11
    return total

# Verificar a mão do Dealer;
def verMao(maodoDealer):
    if len(maodoDealer) == 2:
        return maodoDealer[0]
    elif len(maodoDealer) > 2:
        return maodoDealer[0], maodoDealer[1]

# Começar com resposta = sim
resposta = "sim"

while resposta.lower() == "sim":

    jogador = True
    dealer = True

    # Pacotes de cartas / Mão do Dealer;
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
    maodoJogador = []
    maodoDealer = []

    # Iniciar uma partida;
    for _ in range(2):
        darCartas(maodoDealer, cartas)
        darCartas(maodoJogador, cartas)

    while jogador or dealer:
        print(f"O Dealer tem um {verMao(maodoDealer)} e mais uma carta\n")
        print(f"Você tem {maodoJogador} totalizando {totaldeCartas(maodoJogador)}\n")
        if jogador:
            print("Escolha uma das opções: \n")
            stayOuHit = input("1: Manter suas mão de cartas(Stay) \n2: Pega mais uma carta(Hit)\n")
            print(f"Você escolheu a opção: {stayOuHit} \n")
            if stayOuHit == '1':
                jogador = False
            elif stayOuHit == '2':
                darCartas(maodoJogador, cartas)
                print(f"Suas cartas são: {maodoJogador}\n")
        if dealer:
            while totaldeCartas(maodoDealer) < 17:
                darCartas(maodoDealer, cartas)
            dealer = False
        if totaldeCartas(maodoJogador) >= 21 or totaldeCartas(maodoDealer) >= 21:
            break

    if totaldeCartas(maodoJogador) == 21:
        print(f"\n Você tem {maodoJogador} totalizando: {totaldeCartas(maodoJogador)}. Enquanto o Dealer tem {maodoDealer} totalizando: {totaldeCartas(maodoDealer)}")
        print("Blackjack! Você ganhou.")
    elif totaldeCartas(maodoDealer) == 21:
        print(f"\n Você tem {maodoJogador} totalizando: {totaldeCartas(maodoJogador)}. Enquanto o Dealer tem {maodoDealer} totalizando: {totaldeCartas(maodoDealer)}")
        print("BlackJack! O Dealer ganhou!")
    elif totaldeCartas(maodoJogador) > 21:
        print(f"\n Você tem {maodoJogador} \n")
        print(f"Você estourou o numero de cartas ficando com {totaldeCartas(maodoJogador)}! O Dealer ganhou!\n")
    elif totaldeCartas(maodoDealer) > 21:
        print(f"\n O Dealer tem {maodoDealer} \n")
        print("O Dealer estourou o numero de cartas! Você ganhou!\n")
    elif 21 - totaldeCartas(maodoDealer) < 21 - totaldeCartas(maodoJogador):
        print(f"\n Você tem {maodoJogador} de um total de {totaldeCartas(maodoJogador)}. Enquanto o Dealer tem {maodoDealer} totalizando: {totaldeCartas(maodoDealer)}")
        print("O Dealer ganhou!")
    elif 21 - totaldeCartas(maodoDealer) > 21 - totaldeCartas(maodoJogador):
        print(f"\n Você tem {maodoJogador} de um total de {totaldeCartas(maodoJogador)}. Enquanto o Dealer tem {maodoDealer} totalizando: {totaldeCartas(maodoDealer)}")
        print("Você ganhou!")
    else:
        print(f"\n Você tem {maodoJogador} de um total de {totaldeCartas(maodoJogador)}. Enquanto o Dealer tem {maodoDealer} totalizando: {totaldeCartas(maodoDealer)}")
        print("Empate!")

    # Perguntar se deseja continuar jogando:
    while True:
        resposta = input("\nDeseja jogar novamente? (Sim/Não): ")
        if resposta.lower() in ["sim", "nao","não"]:
            break
        else:
            print("\nEntrada inválida! Por favor digite apenas 'Sim' ou 'Não'.")
