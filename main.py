import random

class Deck():
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
    suits = ["♠", "♥", "♣", "♦"]
            
    @classmethod
    def create_deck(cls):
        deck = []
        for value in cls.cards:
            for suit in cls.suits:
                deck.append(value+suit)
        return deck
                
    @classmethod
    def deal_card(cls, deck):
        card = random.choice(deck)
        deck.pop(deck.index(card))
        return card

class Hand(Deck):
    def __init__(self, deck, num):
        self.hand = []
        [self.hand.append(Deck.deal_card(deck)) for items in range(num)]

class UsersTurn(Deck):
    
    def __init__(self, deck, users_hand, card):
        self.deck = deck
        self.turn = self.hand(users_hand.hand)
        self.card = card
    
    def hand(self, hand):
        hand_dict = {}
        count = 1
        while count <= len(hand):
            hand_dict[count] = hand[count-1]
            count +=1
        return hand_dict

class CompsTurn(Deck):
    pass

class Game(Deck):
    deck = Deck.create_deck()
    card = Deck.deal_card(deck)
    users_hand = Hand(deck, 5)
    comps_hand = Hand(deck, 5)


    
new=Game()
new1=UsersTurn(new.deck, new.users_hand, new.card)
print(new1.turn)