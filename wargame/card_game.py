# War game
'''
War card game takes input from two players who will be given an equal amount of cards.
Those cards will be randomly chosen. Each player will "place a card on the deck" and whichever card is 
of greater value, that player will take all the cards on the deck. 
'''

import random
#create a deck suits, rank, and values for players
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#Create a card class 
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
        #create init method and its suit ad rank properties
        
    
    def __str__(self):
        return self.rank + " of " + self.suit
        # strings to add rank and suit together

#Deck class
class Deck:
    def __init__(self):      
        self.all_cards = []        
        for suit in suits: 
            for rank in ranks:
                #create the card object
                created_card = Card(suit,rank)
                #Create the card object
                self.all_cards.append(created_card)
                
    def shuffle(self):
        #shuffle all the cards
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        #pick a card from the deck
        return self.all_cards.pop()
        
        
class Player:  
    def __init__(self,name): 
        #Player name + empty hand (self.all_cards)
        self.name = name
        self.all_cards = []
         
    def remove_one(self):
        return self.all_cards.pop(0)
    #remove a card
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            #List of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            #Single card object
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    
     
#GAME SETUP
player_one = Player("One")
player_two = Player("Two")
new_deck = Deck()
new_deck .shuffle()
 
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#Game on
GAME_ON = True
ROUND_NUM = 0

def new_func(player_one):
    return player_one.remove_one()

while GAME_ON: 
    ROUND_NUM += 1
    print(f"Round {ROUND_NUM}")
    
    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        GAME_ON = False
        break
        
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!')
        GAME_ON = False
        break   
    #START NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(new_func(player_one))
    
    
    '''
    while at war
    '''
    at_war = True

    while at_war: 
    
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
            
        else:
            print('War!')  
            
            if len(player_one.all_cards) < 5:
                print('Player One unable to play war')
                print('Player Two Wins!')
                GAME_ON = False
                break
                
            if len(player_two.all_cards) < 5:
                print('Player Two unable to play war')
                print('Player One Wins!')
                GAME_ON = False
                break
        
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    

