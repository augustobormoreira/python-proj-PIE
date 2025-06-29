import random
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

root = Tk()
root.title("Blackjack Game - PIE")
root.geometry("1200x900")
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

#Funcao pra apostar tudo o que tem
def make_allin():
    global betValue
    betValue = curScore

#Funcao pra apostar 100 fichas
def make_bet100():
    global betValue
    betValue = 100

#Funcao pra apostar 500 fichas
def make_bet500():
    global betValue
    betValue = 500

#Funcao pra enquadrar as cartas nas labels, arrumando o tamanho delas
def resize_cards(card):
    card_img = Image.open(card)

    card_img_resized = card_img.resize((150, 218))

    global new_card_img
    new_card_img = ImageTk.PhotoImage(card_img_resized)

    return new_card_img

#Funcao principal praticamente, cria o player e o dealer, o baralho, abre o arquivo de recorde de score, cria  as variaveis
#globais, dá as primeiras duas cartas de cada mao e limpa as labels que tinha cartas dos jogos anteriores
def shuffle():
    hitButton.config(state='normal')
    standButton.config(state='normal')

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

    global dealer, player, dealer_spot, player_spot, player_score, dealer_score, maxScore, curScore, betValue
    maxScorePath = 'max_score.txt'
    with open(maxScorePath, 'r') as maxScoreFile:
        maxScore = maxScoreFile.read()
    betValue = 0
    dealer = []
    player = []
    player_score = []
    dealer_score = []
    dealer_spot=0
    player_spot=0

    for _ in range(2):
        darCartasPlayer()
        darCartasDealer()

#Funcao pra revelar a carta escondida da mao do dealer
def reveal_dealer_card():
    print(f'Dealer Score: {check_person_score(dealer_score)}')
    dealer_label_1.config(image=dealer_image_1)

#Funcao pra dar as cartas pro dealer, como tem que mexer em label teve q mudar muita coisa, usa a funcao darCartas como base
def darCartasDealer():
    global dealer_spot, cardPath, dealer
    if dealer_spot < 5:
        carta = darCartas(dealer, deck)
        global dealer_upside_down_image_1, dealer_image_1, dealer_image_2, dealer_image_3, dealer_image_4, dealer_image_5
        if (dealer_spot == 0):
            dealer_image_1 = resize_cards(f'{cardPath}{carta}.png')
            dealer_upside_down_image_1 = resize_cards(f'{cardPath}upside_down_card.png')
            dealer_label_1.config(image=dealer_upside_down_image_1)
            dealer_spot += 1
        elif (dealer_spot == 1):
            dealer_image_2 = resize_cards(f'{cardPath}{carta}.png')
            dealer_label_2.config(image=dealer_image_2)
            dealer_spot += 1
        elif (dealer_spot == 2):
            dealer_image_3 = resize_cards(f'{cardPath}{carta}.png')
            dealer_label_3.config(image=dealer_image_3)
            dealer_spot += 1
        elif (dealer_spot == 3):
            dealer_image_4 = resize_cards(f'{cardPath}{carta}.png')
            dealer_label_4.config(image=dealer_image_4)
            dealer_spot += 1
        elif (dealer_spot == 4):
            dealer_image_5 = resize_cards(f'{cardPath}{carta}.png')
            dealer_label_5.config(image=dealer_image_5)
            dealer_spot += 1

        cartaValue = carta.split('_', 1)[0]
        if (cartaValue == 'ace'):
            dealer_score.append(11)
        elif (cartaValue == 'jack' or cartaValue == 'queen' or cartaValue == 'king'):
            dealer_score.append(10)
        elif (cartaValue == '1' or cartaValue == '2' or cartaValue == '3' or cartaValue == '4' or cartaValue == '5'
              or cartaValue == '6' or cartaValue == '7' or cartaValue == '8' or cartaValue == '9' or cartaValue == '10'):
            dealer_score.append(int(cartaValue))
        check_person_score(dealer_score)

#Funcao pra dar as cartas pro player, como tem q mexer em label teve q mudar muita coisa, usa a funcao darCartas como base
def darCartasPlayer():
    global player_spot, cardPath, player
    if player_spot < 5:
        carta = darCartas(player, deck)
        global player_image_1, player_image_2, player_image_3, player_image_4, player_image_5
        if(player_spot==0):
            player_image_1 = resize_cards(f'{cardPath}{carta}.png')
            player_label_1.config(image=player_image_1)
            player_spot += 1
        elif (player_spot == 1):
            player_image_2 = resize_cards(f'{cardPath}{carta}.png')
            player_label_2.config(image=player_image_2)
            player_spot += 1
        elif (player_spot == 2):
            player_image_3 = resize_cards(f'{cardPath}{carta}.png')
            player_label_3.config(image=player_image_3)
            player_spot += 1
        elif (player_spot == 3):
            player_image_4 = resize_cards(f'{cardPath}{carta}.png')
            player_label_4.config(image=player_image_4)
            player_spot += 1
        elif (player_spot == 4):
            player_image_5 = resize_cards(f'{cardPath}{carta}.png')
            player_label_5.config(image=player_image_5)
            player_spot += 1

        cartaValue = carta.split('_', 1)[0]
        if (cartaValue == 'ace'):
            player_score.append(11)
        elif (cartaValue == 'jack' or cartaValue == 'queen' or cartaValue == 'king'):
            player_score.append(10)
        elif (cartaValue == '1' or cartaValue == '2' or cartaValue == '3' or cartaValue == '4' or cartaValue == '5'
              or cartaValue == '6' or cartaValue == '7' or cartaValue == '8' or cartaValue == '9' or cartaValue == '10'):
            player_score.append(int(cartaValue))
        score = check_person_score(player_score)
        if(score > 21):
            check_winner()

#Verifica o score da mao da pessoa que recebeu como parametro, pode ser o dealer ou o player
def check_person_score(person_score):
    tempScoreToStorePlayerScore = 0
    for score in person_score:
        tempScoreToStorePlayerScore += score
        if(tempScoreToStorePlayerScore>21):
            if(check_if_has_eleven_and_turn_into_one(person_score)):
                tempScoreToStorePlayerScore -= 11
                tempScoreToStorePlayerScore += 1

    return tempScoreToStorePlayerScore

#Funcao pra verificar se tem algum 11 na mao da pessoa(dealer ou player) e trocar por 1, é usada no caso de estouro
def check_if_has_eleven_and_turn_into_one(person_score):
    has11= False
    for score in person_score:
        if(score == 11):
            person_score.remove(score)
            person_score.append(1)
            return True
    return has11

#Funcao pra dar as cartas pro dealer depois que o usuario ou estoura ou clica em Ficar
def deal_dealer_cards():
    while(check_person_score(dealer_score) <=17):
        darCartasDealer()

#Salva o max score no arquivo max_score e arruma a label de maior score
def set_max_score():
    global maxScore, maxScoreLabel
    maxScorePath = 'max_score.txt'
    with open(maxScorePath, 'w') as maxScoreFile:
        maxScoreFile.write(str(maxScore))
        maxScoreLabel.config(text=f'Maior Score: {maxScore}')
        maxScoreFile.close()

#Funcao pra verificar o vencedor, desativa os botoes e arruma as bets
def check_winner():
    global curScore, betValue, maxScore

    reveal_dealer_card()
    deal_dealer_cards()

    if(len(player_score)==2 and check_person_score(player_score) == 21):
        messagebox.showinfo('Blackjack!',  f'Você ganhou! Seu score = {player_score}')
        hitButton.config(state='disabled')
        standButton.config(state='disabled')
        curScore += betValue
        curScoreLabel.config(text=f'Score atual: {curScore}')
    elif(check_person_score(player_score) > 21):
        messagebox.showinfo('Derrota!', 'Você estorou!')
        hitButton.config(state='disabled')
        standButton.config(state='disabled')
        curScore -= betValue
        curScoreLabel.config(text=f'Score atual: {curScore}')
    elif (check_person_score(player_score) < check_person_score(dealer_score) and check_person_score(
        dealer_score) > 21):
        messagebox.showinfo('Vitória!', 'O Dealer estorou!')
        hitButton.config(state='disabled')
        standButton.config(state='disabled')
        curScore += betValue
        curScoreLabel.config(text=f'Score atual: {curScore}')
    elif(check_person_score(player_score) > check_person_score(dealer_score)):
        messagebox.showinfo('Vitória!', 'Você ganhou!')
        hitButton.config(state='disabled')
        standButton.config(state='disabled')
        curScore += betValue
        curScoreLabel.config(text=f'Score atual: {curScore}')
    elif(check_person_score(player_score) == check_person_score(dealer_score)):
        messagebox.showinfo('Empate!', 'Você e o dealer empataram! Aposta devolvida!')
        hitButton.config(state='disabled')
        standButton.config(state='disabled')
    elif(check_person_score(player_score) < check_person_score(dealer_score)):
        messagebox.showinfo('Derrota!', 'Você perdeu!')
        hitButton.config(state='disabled')
        standButton.config(state='disabled')
        curScore -= betValue
        curScoreLabel.config(text=f'Score atual: {curScore}')

    betValue = 0
    if(int(curScore) > int(maxScore)):
        maxScore = curScore
        set_max_score()

#Cria frame principal
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

global hitButton, shuffleButton, standButton
#Botoes necessarios
shuffleButton = Button(buttonFrame, text="Embaralhar", font=("Helvetica", 14), command=shuffle)
shuffleButton.grid(row=0, column=0)

hitButton = Button(buttonFrame, text="Pedir", font=("Helvetica", 14), command=darCartasPlayer)
hitButton.grid(row=0, column=1, padx=10)

standButton = Button(buttonFrame, text="Ficar", font=("Helvetica", 14), command=check_winner)
standButton.grid(row=0, column=2)

#Chama essa funcao de inicio pra começar tudo
shuffle()
curScore = 1000

#Frame de score
global curScoreLabel, maxScoreLabel
scoreFrame = Frame(root, bg='green')
scoreFrame.pack(pady=20)

maxScoreLabel = Label(scoreFrame, text=f'Maior Score: {maxScore}', font=("Helvetica", 14))
maxScoreLabel.grid(row=0, column=0, ipady=10, ipadx=10)

curScoreLabel = Label(scoreFrame, text=f'Score atual: {curScore}', font=("Helvetica", 14))
curScoreLabel.grid(row=0, column=1, ipady=10, ipadx=10)


#Frame de botao de apostas
betsFrame = Frame(root, bg='green')
betsFrame.pack(pady=20)

bet100Button = Button(betsFrame,font=("Helvetica", 14), text="Bet 100", command=make_bet100)
bet100Button.grid(row=0, column=0, padx=10)

bet500Button = Button(betsFrame,font=("Helvetica", 14), text="Bet 500", command=make_bet500)
bet500Button.grid(row=0, column=1, padx=10)

betAllInButton = Button(betsFrame,font=("Helvetica", 14), text="All In", command=make_allin)
betAllInButton.grid(row=0, column=2, padx=10)

root.mainloop()
'''   
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

'''