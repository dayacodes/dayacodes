import random
from Card import Card

class SixDeck():
    
    def __init__(self):
        self.cards = []
        self.build()
                
    def build(self):
        for i in range(0, 6):
            for j in ["Hearts", "Diamonds", "Clubs", "Spades"]:
                for k in range(1, 14):
                    self.cards.append(Card(k, j))  # Indent this line one level further
        
    def shuffle(self):
        for i in range(1,15):
            for i in range(len(self.cards)-1, 0, -1):
                r = random.randint(0, i)
                self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
                
    def draw(self):
        return self.cards.pop()
    
    def length(self):
        return len(self.cards)
    
    def deckReset(self):
        self.cards = []
        self.built()
    
   