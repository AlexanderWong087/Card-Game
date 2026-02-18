cards=[]
for i in (1,2,3,4,5,6,7,8,9,10,11,12,13):
    for j in ('♥','♦','♣'.'♠'):
        cards.append(f'{i} of {j}')
player_cards=[]
bot_cards=[]
game_started=[False]

def start_game():
    game_started.remove(False)
    game_started.append(True)

def shuffle_deck():
    random.shuffle(cards)

def pick_card(side):
    length=len(cards)
    index=random.randint(0,length)
    if side=='Computer':
        bot_cards.append(cards[index])
        cards.pop(index)
    elif side=='Player':
        player_cards.append(cards[index])
        cards.pop(index)
        
def show_my_cards():
    print('You have: ')
    for i in player_cards:
        print(f'{i}')
        
def check_win():
    winner='undefined'
    if player_cards=[]

def exit():
    exit

def game_menu():
    action=input('Input an action: ')
    if action=='Shuffle Deck':
        shuffle_deck()
