import random

class Deck():
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
    suits = ["♠", "♥", "♣", "♦"]
    deck = []        
            
    @classmethod
    def create_deck(cls):
        deck = []
        for value in cls.cards:
            for suit in cls.suits:
                cls.deck.append(value+suit)
                
    @classmethod
    def deal_card(cls):
        card = random.choice(cls.deck)
        cls.deck.pop(cls.deck.index(card))
        return card

class Hand(Deck):
    def __init__(self):
        self.card= Deck.deal_card()
    



new=Deck()
new.create_deck()
new1=Hand()
print(new1.card)
print(new1.deck)