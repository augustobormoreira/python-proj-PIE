import random
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Blackjack Game - PIE")
root.geometry("1200x800")
root.configure(bg="green")

# Função pro Dealer dar as cartas;
def darCartas(maoPlayer, cartas):
    try:
        carta = random.choice(cartas)
        maoPlayer.append(carta)
        cartas.remove(carta)
        root.title(f'Blackjack Game - PIE - {len(cartas)} cards remaining!')
        return carta
    except:
        root.title(f'Blackjack Game - PIE - No Cards remaining!')

def darCartasPlayer():
    global player_spot, cardPath
    global player_label_1, player_label_2, player_label_3, player_label_4, player_label_5
    if player_spot < 5:
        carta = darCartas(player, deck)
        if(player_spot==0):
            player_image_1 = resize_cards(f'{cardPath}/{carta}.png')
            player_label_1.config(image=player_image_1)
            player_spot += 1
        elif (player_spot == 1):
            player_image_2 = resize_cards(f'{cardPath}/{carta}.png')
            player_label_2.config(image=player_image_2)
            player_spot += 1
        elif (player_spot == 2):
            player_image_3 = resize_cards(f'{cardPath}/{carta}.png')
            player_label_3.config(image=player_image_3)
            player_spot += 1
        elif (player_spot == 3):
            player_image_4 = resize_cards(f'{cardPath}/{carta}.png')
            player_label_4.config(image=player_image_4)
            player_spot += 1
        elif (player_spot == 4):
            player_image_5 = resize_cards(f'{cardPath}/{carta}.png')
            player_label_5.config(image=player_image_5)
            player_spot += 1


def darCartasDealer():
    global dealer_spot
    if dealer_spot < 5:
        darCartas(dealer, deck)




def deal():
    cartaPlayer = darCartas(player, deck)
    cartaDealer = darCartas(dealer, deck)
    global dealer_image, player_image
    dealer_image = resize_cards(f'Cards/Playing Cards/PNG-cards-1.3/{cartaDealer}.png')
    player_image = resize_cards(f'Cards/Playing Cards/PNG-cards-1.3/{cartaPlayer}.png')
    dealer_label_1.config(image=dealer_image)
    player_label_1.config(image=player_image)

def resize_cards(card):
    card_img = Image.open(card)

    card_img_resized = card_img.resize((150, 218))

    global new_card_img
    new_card_img = ImageTk.PhotoImage(card_img_resized)

    return new_card_img

def shuffle():
    suits = ['diamonds', 'clubs', 'hearts', 'spades']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace']

    #Limpar cartas dos jogos antigos
    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')

    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    global dealer, player, dealer_spot, player_spot
    dealer = []
    player = []
    dealer_spot=0
    player_spot=0

    cartaDealer = darCartas(dealer, deck)
    cartaPlayer = darCartas(player, deck)
    global dealer_image, player_image
    dealer_image = resize_cards(f'Cards/Playing Cards/PNG-cards-1.3/{cartaDealer}.png')
    player_image = resize_cards(f'Cards/Playing Cards/PNG-cards-1.3/{cartaPlayer}.png')
    dealer_label_1.config(image = dealer_image)
    player_label_1.config(image = player_image)


myFrame = Frame(root, bg='green')
myFrame.pack(pady=20)

global dealerFrame, playerFrame

#Criando os frames das Cartas
dealerFrame = LabelFrame(myFrame, text="Dealer", bd=0)
dealerFrame.pack(padx=20, ipadx=20)

playerFrame = LabelFrame(myFrame, text="Player", bd=0)
playerFrame.pack(pady=20, ipadx=20)

#Colocar cartas nos frames
global cardPath
cardPath = 'Cards/Playing Cards/PNG-cards-1.3/'
global dealer_label_1, dealer_label_2, dealer_label_3, dealer_label_4, dealer_label_5
global player_label_1, player_label_2, player_label_3, player_label_4, player_label_5

dealer_label_1 = Label(dealerFrame, text='')
dealer_label_1.grid(row = 0, column= 0,pady=20, padx=20)
dealer_label_2 = Label(dealerFrame, text='')
dealer_label_2.grid(row = 0, column= 1,pady=20, padx=20)
dealer_label_3 = Label(dealerFrame, text='')
dealer_label_3.grid(row = 0, column= 2,pady=20, padx=20)
dealer_label_4 = Label(dealerFrame, text='')
dealer_label_4.grid(row = 0, column= 3,pady=20, padx=20)
dealer_label_5 = Label(dealerFrame, text='')
dealer_label_5.grid(row = 0, column= 4,pady=20, padx=20)

player_label_1 = Label(playerFrame, text='')
player_label_1.grid(row = 0, column= 0,pady=20, padx=20)
player_label_2 = Label(playerFrame, text='')
player_label_2.grid(row = 0, column= 1,pady=20, padx=20)
player_label_3 = Label(playerFrame, text='')
player_label_3.grid(row = 0, column= 2,pady=20, padx=20)
player_label_4 = Label(playerFrame, text='')
player_label_4.grid(row = 0, column= 3,pady=20, padx=20)
player_label_5 = Label(playerFrame, text='')
player_label_5.grid(row = 0, column= 4,pady=20, padx=20)


#Criando frame de botoes
buttonFrame = Frame(root, bg='green')
buttonFrame.pack(pady=20)


#Botoes necessarios
shuffleButton = Button(buttonFrame, text="Embaralhar", font=("Helvetica", 14), command=shuffle)
shuffleButton.grid(row=0, column=0)

hitButton = Button(buttonFrame, text="Pedir", font=("Helvetica", 14), command=darCartasPlayer())
hitButton.grid(row=0, column=1, padx=10)

standButton = Button(buttonFrame, text="Ficar", font=("Helvetica", 14))
standButton.grid(row=0, column=2)

shuffle()
root.mainloop()
    
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

