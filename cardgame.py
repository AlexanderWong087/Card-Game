import random
cards=[]
suits=[["♥","♦","♣","♠"],["😃","😈","😵","🤢"],["🤡","👹","👺","👻",]]
values=["2","3","4","5","6","7","8","9","10","11","12","13","14"]
def create_deck(suit):
    for i in values:
        for j in suits[suit]:
            cards.append(f'{i}{j}')
player_cards=[]
bot_cards=[]
game_started=[False]

def rule1():
    player_check=player_cards[0][:-1]
    player_win=True
    bot_check=bot_cards[0][:-1]
    bot_win=True
    for i in player_cards:
        if i[0]==player_check:
            continue
        else:
            player_win=False
            break
    for i in bot_cards:
        if i[0]==bot_check:
            continue
        else:
            bot_win=False
            break
    if player_win==bot_win:
        return "Tie"
    elif player_win==True:
        return "Player"
    elif bot_win==True:
        return "False"
def rule2():
    player_flush=True
    bot_flush=True
    playersuit=player_cards[0][-1]
    botsuit=bot_cards[0][-1]
    for i in player_cards:
        if i[-1]==playersuit:
            continue
        else:
            player_flush=False
            break
    for j in bot_cards:
        if j[-1]==botsuit:
            continue
        else:
            bot_flush=False
            break
    if player_flush==bot_flush:
        return "Tie"
    elif player_flush==True:
        return "Player"
    else:
        return "Bot"
def rule3():
    player_win=None
    bot_win=None
    player_num=[]
    for i in player_cards:
        player_num.append(int(i[0]))
    bot_num=[]
    for i in bot_cards:
        bot_num.append(int(i[0]))
    player_num.sort()
    bot_num.sort()
    player_first=player_num[0]
    bot_first=bot_num[0]
    if (player_num[1]==player_first+1) and (player_num[2]==player_first+2) and (player_num[3]==player_first+3) and (player_num[4]==player_first+4):
        player_win=True
    if (bot_num[1]==bot_first+1) and (bot_num[2]==bot_first+2) and (bot_num[3]==bot_first+3) and (bot_num[4]==bot_first+4):
        bot_win=True
    if player_win==bot_win:
        return "Tie"
    elif player_win==True:
        return "Player"
    else:
        return "Bot"

def rule4():
    player_num=[]
    for i in player_cards:
        player_num.append(int(i[0]))
    bot_num=[]
    for i in bot_cards:
        bot_num.append(int(i[0]))
    player_avg=sum(player_num)/5
    bot_avg=sum(bot_num)/5
    if player_avg>bot_avg:
        return "Player"
    elif player_avg<bot_avg:
        return "Bot"
    else:
        return "Tie"

def check_win():
    if rule1()=="Tie":
        if rule2()=="Tie":
            if rule3()=="Tie":
                if rule4()=="Tie":
                    return "Tie"
                elif rule2()=="Player":
                    return "Player wins!"
                else:
                    return "Bot wins!"
            elif rule2()=="Player":
                return "Player wins!"
            else:
                return "Bot wins!"
        elif rule2()=="Player":
            return "Player wins!"
        else:
            return "Bot wins!"
    elif rule1=="Player":
        return "Player wins!"
    else:
        return "Bot wins!"

def start_game():
    game_started.remove(False)
    game_started.append(True)

def shuffle_deck():
    random.shuffle(cards)

def pick_card():
    length=len(cards)
    print(length)
    index=random.randint(0,length-1)
    bot_cards.append(cards[index])
    cards.pop(index)

    length=len(cards)
    index=random.randint(0,length)
    player_cards.append(cards[index])
    cards.pop(index)
        
def show_my_cards():
    print('You have: ')
    for i in player_cards:
        print(f'{i}')

def leavegame():
    exit
    
def game_menu():
    if game_started==[True]:
        print('You have the following options: ')
        print('1. Draw a Card')
        print('2. Shuffle Deck')
        print('3. Show Cards')
        print('4. Check Win')
        print('5. Exit')
        action=input('Input the number of the desired action: ')
        if action=='1':
            pick_card()
        elif action=='2':
            shuffle_deck()
        elif action=='3':
            show_my_cards()
        elif action=='4':
            print(check_win())
        else:
            leavegame()
    else:
        print('Welcome to the card game. You have the following options: ')
        print('1. Start Game')
        print('2. Exit')
        action=input('Input the number of the desired action: ')
        if action=='1':
            start_game()
        else:
            leavegame()

game_started=[True]
create_deck(1)
while True:
    game_menu()

