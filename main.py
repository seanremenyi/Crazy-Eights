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
        self.turn = users_hand.hand
        self.card = card
        self.hand_choice = self.hand_choose(self.turn) 
    
    def hand_choose(self, hand):
        hand_dict = {}
        count = 1
        while count <= len(hand):
            hand_dict[count] = hand[count-1]
            count +=1
        self.hand_choice = hand_dict
    
    def draw_card(self, hand, deck):
        hand.append(Deck.deal_card(self.deck))
        
    def choose_card(self, hand, card):
        choice = input("Choose a card")
        
    def check(self, hand, card):
        checklist = []
        for items in hand:
            checklist.append(items[0])
            checklist.append(items[1])
        if card[0] in checklist or card[1] in checklist:
            return True
        return False
        
    def play_card(self, hand, card):
    
    def users_turn():
        print(self.hand_choice)
        users_input = input("choose your card")
        if check(self.turn, self.card):
            
    
        
class CompsTurn(Deck):
    pass
    



class Game(Deck):
    deck = Deck.create_deck()
    card = Deck.deal_card(deck)
    users_hand = Hand(deck, 5)
    comps_hand = Hand(deck, 5)


    
new=Game()
new1=UsersTurn(new.deck, new.users_hand, new.card)
print(new1.__dict__) 
new1.draw_card(new1.turn, new1.deck)
print(new1.check(new1.turn, new1.card))



