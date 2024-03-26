import tkinter as tk
from tkinter import messagebox, PhotoImage
import os

from tkinter import *

import random

window = tk.Tk()
window.configure(bg="green")
window.iconbitmap('/Users/dayanabarron/Desktop/War_card_game/Card pics')
window.geometry("900x700")
window.minsize(100,100)
window.maxsize(1000,1000)
greeting = Label(
    text="Blackjack",
    fg="black",
    bg="green",
    font=30,
    width=100,
    height=55
    )
greeting.pack()


#create a deck suits, rank, and values for players
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

my_frame = Frame(window, bg="green")
my_frame.pack(pady=20)
#my_frame.columnconfigure(0,minsize=250)
#my_frame.rowconfigure([0,1], minsize=100)

#Create Frames for cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)
#dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player")
player_frame.grid(row=0, column=1, ipadx=20)
#player_frame.pack(ipadx=20, pady=10)

#Place cards in frame
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)
#dealer_label.grid(row=0, column=0, pady=0, padx=0)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)
#player_label.grid(row=1, column=0, pady=0, padx=0)

def load_images():
    for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
        for rank in ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']:
            # Load card images
            card_name = 'cards/{}_{}.png'.format(rank,suit)
            if os.path.isfile(card_name):
                image = PhotoImage(file=card_name)
                image.append((card_name,image))

    create_deck()
    
playing = True
#Create a card class 
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        #create init method and its suit ad rank properties
        
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
        # strings to add rank and suit together

#Deck class
class Deck:
    def __init__(self):      
        self.deck = []        
        for suit in suits: 
            for rank in ranks:
                #create the card object
                #created_card = Card(suit,rank)
                #Create the card object
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = '' #start with empty string
        for card in self.deck:
            deck_comp+= '\n' +card.__str__() #add cards object's print string
        return 'The deck has:' + deck_comp
                
    def shuffle(self):
        #shuffle all the cards
        random.shuffle(self.deck)
        
    def shuffle_deck():
        
        deck.shuffle()
        print("Deck shuffled")
        
    def deal(self):
        #pick a card from the deck
        single_card = self.deck.pop()
        return single_card
    
    def deal_cards(self):
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal()) 
        dealer_hand.add_card(deck.deal())   
        dealer_hand.add_card(deck.deal())
        
        
        player_label.config(text=str(player_hand))     
        dealer_label.config(text=str(dealer_hand))  
        
        
        
        
class Hand:  
    def __init__(self): 
        #Player name + empty hand (self.all_cards)
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be a number!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break  

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break
    
    
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
    
    
while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    player_label.config(text='card')
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_label.config(text='card')  
         
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break

#Buttons for shuffling and dealing cards   
shuffle_button = Button(
    window,
    text="Shuffle Deck", 
    font=("Helvetica", 14),
    command=shuffle_deck
    )
shuffle_button.pack(pady=20)


def deal_cards():
    # Define the function here
    pass

button_frame = Frame(window, bg="green")
button_frame.pack(pady=20)

card_button = Button(
    window,
    text="Deal Cards",
    font=("Helvetica", 14),
    command=deal_cards 
    )
card_button.pack(pady=20)

random.shuffle()

window.mainloop()

#root.geometry("700x500")
#root.configure(background = "grey")

#my_frame = Frame(root, bg = "grey")
#my_frame.pack(pady=15)

#dealer_frame = LabelFrame(my_frame, text = "War", bd=0)
#dealer_frame.grid(row=0, column= 0, padx=20, ipadx=20)

#player_frame = LabelFrame(my_frame, text = "Player", bd =0)
#player_frame.grid(row=0, column=1, ipadx=0)

#dealer_label = Label(dealer_frame, text='')
#dealer_label.pack(pady=20)

#player_label=Label(player_frame, text='')
#player_label.pack(pady=20)

#shuffle_button = Button(root,text="Shuffle Deck",font=14 & "Helvetica")
#shuffle_button.pack(pady=20)


#deal_button = Button(root,text="Get Cards",font=14 & "Helvetica")
#deal_button.pack(pady=20)


