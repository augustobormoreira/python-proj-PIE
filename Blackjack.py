import random
from tkinter import *

root = Tk()
root.title("Blackjack Game - PIE")
root.geometry("900x500")
root.configure(bg="green")

def embaralhar():
    suits = ['diamonds', 'clubs', 'hearts', 'spades']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']


    global deck
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    global maoDoDealer, maoDoJogador
    maoDoDealer = []
    maoDoJogador = []

    darCartas(maoDoDealer, deck)
    darCartas(maoDoJogador, deck)


myFrame = Frame(root, bg='green')
myFrame.pack(pady=20)


#Criando os frames das Cartas
dealerFrame = LabelFrame(myFrame, text="Dealer", bd=0)
dealerFrame.grid(row=0, column=0, padx=20, ipadx=20)

playerFrame = LabelFrame(myFrame, text="Player", bd=0)
playerFrame.grid(row=0, column=1, ipadx=20)

#Colocar cartas nos frames
dealerLabel = Label(dealerFrame, text="")
dealerLabel.pack(pady=20)

playerLabel = Label(playerFrame, text="")
playerLabel.pack(pady=20)

#Botoes necessarios
shuffleButton = Button(root, text="Embaralhar", font=("Helvetica", 14), command=shuffle)
shuffleButton.pack(pady=20)

cardButton = Button(root, text="Receber Cartas", font=("Helvetica", 14))
cardButton.pack(pady=20)

root.mainloop()


# Função pro Dealer dar as cartas;
def darCartas(Rodada, cartas):
    carta = random.choice(cartas)
    Rodada.append(carta)
    cartas.remove(carta)
    
# Calcular a mão do player e do Dealer;
def totaldeCartas(Rodada):
    total = 0
    fcarta = ['J', 'K', 'Q'] #Caso queira mudar para 11,12 e 13 fique a vontade, mas precisa alterar os ifs do 14 ao 23;
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

# Adicionando fichas/pontos;

fichas = 500;

while resposta.lower() == "sim":

    jogador = True
    dealer = True
    #Talvez uma função de criar mais players contra o Dealer?

    # Pacotes de cartas / Mão do Dealer;
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
    #Fazer uma matriz que organize as cartas por cor, tipo e numero;
    maodoJogador = [] 
    maodoDealer = []
    
     # Verificando saldo de fichas do jogador: 
    print(f"\nVocê tem {fichas} fichas.")
    if fichas <= 0:
        print("Você ficou sem fichas! Fim de jogo.\n")
        break
    
    while True:
        print(f"Digite um valor para apostar ou aposte tudo(all-in). Você tem {fichas} fichas");
        entrada = input("Aposta: ").strip().lower()
        if entrada == "all-in":
            aposta = fichas
            break
        else:
            try:
                aposta = int(entrada)
                if 0 < aposta <= fichas:
                    break
                else:
                    print(f"Aposta inválida! Not enough cash stranger! Você ainda tem {fichas} fichas\n")
            except ValueError:
                print("Digite um numero de fichas que deseja apostar ou aposte tudo(All-in).");
        

    # Iniciar uma partida;
    ganho = int(aposta * 2.5)
    for _ in range(2):
        darCartas(maodoDealer, cartas)
        darCartas(maodoJogador, cartas)

    while jogador or dealer: #Acho que consegui resolver o problema do Dealer mas dá uma olhada as vezes eu fiz uma merda e não percebi até agora :)
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

    if totaldeCartas(maodoJogador) == 21 and len(maodoJogador) == 2: #Caso queira remover o metodo empate, eu acho que não precisa
        print(f"\n Você tem {maodoJogador} totalizando: {totaldeCartas(maodoJogador)}. Enquanto o Dealer tem {maodoDealer} totalizando: {totaldeCartas(maodoDealer)}")
        fichas += ganho - aposta;
        print(f"lackjack! Você ganhou {ganho} fichas ficando com {fichas} fichas \n");
    elif totaldeCartas(maodoDealer) == 21 and len(maodoDealer) == 2:
        print(f"\n Você tem {maodoJogador} totalizando: {totaldeCartas(maodoJogador)}. Enquanto o Dealer tem {maodoDealer} totalizando: {totaldeCartas(maodoDealer)}")
        fichas -= aposta;
        print(f"BlackJack! O Dealer ganhou! você perdeu {aposta} fichas ficando com {fichas}");
    elif totaldeCartas(maodoJogador) > 21:
        print(f"\n Você tem {maodoJogador} \n")
        print(f"Você estourou o numero de cartas ficando com {totaldeCartas(maodoJogador)}! O Dealer ganhou!\n")
        fichas -= aposta;
        print(f"você perdeu {aposta} fichas, ficando com {fichas}")
    elif totaldeCartas(maodoDealer) > 21:
        print(f"\n O Dealer tem {maodoDealer} \n")
        fichas += ganho - aposta;
        print(f"O Dealer estourou o numero de cartas! Você ganhou {ganho} fichas, ficando com {fichas} fichas\n")
    elif 21 - totaldeCartas(maodoDealer) < 21 - totaldeCartas(maodoJogador):
        print(f"\n Você tem {maodoJogador} de um total de {totaldeCartas(maodoJogador)}. Enquanto o Dealer tem {maodoDealer} totalizando: {totaldeCartas(maodoDealer)}")
        fichas -= aposta;
        print(f"O Dealer ganhou! você perdeu {aposta} fichas ficando com {fichas} fichas")
    elif 21 - totaldeCartas(maodoDealer) > 21 - totaldeCartas(maodoJogador):
        print(f"\n Você tem {maodoJogador} de um total de {totaldeCartas(maodoJogador)}. Enquanto o Dealer tem {maodoDealer} totalizando: {totaldeCartas(maodoDealer)}")
        fichas += ganho - aposta;
        print(f"Você ganhou {ganho} fichas, ficando com {fichas} fichas ")
    else:
        print(f"\n Você tem {maodoJogador} de um total de {totaldeCartas(maodoJogador)}. Enquanto o Dealer tem {maodoDealer} totalizando: {totaldeCartas(maodoDealer)}")
        print("Empate! Você não perdeu/ganhou fichas!")

    # Perguntar se deseja continuar jogando:
    while True:
        resposta = input("\nDeseja jogar novamente? (Sim/Não): ")
        if resposta.lower() in ["sim", "nao","não"]:
            break
        else:
            print("\nEntrada inválida! Por favor digite apenas 'Sim' ou 'Não'.")

